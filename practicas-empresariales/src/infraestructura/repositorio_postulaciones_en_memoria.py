from datetime import datetime

from dominio.postulacion import Postulacion
from dominio.tarea_pendiente import FALLIDA, TareaPendiente


class RepositorioPostulacionesEnMemoria:
    """Adaptador en memoria de RepositorioPostulaciones (sin PostgreSQL)."""

    def __init__(self) -> None:
        self._postulaciones: dict[str, Postulacion] = {}
        self._tareas: dict[str, TareaPendiente] = {}

    def guardar_con_tarea(self, postulacion: Postulacion, tarea: TareaPendiente) -> None:
        self._postulaciones[postulacion.id] = postulacion
        self._tareas[tarea.id] = tarea

    def guardar_postulacion(self, postulacion: Postulacion) -> None:
        self._postulaciones[postulacion.id] = postulacion

    def guardar_tarea(self, tarea: TareaPendiente) -> None:
        self._tareas[tarea.id] = tarea

    def obtener_postulacion(self, postulacion_id: str) -> Postulacion | None:
        return self._postulaciones.get(postulacion_id)

    def obtener_tarea(self, tarea_id: str) -> TareaPendiente | None:
        return self._tareas.get(tarea_id)

    def buscar_postulacion_activa(self, estudiante_id: str) -> Postulacion | None:
        for postulacion in self._postulaciones.values():
            if postulacion.estudiante_id == estudiante_id and postulacion.esta_activa():
                return postulacion
        return None

    def tareas_listas(self, ahora: datetime) -> list[TareaPendiente]:
        return [t for t in self._tareas.values() if t.esta_lista(ahora)]

    def tareas_fallidas(self) -> list[TareaPendiente]:
        return [t for t in self._tareas.values() if t.estado == FALLIDA]
