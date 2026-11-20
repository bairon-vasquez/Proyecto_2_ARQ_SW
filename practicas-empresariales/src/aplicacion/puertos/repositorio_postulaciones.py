from datetime import datetime
from typing import Protocol

from dominio.postulacion import Postulacion
from dominio.tarea_pendiente import TareaPendiente


class RepositorioPostulaciones(Protocol):
    """Puerto: persistencia de postulaciones y sus tareas pendientes."""

    def guardar_con_tarea(self, postulacion: Postulacion, tarea: TareaPendiente) -> None:
        """Guarda postulación y tarea en una sola operación (ADR-003)."""
        ...

    def guardar_postulacion(self, postulacion: Postulacion) -> None:
        """Guarda los cambios de una postulación existente."""
        ...

    def guardar_tarea(self, tarea: TareaPendiente) -> None:
        """Guarda los cambios de una tarea existente."""
        ...

    def obtener_postulacion(self, postulacion_id: str) -> Postulacion | None:
        ...

    def obtener_tarea(self, tarea_id: str) -> TareaPendiente | None:
        ...

    def buscar_postulacion_activa(self, estudiante_id: str) -> Postulacion | None:
        """Postulación pendiente de verificación o verificada del estudiante."""
        ...

    def tareas_listas(self, ahora: datetime) -> list[TareaPendiente]:
        """Tareas pendientes cuyo próximo intento ya llegó."""
        ...

    def tareas_fallidas(self) -> list[TareaPendiente]:
        """Tareas en estado fallida, visibles para el director de programa."""
        ...
