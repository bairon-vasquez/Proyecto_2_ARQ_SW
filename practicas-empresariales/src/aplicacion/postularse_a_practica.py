from collections.abc import Callable
from datetime import datetime
from uuid import uuid4

from aplicacion.dto.postulacion_entrada import PostulacionEntrada
from aplicacion.dto.postulacion_salida import PostulacionSalida
from aplicacion.puertos.bitacora import Bitacora
from aplicacion.puertos.repositorio_postulaciones import RepositorioPostulaciones
from dominio.postulacion import Postulacion
from dominio.tarea_pendiente import TareaPendiente

# ADR-005: rol declarado para este caso de uso; todo otro rol se deniega.
ROL_PERMITIDO = "estudiante"


class PostularseAPractica:
    """CU-01: el estudiante envía su postulación.

    No consulta al SIA: guarda la postulación y su tarea pendiente en una sola
    operación y responde de inmediato (ADR-003, EAC-02).
    """

    def __init__(
        self,
        repositorio: RepositorioPostulaciones,
        bitacora: Bitacora,
        ahora: Callable[[], datetime] = datetime.now,
    ) -> None:
        self._repositorio = repositorio
        self._bitacora = bitacora
        self._ahora = ahora

    def ejecutar(self, entrada: PostulacionEntrada) -> PostulacionSalida:
        if entrada.rol != ROL_PERMITIDO:
            self._bitacora.registrar(
                "acceso_denegado",
                entrada.usuario_id,
                f"Rol '{entrada.rol}' intentó postularse",
            )
            raise PermissionError("Solo un estudiante puede postularse")

        if not entrada.autorizo_datos:
            return PostulacionSalida(
                False, "Debe autorizar el tratamiento de sus datos personales"
            )

        if entrada.version_reglas_vigente is None:
            return PostulacionSalida(
                False,
                "Su programa no tiene reglas de práctica publicadas; "
                "contacte al director de programa",
            )

        existente = self._repositorio.buscar_postulacion_activa(entrada.usuario_id)
        if existente is not None:
            return PostulacionSalida(
                False,
                f"Ya tiene una postulación en estado '{existente.estado.value}'",
                existente.id,
                existente.estado.value,
            )

        ahora = self._ahora()
        postulacion = Postulacion(
            id=str(uuid4()),
            estudiante_id=entrada.usuario_id,
            programa_id=entrada.programa_id,
            empresa=entrada.empresa,
            supervisor=entrada.supervisor,
            autorizo_datos=entrada.autorizo_datos,
            version_reglas=entrada.version_reglas_vigente,
            fecha=ahora,
        )
        tarea = TareaPendiente(
            id=str(uuid4()), postulacion_id=postulacion.id, proximo_intento=ahora
        )
        self._repositorio.guardar_con_tarea(postulacion, tarea)
        self._bitacora.registrar(
            "postulacion_recibida", entrada.usuario_id, f"Postulación {postulacion.id}"
        )
        return PostulacionSalida(
            True,
            "Postulación recibida, en verificación",
            postulacion.id,
            postulacion.estado.value,
        )
