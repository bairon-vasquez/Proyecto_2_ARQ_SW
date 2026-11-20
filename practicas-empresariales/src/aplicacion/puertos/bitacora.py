from typing import Protocol


class Bitacora(Protocol):
    """Puerto: registro de eventos auditables, de solo inserción (ADR-006)."""

    def registrar(self, evento: str, usuario_id: str, detalle: str = "") -> None:
        ...
