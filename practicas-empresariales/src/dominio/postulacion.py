from dataclasses import dataclass, field
from datetime import datetime

from dominio.estado_postulacion import EstadoPostulacion


@dataclass
class Postulacion:
    """Solicitud del estudiante a realizar la práctica empresarial.

    Nace en estado `PENDIENTE_DE_VERIFICACION` y solo puede cambiar de estado
    mediante las transiciones definidas en este archivo.

    Transiciones válidas (spec 001-postularse):
        PENDIENTE_DE_VERIFICACION -> VERIFICADA
        PENDIENTE_DE_VERIFICACION -> NO_CUMPLE_REQUISITOS

    Las transiciones hacia APROBADA y RECHAZADA pertenecen a CU-02 y no se
    definen aquí.
    """

    id: str
    estudiante_id: str
    programa_id: str
    empresa: str
    supervisor: str
    autorizo_datos: bool
    version_reglas: str
    fecha: datetime = field(default_factory=datetime.now)
    estado: EstadoPostulacion = EstadoPostulacion.PENDIENTE_DE_VERIFICACION
    requisitos_faltantes: list[str] = field(default_factory=list)

    def marcar_verificada(self) -> None:
        """El SIA confirmó que el estudiante cumple los requisitos."""
        self._transicionar(EstadoPostulacion.VERIFICADA)

    def marcar_no_cumple_requisitos(self, faltantes: list[str] | None = None) -> None:
        """El SIA indicó que al estudiante le faltan requisitos; se guardan."""
        self._transicionar(EstadoPostulacion.NO_CUMPLE_REQUISITOS)
        self.requisitos_faltantes = list(faltantes or [])

    def esta_activa(self) -> bool:
        """Activa = pendiente de verificación o verificada (spec: unicidad)."""
        return self.estado in (
            EstadoPostulacion.PENDIENTE_DE_VERIFICACION,
            EstadoPostulacion.VERIFICADA,
        )

    def _transicionar(self, nuevo_estado: EstadoPostulacion) -> None:
        if self.estado is not EstadoPostulacion.PENDIENTE_DE_VERIFICACION:
            raise ValueError(
                f"Transición no válida: {self.estado.value} -> {nuevo_estado.value}"
            )
        self.estado = nuevo_estado
