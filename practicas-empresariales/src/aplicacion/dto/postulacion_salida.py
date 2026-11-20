from dataclasses import dataclass


@dataclass(frozen=True)
class PostulacionSalida:
    """Salida de `PostularseAPractica` y `VerificarPostulacion`.

    `aceptada` es False cuando la solicitud se rechaza por una regla de
    negocio; `mensaje` explica el motivo o el resultado al usuario.
    `postulacion_id` y `estado` identifican la postulación afectada o, si se
    rechazó por duplicada, la ya existente.
    """

    aceptada: bool
    mensaje: str
    postulacion_id: str | None = None
    estado: str | None = None
