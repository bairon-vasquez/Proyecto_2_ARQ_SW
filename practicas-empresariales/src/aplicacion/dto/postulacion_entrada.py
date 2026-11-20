from dataclasses import dataclass


@dataclass(frozen=True)
class PostulacionEntrada:
    """Entrada de `PostularseAPractica`.

    `version_reglas_vigente` es la versión de reglas publicada y vigente del
    programa del estudiante (ADR-007), o `None` si el programa no tiene una.
    Quien invoca el caso de uso la resuelve: el plan no define un puerto de
    reglas para CU-01.
    """

    usuario_id: str
    rol: str
    programa_id: str
    empresa: str
    supervisor: str
    autorizo_datos: bool
    version_reglas_vigente: str | None
