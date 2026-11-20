from enum import Enum


class EstadoPostulacion(Enum):
    """Estados posibles de una postulación a la práctica empresarial.

    Solo define los valores. Las transiciones válidas entre estados
    pertenecen a la entidad `Postulacion` (T-02).
    """

    PENDIENTE_DE_VERIFICACION = "pendiente de verificación"
    VERIFICADA = "verificada"
    NO_CUMPLE_REQUISITOS = "no cumple requisitos"
    APROBADA = "aprobada"
    RECHAZADA = "rechazada"
