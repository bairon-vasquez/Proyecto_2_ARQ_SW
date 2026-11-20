# Documento de arquitectura: Sistema de Gestión de Prácticas Empresariales
> Versión 0.4 | Estado: en construcción | Mapa que enlaza, no copia

## 1. Introducción y objetivos
La Facultad de Ingenierías gestiona hoy 500 prácticas al año con Excel y correo. El sistema da una fuente única de información para postulación, asignación de asesor, horas, evaluación de la empresa y acta final. Siete objetivos de negocio medibles (p. ej. acta en ≤3 días hábiles, [OB-01](vision.md#ob-01)).
Detalle: [Visión](vision.md) (objetivos, alcance y stakeholders).

## 2. Restricciones
Cuatro técnicas ([RT-01](drivers.md#rt-01) a [RT-04](drivers.md#rt-04)) y cinco de negocio ([RN-01](drivers.md#rn-01) a [RN-05](drivers.md#rn-05)), cada una con origen e impacto.
Detalle: [Restricciones](drivers.md#3-restricciones).

## 3. Contexto del sistema
Cinco tipos de persona y tres sistemas externos: SIA, proveedor de identidad y correo institucional.
Detalle: [Contexto](contexto.md).

## 4. Estrategia de solución

| Driver | Enfoque | ADR |
|---|---|---|
| [EAC-01](drivers.md#eac-01) (modificar reglas), [PA-01](drivers.md#pa-01) | Monolito modular con puertos y adaptadores; reglas como datos versionados | [001](adr/ADR-001-monolito-modular.md), [007](adr/ADR-007-reglas-versionadas.md) |
| [EAC-02](drivers.md#eac-02), [CU-01](drivers.md#cu-01), [PA-04](drivers.md#pa-04) | Tabla de tareas pendientes (outbox) y procesador con reintentos | [003](adr/ADR-003-integraciones-outbox.md) |
| [EAC-03](drivers.md#eac-03), [RN-04](drivers.md#rn-04), [RT-02](drivers.md#rt-02), [PA-02](drivers.md#pa-02) | SSO institucional para internos y enlace de un solo uso para supervisores | [004](adr/ADR-004-autenticacion-dual.md), [005](adr/ADR-005-autorizacion-por-roles.md) |
| [EAC-04](drivers.md#eac-04), [CU-09](drivers.md#cu-09), [CU-10](drivers.md#cu-10), [RN-02](drivers.md#rn-02), [RN-03](drivers.md#rn-03) | Acta desde plantilla externa, generación síncrona y PDF inmutable con hash | [008](adr/ADR-008-acta-plantilla-inmutable.md) |
| [PA-03](drivers.md#pa-03), [OB-06](vision.md#ob-06) | Bitácora de solo inserción en PostgreSQL | [006](adr/ADR-006-bitacora-auditoria.md) |
| [RT-01](drivers.md#rt-01), [RT-04](drivers.md#rt-04), [RN-05](drivers.md#rn-05) | Plataforma institucional, software libre | [002](adr/ADR-002-plataforma-institucional.md) |
| [CU-15](drivers.md#cu-15) | Migración con plantilla normalizada y *dry-run* | [009](adr/ADR-009-migracion-inicial.md) |
| [PA-05](drivers.md#pa-05) | Variables de entorno, tres entornos y migraciones de BD | [010](adr/ADR-010-configuracion-y-entornos.md) |

## 5. Vistas (4+1)
[Lógica](vistas/01-logica.md) | [Procesos](vistas/02-procesos.md) | [Desarrollo](vistas/03-desarrollo.md) | [Física](vistas/04-fisica.md)
Escenarios (+1): [diagramas/secuencias/](diagramas/secuencias/), tabla en [drivers.md](drivers.md#6-escenarios-1-de-41) y [matriz de cobertura](vistas/matriz-cobertura.md).

## 6. Conceptos transversales

| Concepto | Cómo se resuelve | Dónde se ve |
|---|---|---|
| Autenticación y autorización | SSO + enlace de un solo uso; roles y pertenencia en los casos de uso; negación por defecto | [ADR-004](adr/ADR-004-autenticacion-dual.md), [ADR-005](adr/ADR-005-autorizacion-por-roles.md); vista de desarrollo |
| Trazabilidad | Bitácora de solo inserción, escrita en la misma transacción | [ADR-006](adr/ADR-006-bitacora-auditoria.md); vista lógica |
| Manejo de fallas de integración | Estado "pendiente", reintentos con espera creciente y alerta | [ADR-003](adr/ADR-003-integraciones-outbox.md); [ESC-01](drivers.md#esc-01) |
| Configuración y entornos | Variables de entorno; tres entornos; migraciones de BD | [ADR-010](adr/ADR-010-configuracion-y-entornos.md); vista física |
| Migración inicial | Plantilla normalizada y comando con *dry-run* | [ADR-009](adr/ADR-009-migracion-inicial.md); [ESC-06](drivers.md#esc-06) |
| Datos personales | Autorización de tratamiento, cifrado en tránsito, acceso por rol | [ADR-005](adr/ADR-005-autorizacion-por-roles.md) |

## 7. Decisiones de diseño

| ADR | Decisión | Estado | Drivers |
|---|---|---|---|
| [ADR-001](adr/ADR-001-monolito-modular.md) | Monolito modular con puertos y adaptadores | Aceptado | [EAC-01](drivers.md#eac-01), [PA-01](drivers.md#pa-01) |
| [ADR-002](adr/ADR-002-plataforma-institucional.md) | Plataforma e infraestructura institucional | Aceptado (impuesta) | [RT-01](drivers.md#rt-01), [RT-04](drivers.md#rt-04), [RN-05](drivers.md#rn-05) |
| [ADR-003](adr/ADR-003-integraciones-outbox.md) | Integraciones con outbox y reintentos | Aceptado | [CU-01](drivers.md#cu-01), [EAC-02](drivers.md#eac-02), [RT-03](drivers.md#rt-03), [PA-04](drivers.md#pa-04) |
| [ADR-004](adr/ADR-004-autenticacion-dual.md) | SSO y enlaces de un solo uso | Aceptado | [CU-07](drivers.md#cu-07), [EAC-03](drivers.md#eac-03), [RT-02](drivers.md#rt-02), [RN-04](drivers.md#rn-04), [PA-02](drivers.md#pa-02) |
| [ADR-005](adr/ADR-005-autorizacion-por-roles.md) | Autorización por roles en los casos de uso | Aceptado | [CU-10](drivers.md#cu-10), [RN-01](drivers.md#rn-01), [PA-02](drivers.md#pa-02) |
| [ADR-006](adr/ADR-006-bitacora-auditoria.md) | Bitácora de solo inserción | Aceptado | [EAC-03](drivers.md#eac-03), [RN-02](drivers.md#rn-02), [PA-03](drivers.md#pa-03) |
| [ADR-007](adr/ADR-007-reglas-versionadas.md) | Reglas por programa como datos versionados | Aceptado | [CU-12](drivers.md#cu-12), [EAC-01](drivers.md#eac-01) |
| [ADR-008](adr/ADR-008-acta-plantilla-inmutable.md) | Acta con plantilla externa e inmutable | Aceptado | [CU-09](drivers.md#cu-09), [CU-10](drivers.md#cu-10), [EAC-04](drivers.md#eac-04), [RN-02](drivers.md#rn-02), [RN-03](drivers.md#rn-03) |
| [ADR-009](adr/ADR-009-migracion-inicial.md) | Migración inicial con *dry-run* | Aceptado | [CU-15](drivers.md#cu-15) |
| [ADR-010](adr/ADR-010-configuracion-y-entornos.md) | Configuración y entornos | Aceptado | [PA-05](drivers.md#pa-05) |

## 8. Requisitos de calidad

| EAC | Atributo | Prioridad | ADR | Se verifica en |
|---|---|---|---|---|
| [EAC-01](drivers.md#eac-01-mantenibilidad-modificabilidad) | Mantenibilidad | Alta | 001, 007 | [specs/012-configurar-reglas](../specs/012-configurar-reglas/spec.md), escenario "Programa nuevo sin tocar el código" |
| [EAC-02](drivers.md#eac-02-fiabilidad-tolerancia-a-fallos) | Fiabilidad | Alta | 003 | [specs/001-postularse](../specs/001-postularse/spec.md), escenario "SIA no responde" |
| [EAC-03](drivers.md#eac-03-seguridad-confidencialidad-y-responsabilidad) | Seguridad | Alta | 004, 006 | [specs/007-evaluar-practicante](../specs/007-evaluar-practicante/spec.md), esquema "Rechazo de enlaces no válidos" |
| [EAC-04](drivers.md#eac-04-eficiencia-de-desempeño-comportamiento-temporal) | Eficiencia de desempeño | Media | 008 | [specs/009-generar-acta](../specs/009-generar-acta/spec.md), escenario "Generación en el cierre de periodo" |

Un EAC sin spec que lo verifique queda en evidencia: hoy los cuatro EAC tienen escenario Gherkin.

## 9. Riesgos y deuda técnica

| ID | Riesgo o deuda | Origen | Impacto | Respuesta |
|---|---|---|---|---|
| RA-01 | El sondeo de tareas no escala si la carga supera [S-03](vision.md#s-03) | [ADR-003](adr/ADR-003-integraciones-outbox.md) | Retrasos en verificaciones y correos | Alerta con más de 100 tareas pendientes; ADR nuevo hacia un bróker |
| RA-02 | Se exige firma digital certificada del acta | [R-03](vision.md#r-03), [ADR-008](adr/ADR-008-acta-plantilla-inmutable.md) | Rediseño de la aprobación | Aprobación detrás de un puerto; adaptador nuevo |
| RA-03 | El catálogo institucional no incluye lo supuesto ([S-09](vision.md#s-09)) | [ADR-002](adr/ADR-002-plataforma-institucional.md) | Cambia el stack | Validar en la primera semana; ADR nuevo |
| RA-04 | Pico de cierre supera 10 s en generar actas | [EAC-04](drivers.md#eac-04), [ADR-008](adr/ADR-008-acta-plantilla-inmutable.md) | Mala experiencia en cierre | Medir; pasar a segundo plano con ADR nuevo |
| DT-01 | Las tareas fallidas dependen de revisión humana del director | [ADR-003](adr/ADR-003-integraciones-outbox.md) | Postulaciones sin verificar | Se acepta; automatizar el reproceso si crece |
| DT-02 | Coexisten varias versiones de reglas activas | [ADR-007](adr/ADR-007-reglas-versionadas.md) | Soporte y reportes más complejos | Se acepta; documentar versiones en la interfaz |
| DT-03 | Sin pruebas de arquitectura automáticas todavía | [ADR-001](adr/ADR-001-monolito-modular.md) | Ciclos entre módulos no detectados | Agregar verificación de dependencias en el PR |

## 10. Glosario

| Término | Definición | Nombre en el código |
|---|---|---|
| Estudiante | Quien realiza la práctica | `Estudiante` |
| Postulación | Solicitud del estudiante a realizar la práctica | `Postulacion` |
| Estado de la postulación | Pendiente de verificación, verificada, no cumple requisitos, aprobada o rechazada | `EstadoPostulacion` |
| Práctica | Práctica en curso, nace de una postulación aprobada | `Practica` |
| Docente asesor | Docente que acompaña al practicante | `DocenteAsesor` |
| Director de programa | Coordina la práctica de su programa | `DirectorPrograma` |
| Supervisor de empresa | Persona que supervisa en la empresa; sin cuenta | `SupervisorEmpresa` |
| Horas | Horas semanales que registra el estudiante | `RegistroHoras` |
| Evaluación | Valoración de la empresa al practicante | `Evaluacion` |
| Acta | Acta final de la práctica | `Acta` |
| Versión de reglas | Reglas de un programa con vigencia | `VersionReglas` |
| Enlace de acceso | Acceso de un solo uso para el supervisor | `EnlaceAcceso` |
| Tarea pendiente | Trabajo en segundo plano con reintentos | `TareaPendiente` |
| Bitácora | Registro de eventos auditables | `RegistroBitacora` |
| Consulta académica | Verificación de requisitos contra el SIA | `ConsultaAcademica` (puerto) |
