"""Pruebas de los escenarios de specs/001-postularse/spec.md (CU-01)."""
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from aplicacion.dto.postulacion_entrada import PostulacionEntrada  # noqa: E402
from aplicacion.postularse_a_practica import PostularseAPractica  # noqa: E402
from aplicacion.verificar_postulacion import VerificarPostulacion  # noqa: E402
from dominio.tarea_pendiente import FALLIDA, MAXIMO_INTENTOS  # noqa: E402
from infraestructura.bitacora_en_memoria import BitacoraEnMemoria  # noqa: E402
from infraestructura.consulta_academica_en_memoria import (  # noqa: E402
    ConsultaAcademicaEnMemoria,
)
from infraestructura.procesador_de_tareas import ProcesadorDeTareas  # noqa: E402
from infraestructura.repositorio_postulaciones_en_memoria import (  # noqa: E402
    RepositorioPostulacionesEnMemoria,
)

INICIO = datetime(2026, 1, 1, 8, 0, 0)


class Entorno:
    def __init__(self, **sia):
        self.reloj = INICIO
        self.repositorio = RepositorioPostulacionesEnMemoria()
        self.bitacora = BitacoraEnMemoria()
        self.sia = ConsultaAcademicaEnMemoria(**sia)
        ahora = lambda: self.reloj  # noqa: E731
        self.postularse = PostularseAPractica(self.repositorio, self.bitacora, ahora)
        self.verificar = VerificarPostulacion(
            self.repositorio, self.sia, self.bitacora, ahora
        )
        self.procesador = ProcesadorDeTareas(self.repositorio, self.verificar, ahora)

    def avanzar(self, segundos: float) -> None:
        self.reloj += timedelta(seconds=segundos)

    def estado(self, estudiante: str = "u1") -> str:
        return self.repositorio.buscar_postulacion_activa(estudiante).estado.value

    def eventos(self) -> list[str]:
        return [e[1] for e in self.bitacora.eventos]


def entrada(**cambios) -> PostulacionEntrada:
    datos = dict(
        usuario_id="u1",
        rol="estudiante",
        programa_id="ingenieria",
        empresa="Empresa S.A.",
        supervisor="Ana Pérez",
        autorizo_datos=True,
        version_reglas_vigente="v1",
    )
    return PostulacionEntrada(**{**datos, **cambios})


def test_postulacion_verificada_correctamente():
    e = Entorno()
    salida = e.postularse.ejecutar(entrada())
    assert salida.aceptada and salida.estado == "pendiente de verificación"
    assert "recibida" in salida.mensaje
    e.procesador.procesar_pendientes()
    assert e.estado() == "verificada"
    assert e.eventos() == ["postulacion_recibida", "postulacion_verificada"]


def test_estudiante_no_cumple_requisitos():
    e = Entorno(requisitos_faltantes=["promedio mínimo"])
    e.postularse.ejecutar(entrada())
    e.procesador.procesar_pendientes()
    postulacion = next(iter(e.repositorio._postulaciones.values()))
    assert postulacion.estado.value == "no cumple requisitos"
    tarea = next(iter(e.repositorio._tareas.values()))
    assert tarea.estado == "completada"


def test_mensaje_indica_requisito_faltante():
    e = Entorno(requisitos_faltantes=["promedio mínimo"])
    e.postularse.ejecutar(entrada())
    tarea = next(iter(e.repositorio._tareas.values()))
    assert "promedio mínimo" in e.verificar.ejecutar(tarea.id).mensaje


def test_sin_autorizacion_de_datos_no_se_guarda():
    e = Entorno()
    salida = e.postularse.ejecutar(entrada(autorizo_datos=False))
    assert not salida.aceptada and "autorizar" in salida.mensaje
    assert not e.repositorio._postulaciones and not e.repositorio._tareas


def test_postulacion_activa_se_rechaza_e_informa_estado():
    e = Entorno()
    e.postularse.ejecutar(entrada())
    salida = e.postularse.ejecutar(entrada())
    assert not salida.aceptada
    assert salida.estado == "pendiente de verificación"
    assert len(e.repositorio._postulaciones) == 1
    e.procesador.procesar_pendientes()
    assert e.postularse.ejecutar(entrada()).estado == "verificada"


def test_programa_sin_reglas_publicadas():
    e = Entorno()
    salida = e.postularse.ejecutar(entrada(version_reglas_vigente=None))
    assert not salida.aceptada and "director de programa" in salida.mensaje
    assert not e.repositorio._postulaciones


def test_usuario_no_estudiante_se_deniega_y_se_registra():
    e = Entorno()
    with pytest.raises(PermissionError):
        e.postularse.ejecutar(entrada(rol="docente asesor"))
    assert e.eventos() == ["acceso_denegado"]
    assert not e.repositorio._postulaciones


def test_sia_caido_guarda_confirma_y_reintenta_sin_intervencion():
    e = Entorno(falla=True)
    inicio = time.perf_counter()
    salida = e.postularse.ejecutar(entrada())
    assert time.perf_counter() - inicio < 2
    assert salida.aceptada and e.estado() == "pendiente de verificación"

    e.procesador.procesar_pendientes()
    assert e.estado() == "pendiente de verificación"
    e.sia.falla = False
    # El procesador sigue sondeando cada 15 s; la espera máxima entre intentos es 300 s.
    for _ in range(300 // 15 + 1):
        e.avanzar(15)
        e.procesador.procesar_pendientes()
    assert e.estado() == "verificada"


def test_sia_lento_cuenta_como_no_responde():
    e = Entorno(demora_segundos=5)
    e.postularse.ejecutar(entrada())
    e.procesador.procesar_pendientes()
    tarea = next(iter(e.repositorio._tareas.values()))
    assert tarea.intentos == 1 and tarea.estado == "pendiente"
    assert e.estado() == "pendiente de verificación"


def test_reintentos_agotados_dejan_tarea_fallida_visible():
    e = Entorno(falla=True)
    e.postularse.ejecutar(entrada())
    for _ in range(MAXIMO_INTENTOS * 25):
        e.procesador.procesar_pendientes()
        e.avanzar(15)
    tarea = next(iter(e.repositorio._tareas.values()))
    assert tarea.estado == FALLIDA and tarea.intentos == MAXIMO_INTENTOS
    assert e.estado() == "pendiente de verificación"
    assert e.repositorio.tareas_fallidas() == [tarea]
    assert "verificacion_fallida" in e.eventos()
    # una tarea fallida ya no se vuelve a procesar
    assert e.procesador.procesar_pendientes() == 0


def test_cuarenta_postulaciones_simultaneas_no_se_pierden():
    e = Entorno(falla=True)
    inicio = time.perf_counter()
    for i in range(40):
        assert e.postularse.ejecutar(entrada(usuario_id=f"u{i}")).aceptada
    assert time.perf_counter() - inicio < 2
    assert len(e.repositorio._postulaciones) == 40
    assert len(e.repositorio._tareas) == 40
