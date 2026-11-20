# language: es
# Traza: [CU-01](../../docs/drivers.md#cu-01), [EAC-02](../../docs/drivers.md#eac-02), [RT-02](../../docs/drivers.md#rt-02), [RT-03](../../docs/drivers.md#rt-03), [RN-01](../../docs/drivers.md#rn-01), [PA-04](../../docs/drivers.md#pa-04), [ADR-003](../../docs/adr/ADR-003-integraciones-outbox.md), [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md), [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md), [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md)
Característica: Postularse a la práctica empresarial

  Como estudiante autenticado con la cuenta institucional
  quiero postularme a la práctica empresarial ante la Facultad
  para que mis requisitos académicos se verifiquen y el director de programa decida sobre mi solicitud.

  Antecedentes:
    Dado un estudiante autenticado con la cuenta institucional
    Y un programa con una versión de reglas de práctica publicada y vigente

  Escenario: Postulación verificada correctamente (flujo básico)
    Dado que el estudiante cumple los requisitos académicos según el SIA
    Y que el estudiante autorizó el tratamiento de sus datos personales
    Cuando envía su postulación con la empresa y el supervisor
    Entonces la postulación queda registrada en estado "pendiente de verificación"
    Y el estudiante recibe la confirmación de recepción
    Y el sistema verifica los requisitos y deja la postulación en estado "verificada"
    Y se registra el evento en la bitácora

  Escenario: El estudiante no cumple los requisitos académicos
    Dado que el SIA indica que al estudiante le faltan requisitos
    Cuando envía su postulación
    Entonces la postulación queda en estado "no cumple requisitos"
    Y se le indica qué requisito falta
    # [NECESITA ACLARACIÓN: ¿cómo se entera el estudiante del requisito faltante, si la verificación es asíncrona? (consulta del estado en la aplicación, correo u otro). Hallazgo H-04 de validacion.md]

  Escenario: El estudiante no autoriza el tratamiento de datos
    Dado que el estudiante no autorizó el tratamiento de sus datos personales
    Cuando envía su postulación
    Entonces la postulación se rechaza antes de guardarse
    Y se le indica que debe autorizar el tratamiento de datos

  Escenario: El estudiante ya tiene una postulación activa
    Dado que el estudiante tiene una postulación "pendiente de verificación" o "verificada"
    Cuando envía una nueva postulación
    Entonces la nueva postulación se rechaza
    Y se le informa el estado de la postulación existente

  Escenario: El programa no tiene reglas de práctica publicadas
    Dado un estudiante de un programa sin versión de reglas publicada
    Cuando envía su postulación
    Entonces la postulación se rechaza
    Y se le indica que contacte al director de programa

  Escenario: El usuario no es un estudiante
    Dado un usuario autenticado con rol de docente asesor
    Cuando intenta postularse
    Entonces el acceso se deniega
    Y el intento queda registrado en la bitácora

  Escenario: El SIA no responde durante la postulación ([EAC-02](../../docs/drivers.md#eac-02))
    Dado que el SIA no responde en 4 segundos o responde con error
    Y que hay hasta 40 estudiantes postulándose a la vez
    Cuando el estudiante envía su postulación
    Entonces la postulación queda guardada en estado "pendiente de verificación"
    Y el estudiante recibe la confirmación de recepción en menos de 2 segundos en el 95 % de los casos
    Y el sistema reintenta la verificación sin intervención humana
    Y la verificación se completa en máximo 20 minutos después de que el SIA se recupera
    Y no se pierde ninguna postulación

  Escenario: El SIA sigue caído y se agotan los reintentos
    Dado que el SIA permanece caído durante 8 intentos de verificación
    Cuando se agota el último intento
    Entonces la tarea de verificación pasa al estado "fallida"
    Y la postulación sigue en "pendiente de verificación"
    Y la tarea fallida queda visible para el director de programa (el envío real del aviso por correo se especifica en [CU-08](../../docs/drivers.md#cu-08))
