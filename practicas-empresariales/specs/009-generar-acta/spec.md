# language: es
# Traza: [CU-09](../../docs/drivers.md#cu-09), [EAC-04](../../docs/drivers.md#eac-04), [OB-01](../../docs/vision.md#ob-01), [OB-04](../../docs/vision.md#ob-04), [RN-03](../../docs/drivers.md#rn-03), [ADR-008](../../docs/adr/ADR-008-acta-plantilla-inmutable.md), [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md), [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md), [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md)
Característica: Generar el acta final de la práctica

  Como docente asesor autenticado
  quiero generar el acta final de mi practicante con los datos ya registrados
  para obtenerla en el formato oficial sin transcribir información.

  Antecedentes:
    Dado un docente asesor autenticado
    Y una práctica asignada a ese docente asesor, regida por una versión de reglas

  Escenario: Acta generada correctamente (flujo básico)
    Dado que las horas validadas alcanzan el mínimo de la versión de reglas de la práctica
    Y que la evaluación de la empresa ya fue recibida
    Cuando el docente asesor solicita generar el acta
    Entonces el sistema genera el acta en el formato de la plantilla vigente con los datos registrados
    Y el acta queda en estado "borrador" con su huella
    Y el evento queda registrado en la bitácora

  Escenario: Horas validadas insuficientes
    Dado que las horas validadas no alcanzan el mínimo de la versión de reglas de la práctica
    Cuando el docente asesor solicita generar el acta
    Entonces no se genera el acta
    Y se le indica cuántas horas validadas faltan

  Escenario: Falta la evaluación de la empresa
    Dado que la empresa aún no ha registrado su evaluación
    Cuando el docente asesor solicita generar el acta
    Entonces no se genera el acta
    Y se le indica que falta la evaluación de la empresa

  Escenario: El docente no es el asesor de la práctica
    Dado una práctica asignada a otro docente asesor
    Cuando el docente solicita generar el acta
    Entonces el acceso se deniega
    Y el intento queda registrado en la bitácora

  Escenario: La práctica ya tiene un acta aprobada
    Dado que la práctica ya tiene un acta aprobada
    Cuando el docente asesor solicita generar el acta
    Entonces el sistema no modifica el acta aprobada
    Y genera una nueva acta en borrador que referencia a la anterior

  Escenario: Se usa la plantilla vigente sin afectar actas anteriores
    Dado que el Consejo de Facultad publicó una nueva versión de la plantilla
    Cuando el docente asesor genera el acta de una práctica
    Entonces el acta usa la nueva versión de la plantilla
    Pero las actas ya aprobadas conservan la versión con la que se generaron

  Escenario: Generación en el cierre de periodo ([EAC-04](../../docs/drivers.md#eac-04))
    Dado el cierre de periodo con hasta 30 docentes asesores generando actas a la vez
    Cuando cada uno solicita generar el acta de un practicante
    Entonces el acta se genera en menos de 10 segundos en el 95 % de los casos
    Y no se transcribe manualmente ningún campo
    Y el uso de CPU del servidor de aplicaciones se mantiene por debajo del 70 %
