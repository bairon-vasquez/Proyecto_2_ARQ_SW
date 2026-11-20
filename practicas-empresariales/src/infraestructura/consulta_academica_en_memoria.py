from dominio.postulacion import Postulacion


class ConsultaAcademicaEnMemoria:
    """Adaptador simulado del SIA (ConsultaAcademica).

    Configurable: `requisitos_faltantes` (lista vacía = cumple),
    `falla` (responde con error) y `demora_segundos` (si supera el timeout
    pedido, simula que el SIA no respondió a tiempo). No espera de verdad.
    """

    def __init__(
        self,
        requisitos_faltantes: list[str] | None = None,
        falla: bool = False,
        demora_segundos: float = 0.0,
    ) -> None:
        self.requisitos_faltantes = requisitos_faltantes or []
        self.falla = falla
        self.demora_segundos = demora_segundos

    def consultar_requisitos(
        self, postulacion: Postulacion, timeout_segundos: float = 4.0
    ) -> list[str]:
        if self.demora_segundos > timeout_segundos:
            raise TimeoutError("El SIA no respondió a tiempo")
        if self.falla:
            raise ConnectionError("El SIA respondió con error")
        return list(self.requisitos_faltantes)
