from collections.abc import Callable
from datetime import datetime

from aplicacion.dto.postulacion_salida import PostulacionSalida
from aplicacion.puertos.bitacora import Bitacora
from aplicacion.puertos.consulta_academica import ConsultaAcademica
from aplicacion.puertos.repositorio_postulaciones import RepositorioPostulaciones
from dominio.tarea_pendiente import FALLIDA

# ADR-003: tiempo máximo de espera al SIA.
TIMEOUT_SIA_SEGUNDOS = 4.0


class VerificarPostulacion:
    """Procesa una tarea de verificación: consulta al SIA y actualiza el estado.

    Si el SIA falla, reprograma la tarea con espera creciente; tras agotar los
    intentos la tarea queda `fallida` y la postulación sigue pendiente.
    """

    def __init__(
        self,
        repositorio: RepositorioPostulaciones,
        consulta_academica: ConsultaAcademica,
        bitacora: Bitacora,
        ahora: Callable[[], datetime] = datetime.now,
    ) -> None:
        self._repositorio = repositorio
        self._consulta = consulta_academica
        self._bitacora = bitacora
        self._ahora = ahora

    def ejecutar(self, tarea_id: str) -> PostulacionSalida:
        tarea = self._repositorio.obtener_tarea(tarea_id)
        if tarea is None:
            raise LookupError(f"No existe la tarea {tarea_id}")
        postulacion = self._repositorio.obtener_postulacion(tarea.postulacion_id)
        if postulacion is None:
            raise LookupError(f"No existe la postulación {tarea.postulacion_id}")

        try:
            faltantes = self._consulta.consultar_requisitos(
                postulacion, TIMEOUT_SIA_SEGUNDOS
            )
        except (TimeoutError, ConnectionError):
            tarea.reprogramar(self._ahora())
            self._repositorio.guardar_tarea(tarea)
            if tarea.estado == FALLIDA:
                self._bitacora.registrar(
                    "verificacion_fallida",
                    postulacion.estudiante_id,
                    f"Tarea {tarea.id} agotó {tarea.intentos} intentos",
                )
                mensaje = "La verificación falló; el director de programa debe revisarla"
            else:
                mensaje = "El SIA no responde; se reintentará la verificación"
            return PostulacionSalida(
                False, mensaje, postulacion.id, postulacion.estado.value
            )

        if faltantes:
            postulacion.marcar_no_cumple_requisitos(faltantes)
            mensaje = "No cumple requisitos. Falta: " + ", ".join(faltantes)
        else:
            postulacion.marcar_verificada()
            mensaje = "Postulación verificada"
        tarea.completar()
        self._repositorio.guardar_postulacion(postulacion)
        self._repositorio.guardar_tarea(tarea)
        self._bitacora.registrar(
            "postulacion_" + postulacion.estado.name.lower(),
            postulacion.estudiante_id,
            f"Postulación {postulacion.id}",
        )
        return PostulacionSalida(
            not faltantes, mensaje, postulacion.id, postulacion.estado.value
        )
