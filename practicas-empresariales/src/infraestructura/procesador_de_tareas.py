from collections.abc import Callable
from datetime import datetime
from threading import Event

from aplicacion.puertos.repositorio_postulaciones import RepositorioPostulaciones
from aplicacion.verificar_postulacion import VerificarPostulacion

# ADR-003: el procesador sondea las tareas cada 15 segundos.
INTERVALO_SONDEO_SEGUNDOS = 15


class ProcesadorDeTareas:
    """Procesador de tareas en segundo plano (ADR-003, ESC-01).

    Toma las tareas pendientes cuyo próximo intento ya llegó y ejecuta
    `VerificarPostulacion` para cada una. Los reintentos y la espera creciente
    los decide la propia tarea.
    """

    def __init__(
        self,
        repositorio: RepositorioPostulaciones,
        verificar_postulacion: VerificarPostulacion,
        ahora: Callable[[], datetime] = datetime.now,
    ) -> None:
        self._repositorio = repositorio
        self._verificar = verificar_postulacion
        self._ahora = ahora

    def procesar_pendientes(self) -> int:
        """Procesa una pasada y devuelve cuántas tareas atendió."""
        tareas = self._repositorio.tareas_listas(self._ahora())
        for tarea in tareas:
            self._verificar.ejecutar(tarea.id)
        return len(tareas)

    def ejecutar(
        self,
        detener: Event,
        intervalo_segundos: float = INTERVALO_SONDEO_SEGUNDOS,
    ) -> None:
        """Sondea hasta que `detener` se active (para correr en un hilo)."""
        while not detener.is_set():
            self.procesar_pendientes()
            detener.wait(intervalo_segundos)
