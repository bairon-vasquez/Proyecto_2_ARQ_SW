# Vista lógica: modelo de dominio

Para: usuarios finales y analistas. Notación: UML (C4 no tiene diagrama para esta vista).

## 1. Presentación principal

Diagrama: [../diagramas/01-logica.puml](../diagramas/01-logica.puml). Solo conceptos del negocio y atributos clave, sin tipos, métodos ni elementos técnicos.

## 2. Catálogo de elementos

| Entidad | Qué representa | Atributos clave | Regla del negocio |
|---|---|---|---|
| Estudiante | Quien realiza la práctica | documento, programa | Solo ve y gestiona sus propias prácticas |
| Programa | Programa académico de la Facultad | nombre | Tiene una o más versiones de reglas |
| VersionReglas | Reglas de práctica de un programa | horas mínimas, requisitos, vigencia desde, estado | Estados: borrador y publicada. Es un dato, no código ([ADR-007](../adr/ADR-007-reglas-versionadas.md)) |
| Postulacion | Solicitud del estudiante | fecha, estado, autorización de datos | Estados: pendiente de verificación, verificada, no cumple, aprobada, rechazada |
| Practica | Práctica en curso | estado, fecha inicio, fecha fin | Nace de una postulación aprobada y guarda la versión de reglas con la que inició |
| DocenteAsesor | Docente que acompaña la práctica | nombre | Solo ve a sus practicantes |
| Empresa | Organización que recibe al practicante | nombre, convenio vigente | Se consulta si el convenio está vigente; no se gestiona |
| SupervisorEmpresa | Persona que supervisa en la empresa | nombre, correo | No tiene cuenta; actúa por enlace |
| RegistroHoras | Horas semanales | semana, horas, estado | Estados: registrado, validado, observado |
| Evaluacion | Evaluación de la empresa al practicante | calificación, fecha | Una por práctica |
| Acta | Acta final | versión, estado, huella | Estados: borrador, aprobada por asesor, aprobada, devuelta. Aprobada es inmutable ([ADR-008](../adr/ADR-008-acta-plantilla-inmutable.md)) |
| PlantillaActa | Formato oficial del acta | versión | Se versiona; cambia sin reprogramar |
| EnlaceAcceso | Acceso de un solo uso | vence, usado | 15 días de vigencia ([ADR-004](../adr/ADR-004-autenticacion-dual.md)) |
| TareaPendiente | Trabajo a procesar en segundo plano | tipo, estado, intentos | Máximo 8 intentos ([ADR-003](../adr/ADR-003-integraciones-outbox.md)) |
| RegistroBitacora | Evento auditable | fecha, evento, actor | Solo inserción ([ADR-006](../adr/ADR-006-bitacora-auditoria.md)) |

## 3. Justificación

- [CU-01](../drivers.md#cu-01), [CU-07](../drivers.md#cu-07), [CU-09](../drivers.md#cu-09), [CU-10](../drivers.md#cu-10), [CU-12](../drivers.md#cu-12): de ellos salen Postulacion, Evaluacion, Acta y VersionReglas.
- [EAC-02](../drivers.md#eac-02): TareaPendiente deja rastro de cada intento; ninguna postulación se pierde sin explicación.
- [EAC-01](../drivers.md#eac-01): VersionReglas como dato permite agregar un programa sin programar.
- Seguridad y [OB-06](../vision.md#ob-06): toda Practica pertenece a un Estudiante y a un DocenteAsesor; RegistroBitacora sostiene el consolidado.
- ADR: [003](../adr/ADR-003-integraciones-outbox.md), [005](../adr/ADR-005-autorizacion-por-roles.md), [006](../adr/ADR-006-bitacora-auditoria.md), [007](../adr/ADR-007-reglas-versionadas.md), [008](../adr/ADR-008-acta-plantilla-inmutable.md).

## 4. Comportamiento

Los diagramas de secuencia cambian los estados de estas entidades: Postulacion en [ESC-01](../diagramas/secuencias/cu01-postularse.puml), Acta en [ESC-03](../diagramas/secuencias/cu09-generar-acta.puml) y [ESC-04](../diagramas/secuencias/cu10-aprobar-acta.puml).

## 5. Vistas relacionadas

- [Desarrollo](03-desarrollo.md): estas entidades viven en la capa de dominio.
- [Procesos](02-procesos.md): se guardan en PostgreSQL; las actas aprobadas, en el almacenamiento de documentos.
