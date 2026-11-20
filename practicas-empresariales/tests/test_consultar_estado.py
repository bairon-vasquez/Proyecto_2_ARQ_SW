"""Pruebas de los escenarios de consulta de estado de specs/001-postularse/spec.md."""
import sys
from datetime import datetime
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from aplicacion.consultar_estado_postulacion import ConsultarEstadoPostulacion  # noqa: E402
from aplicacion.dto.postulacion_entrada import PostulacionEntrada  # noqa: E402
from aplicacion.postularse_a_practica import PostularseAPractica  # noqa: E402
from aplicacion.verificar_postulacion import VerificarPostulacion  # noqa: E402
from infraestructura.bitacora_en_memoria import BitacoraEnMemoria  # noqa: E402
from infraestructura.consulta_academica_en_memoria import (  # noqa: E402
    ConsultaAcademicaEnMemoria,
)
from infraestructura.procesador_de_tareas import ProcesadorDeTareas  # noqa: E402
from infraestructura.repositorio_postulaciones_en_memoria import (  # noqa: E402
    RepositorioPostulacionesEnMemoria,
)


def armar(**sia):
    repositorio = RepositorioPostulacionesEnMemoria()
    bitacora = BitacoraEnMemoria()
    verificar = VerificarPostulacion(
        repositorio, ConsultaAcademicaEnMemoria(**sia), bitacora
    )
    return (
        repositorio,
        bitacora,
        PostularseAPractica(repositorio, bitacora),
        ProcesadorDeTareas(repositorio, verificar),
        ConsultarEstadoPostulacion(repositorio, bitacora),
    )


def entrada(usuario="u1") -> PostulacionEntrada:
    return PostulacionEntrada(
        usuario, "estudiante", "ingenieria", "Empresa S.A.", "Ana Pérez", True, "v1"
    )


def test_consulta_muestra_estado_actual():
    _, _, postularse, procesador, consultar = armar()
    postularse.ejecutar(entrada())
    assert consultar.ejecutar("u1", "estudiante").estado == "pendiente de verificación"
    procesador.procesar_pendientes()
    salida = consultar.ejecutar("u1", "estudiante")
    assert salida.aceptada
    assert salida.estado == "verificada"


def test_consulta_muestra_requisitos_faltantes_si_no_cumple():
    _, _, postularse, procesador, consultar = armar(
        requisitos_faltantes=["promedio mínimo", "créditos aprobados"]
    )
    postularse.ejecutar(entrada())
    procesador.procesar_pendientes()
    salida = consultar.ejecutar("u1", "estudiante")
    assert salida.estado == "no cumple requisitos"
    assert "promedio mínimo" in salida.mensaje
    assert "créditos aprobados" in salida.mensaje


def test_consulta_solo_devuelve_la_postulacion_propia():
    _, _, postularse, _, consultar = armar()
    postularse.ejecutar(entrada("u1"))
    assert consultar.ejecutar("u2", "estudiante").postulacion_id is None


def test_consulta_sin_haber_postulado():
    _, _, _, _, consultar = armar()
    salida = consultar.ejecutar("u1", "estudiante")
    assert not salida.aceptada
    assert "Aún no tiene postulaciones" in salida.mensaje


def test_consulta_de_no_estudiante_se_deniega_y_se_registra():
    _, bitacora, _, _, consultar = armar()
    with pytest.raises(PermissionError):
        consultar.ejecutar("d1", "docente asesor")
    assert [e[1] for e in bitacora.eventos] == ["acceso_denegado"]


def test_consulta_devuelve_la_ultima_postulacion():
    repositorio, _, postularse, procesador, consultar = armar(
        requisitos_faltantes=["promedio mínimo"]
    )
    postularse.ejecutar(entrada())
    procesador.procesar_pendientes()
    # tras "no cumple" puede postularse de nuevo; la consulta muestra la más reciente
    nueva = postularse.ejecutar(entrada())
    assert nueva.aceptada
    assert datetime.now() >= repositorio.obtener_postulacion(nueva.postulacion_id).fecha
    assert consultar.ejecutar("u1", "estudiante").estado == "pendiente de verificación"
