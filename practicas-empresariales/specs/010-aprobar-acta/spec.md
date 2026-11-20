# language: es
# Traza: [CU-10](../../docs/drivers.md#cu-10), [RN-02](../../docs/drivers.md#rn-02), [OB-06](../../docs/vision.md#ob-06), [S-06](../../docs/vision.md#s-06), [PA-03](../../docs/drivers.md#pa-03), [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md), [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md), [ADR-008](../../docs/adr/ADR-008-acta-plantilla-inmutable.md)
Característica: Aprobar el acta electrónicamente

  Como docente asesor y director de programa
  quiero aprobar el acta final con mi usuario institucional
  para que quede una aprobación trazable que reemplace la firma manual.

  Antecedentes:
    Dado un acta en estado "borrador" de una práctica
    Y que el docente asesor de la práctica y el director del programa están autenticados

  Escenario: Aprobación del docente asesor (flujo básico, primera firma)
    Cuando el docente asesor aprueba el acta
    Entonces el acta pasa al estado "aprobada por asesor"
    Y la aprobación queda en la bitácora con quién, cuándo y qué versión

  Escenario: Aprobación del director de programa (segunda firma)
    Dado que el acta está "aprobada por asesor"
    Cuando el director de programa aprueba el acta
    Entonces el acta pasa al estado "aprobada"
    Y el PDF se guarda en el almacenamiento de documentos con su huella
    Y la aprobación queda en la bitácora
    Y se crea una tarea pendiente para notificar al estudiante

  Escenario: El director intenta aprobar antes que el asesor
    Dado que el acta sigue en estado "borrador"
    Cuando el director de programa intenta aprobarla
    Entonces la aprobación se rechaza
    Y se le indica que falta la aprobación del docente asesor

  Escenario: Usuario sin el rol requerido
    Dado un usuario con rol de estudiante
    Cuando intenta aprobar el acta
    Entonces el acceso se deniega
    Y el intento queda registrado en la bitácora

  Escenario: Docente que no es el asesor de la práctica
    Dado un docente asesor de otra práctica
    Cuando intenta aprobar el acta
    Entonces el acceso se deniega
    Y el intento queda registrado en la bitácora

  Escenario: El director devuelve el acta con observaciones
    Dado que el acta está "aprobada por asesor"
    Cuando el director de programa la devuelve con observaciones
    Entonces el acta pasa al estado "devuelta"
    Y las observaciones y el evento quedan en la bitácora

  Escenario: Un acta aprobada no se puede modificar ni borrar
    Dado que el acta está en estado "aprobada"
    Cuando cualquier usuario intenta modificarla o borrarla
    Entonces la operación se rechaza el 100 % de las veces
    Y la huella del PDF almacenado no cambia
    Y el intento queda registrado en la bitácora
