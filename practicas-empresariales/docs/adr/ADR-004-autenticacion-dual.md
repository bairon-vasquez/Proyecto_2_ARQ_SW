# ADR-004: Autenticación institucional para usuarios internos y enlaces de un solo uso para supervisores

## Estado
Aceptado — 2026-11-17

## Contexto
[RT-02](../drivers.md#rt-02) obliga a autenticar a estudiantes, docentes y personal con la cuenta institucional. [RN-04](../drivers.md#rn-04) prohíbe exigir cuenta o registro con contraseña a los supervisores, porque un trámite pesado pone en riesgo [OB-02](../vision.md#ob-02) ([R-01](../vision.md#r-01)). Los supervisores intervienen en [CU-05](../drivers.md#cu-05) (validar horas) y [CU-07](../drivers.md#cu-07) (evaluar). [EAC-03](../drivers.md#eac-03-seguridad-confidencialidad-y-responsabilidad) exige rechazar el 100 % de los enlaces usados, vencidos (más de 15 días) o alterados, sin mostrar datos. [PA-02](../drivers.md#pa-02) pide decidir cómo conviven los dos mecanismos.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Cuentas locales con contraseña para todos | Un solo mecanismo | Incumple [RT-02](../drivers.md#rt-02) y [RN-04](../drivers.md#rn-04); el sistema guardaría contraseñas |
| B) SSO para todos, con cuentas de invitado para supervisores | Control central de identidades | Incumple [RN-04](../drivers.md#rn-04) (el supervisor se registra); carga al administrador del SIA |
| C) SSO (OIDC) para usuarios internos y enlace de un solo uso para supervisores | Cumple [RT-02](../drivers.md#rt-02) y [RN-04](../drivers.md#rn-04); el supervisor entra con un clic ([OB-02](../vision.md#ob-02)) | Dos mecanismos que mantener y probar |

## Decisión
Se elige **C**. Los usuarios internos entran por el proveedor de identidad mediante OpenID Connect a través de un adaptador ([ADR-001](ADR-001-monolito-modular.md)); el sistema no guarda contraseñas. Para cada validación de horas o evaluación se genera un enlace con un identificador aleatorio de 256 bits, de un solo uso y válido 15 días; solo se guarda su resumen criptográfico (hash). Todo intento con un enlace usado, vencido o alterado se rechaza con la misma respuesta genérica, se registra en la bitácora ([ADR-006](ADR-006-bitacora-auditoria.md)) y se avisa al docente asesor.

## Consecuencias
**Positivas.** Se cumplen [RT-02](../drivers.md#rt-02), [RN-04](../drivers.md#rn-04) y [EAC-03](../drivers.md#eac-03); el supervisor no crea cuentas ([R-01](../vision.md#r-01)); el sistema no custodia contraseñas.

**Negativas (costos aceptados).** Dos mecanismos de acceso; quien tenga el enlace antes de que se use puede actuar en nombre del supervisor; el correo es un punto débil.

**Riesgos.** Que el enlace se reenvíe a otra persona. Mitigación: sirve una vez y para una sola práctica, y el docente asesor revisa la evaluación antes de solicitar el acta ([CU-06](../drivers.md#cu-06)).

## Vistas que modifica
[Contexto](../contexto.md), [Procesos](../vistas/02-procesos.md), [Desarrollo](../vistas/03-desarrollo.md)
