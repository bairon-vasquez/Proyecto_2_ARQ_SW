from dataclasses import dataclass
from datetime import datetime, timedelta

# Estados de la tarea (ADR-003).
PENDIENTE = "pendiente"
COMPLETADA = "completada"
FALLIDA = "fallida"

# ADR-003: 8 intentos como máximo; espera creciente con tope de 5 minutos.
MAXIMO_INTENTOS = 8
ESPERA_BASE_SEGUNDOS = 15
ESPERA_MAXIMA_SEGUNDOS = 300


@dataclass
class TareaPendiente:
    """Trabajo en segundo plano con reintentos (outbox, ADR-003).

    Se guarda junto con la postulación y la procesa el procesador de tareas.
    """

    id: str
    postulacion_id: str
    proximo_intento: datetime
    tipo: str = "verificar_postulacion"
    estado: str = PENDIENTE
    intentos: int = 0

    def esta_lista(self, ahora: datetime) -> bool:
        """Está pendiente y ya llegó la hora de su próximo intento."""
        return self.estado == PENDIENTE and self.proximo_intento <= ahora

    def completar(self) -> None:
        """La verificación terminó (con resultado de cumple o no cumple)."""
        self._exigir_pendiente()
        self.estado = COMPLETADA

    def reprogramar(self, ahora: datetime) -> None:
        """Registra un intento fallido.

        Programa el siguiente con espera creciente; al llegar al máximo de
        intentos la tarea pasa a `fallida`.
        """
        self._exigir_pendiente()
        self.intentos += 1
        if self.intentos >= MAXIMO_INTENTOS:
            self.estado = FALLIDA
            return
        espera = min(
            ESPERA_BASE_SEGUNDOS * 2 ** (self.intentos - 1),
            ESPERA_MAXIMA_SEGUNDOS,
        )
        self.proximo_intento = ahora + timedelta(seconds=espera)

    def _exigir_pendiente(self) -> None:
        if self.estado != PENDIENTE:
            raise ValueError(f"La tarea está en estado '{self.estado}', no 'pendiente'")
