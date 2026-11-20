from typing import Protocol

from dominio.postulacion import Postulacion


class ConsultaAcademica(Protocol):
    """Puerto: verificación de requisitos académicos contra el SIA."""

    def consultar_requisitos(
        self, postulacion: Postulacion, timeout_segundos: float = 4.0
    ) -> list[str]:
        """Devuelve los requisitos que le faltan al estudiante.

        Una lista vacía significa que cumple todos los requisitos.

        Lanza `TimeoutError` si el SIA no responde dentro de
        `timeout_segundos` y `ConnectionError` si responde con error.
        """
        ...
