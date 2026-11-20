from datetime import datetime


class BitacoraEnMemoria:
    """Adaptador en memoria de Bitacora: solo permite insertar y consultar."""

    def __init__(self) -> None:
        self._eventos: list[tuple[datetime, str, str, str]] = []

    def registrar(self, evento: str, usuario_id: str, detalle: str = "") -> None:
        self._eventos.append((datetime.now(), evento, usuario_id, detalle))

    @property
    def eventos(self) -> tuple[tuple[datetime, str, str, str], ...]:
        """Copia de solo lectura: (fecha, evento, usuario_id, detalle)."""
        return tuple(self._eventos)
