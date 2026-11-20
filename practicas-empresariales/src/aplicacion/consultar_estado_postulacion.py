from aplicacion.dto.postulacion_salida import PostulacionSalida
from aplicacion.puertos.bitacora import Bitacora
from aplicacion.puertos.repositorio_postulaciones import RepositorioPostulaciones
from dominio.estado_postulacion import EstadoPostulacion

# ADR-005: rol declarado para este caso de uso; todo otro rol se deniega.
ROL_PERMITIDO = "estudiante"


class ConsultarEstadoPostulacion:
    """El estudiante consulta el estado de su última postulación (CU-01, H-04).

    Solo ve sus propios datos: la búsqueda se hace por el usuario autenticado.
    """

    def __init__(
        self, repositorio: RepositorioPostulaciones, bitacora: Bitacora
    ) -> None:
        self._repositorio = repositorio
        self._bitacora = bitacora

    def ejecutar(self, usuario_id: str, rol: str) -> PostulacionSalida:
        if rol != ROL_PERMITIDO:
            self._bitacora.registrar(
                "acceso_denegado",
                usuario_id,
                f"Rol '{rol}' intentó consultar el estado de una postulación",
            )
            raise PermissionError("Solo un estudiante puede consultar su postulación")

        postulacion = self._repositorio.buscar_ultima_postulacion(usuario_id)
        if postulacion is None:
            return PostulacionSalida(False, "Aún no tiene postulaciones")

        mensaje = f"Su postulación está en estado '{postulacion.estado.value}'"
        if postulacion.estado is EstadoPostulacion.NO_CUMPLE_REQUISITOS:
            mensaje += ". Le falta: " + ", ".join(postulacion.requisitos_faltantes)
        return PostulacionSalida(
            True, mensaje, postulacion.id, postulacion.estado.value
        )
