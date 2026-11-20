# language: es
# Traza: [CU-07](../../docs/drivers.md#cu-07), [EAC-03](../../docs/drivers.md#eac-03), [OB-02](../../docs/vision.md#ob-02), [R-01](../../docs/vision.md#r-01), [RN-04](../../docs/drivers.md#rn-04), [RN-01](../../docs/drivers.md#rn-01), [ADR-004](../../docs/adr/ADR-004-autenticacion-dual.md), [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md), [ADR-003](../../docs/adr/ADR-003-integraciones-outbox.md)
Característica: Evaluar el desempeño del practicante por enlace

  Como supervisor de empresa sin cuenta institucional
  quiero evaluar al practicante desde un enlace que recibí por correo
  para que la Facultad reciba la evaluación a tiempo y pueda generar el acta.

  Antecedentes:
    Dado un practicante con una práctica en curso
    Y un enlace de evaluación emitido por el sistema para su supervisor

  Escenario: Evaluación registrada con un enlace válido (flujo básico)
    Dado que el enlace no se ha usado y tiene menos de 15 días de emitido
    Cuando el supervisor abre el enlace
    Entonces el sistema le muestra el formulario de evaluación del practicante
    Cuando el supervisor envía la evaluación con todos los campos obligatorios
    Entonces la evaluación queda registrada para la práctica
    Y el enlace queda marcado como usado
    Y el evento queda registrado en la bitácora

  Escenario: Evaluación con datos incompletos o fuera de rango
    Dado que el enlace es válido
    Cuando el supervisor envía la evaluación con un campo obligatorio vacío o una calificación fuera del rango permitido
    Entonces la evaluación no se guarda
    Y se le indica qué campos corregir
    Pero el enlace sigue vigente y sin usar

  Escenario: Enlace ya usado
    Dado que el enlace ya se usó para registrar una evaluación
    Cuando alguien intenta abrirlo
    Entonces el acceso se rechaza con una respuesta genérica
    Y no se muestra ningún dato del practicante

  Escenario: Enlace vencido
    Dado que el enlace tiene más de 15 días de emitido
    Cuando alguien intenta abrirlo
    Entonces el acceso se rechaza con una respuesta genérica
    Y no se muestra ningún dato del practicante

  Escenario: Enlace con el identificador alterado
    Dado un identificador que no corresponde a ningún enlace emitido
    Cuando alguien intenta abrirlo
    Entonces el acceso se rechaza con la misma respuesta genérica que en los demás casos
    Y no se revela si el enlace existe

  Esquema del escenario: Rechazo de enlaces no válidos ([EAC-03](../../docs/drivers.md#eac-03))
    Dado un enlace <tipo_enlace>
    Cuando una persona distinta del supervisor intenta abrirlo
    Entonces el acceso se rechaza el 100 % de las veces
    Y no se muestra ningún dato personal
    Y el intento queda en la bitácora con fecha, hora y dirección de origen en menos de 1 minuto
    Y el docente asesor recibe el aviso en menos de 10 minutos

    Ejemplos:
      | tipo_enlace              |
      | ya usado                 |
      | con más de 15 días       |
      | con el identificador alterado |
