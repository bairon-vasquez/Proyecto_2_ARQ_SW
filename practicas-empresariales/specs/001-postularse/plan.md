# Plan: 001 Postularse a la práctica empresarial (CU-01)

Traza: [spec.md](spec.md) · [drivers.md](../../docs/drivers.md) · [arquitectura.md](../../docs/arquitectura.md)

## 1. Decisiones (ADR) que aplican

| ADR | Qué impone a esta funcionalidad |
|---|---|
| [ADR-001](../../docs/adr/ADR-001-monolito-modular.md) | Módulo **Postulaciones** con puertos; dominio sin dependencias externas |
| [ADR-003](../../docs/adr/ADR-003-integraciones-outbox.md) | La verificación con el SIA no se hace en la petición: se guarda postulación + tarea pendiente y se procesa en segundo plano con reintentos |
| [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md) | Solo el rol estudiante puede postularse; negación por defecto |
| [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md) | Cada cambio de estado y cada intento denegado se registra |
| [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md) | Se asocia la versión de reglas vigente del programa a la postulación |
| [ADR-002](../../docs/adr/ADR-002-plataforma-institucional.md) | Python; en esta etapa **adaptadores en memoria**, sin PostgreSQL real |

## 2. Componentes por capa (de la [vista de desarrollo](../../docs/vistas/03-desarrollo.md))

| Capa | Componente | Responsabilidad |
|---|---|---|
| dominio | `Postulacion`, `EstadoPostulacion` | Entidad y sus estados válidos y transiciones |
| aplicacion | `PostularseAPractica` (caso de uso) | Valida rol, autorización de datos, unicidad y reglas; guarda postulación y tarea |
| aplicacion | `VerificarPostulacion` (caso de uso) | Procesa una tarea: consulta al SIA, actualiza estado, reprograma o marca fallida |
| aplicacion | `PostulacionEntrada`, `PostulacionSalida` (DTO) | Entrada y salida de los casos de uso |
| aplicacion/puertos | `ConsultaAcademica`, `RepositorioPostulaciones`, `Bitacora` | Contratos que declara la aplicación |
| dominio | `TareaPendiente` | Tarea con intentos y próximo intento ([ADR-003](../../docs/adr/ADR-003-integraciones-outbox.md)) |
| infraestructura | `ConsultaAcademicaEnMemoria`, `RepositorioPostulacionesEnMemoria`, `BitacoraEnMemoria` | Adaptadores simulados |
| infraestructura | `ProcesadorDeTareas` | Procesador de tareas de la vista de desarrollo y de ESC-01: sondea cada 15 s las tareas listas e invoca `VerificarPostulacion` (agregado tras el hallazgo H-01 de `validacion.md`) |

## 3. Flujo

Ver [secuencia de ESC-01](../../docs/diagramas/secuencias/cu01-postularse.puml): API guarda postulación y tarea en una sola operación y responde; el procesador toma la tarea, consulta el SIA con un máximo de 4 s y reintenta con espera creciente (máx. 5 min, 8 intentos).

## 4. Datos que se guardan

`Postulacion`: estudiante, programa, empresa, supervisor, fecha, estado, autorización de datos, versión de reglas. `TareaPendiente`: postulación, tipo, estado, intentos, próximo intento.

## 5. Fuera de alcance

- Controlador REST y aplicación web (no hay tarea de interfaz en esta etapa).
- PostgreSQL real, bitácora persistente y envío de correo real (adaptadores en memoria). El aviso al director cuando la tarea falla (spec, último escenario) queda como estado `fallida` observable; el envío real del correo no se implementa.
- Aprobación o rechazo del director ([CU-02](../../docs/drivers.md#cu-02)) y asignación de asesor ([CU-03](../../docs/drivers.md#cu-03)).
- Verificación de convenio vigente de la empresa.

## 6. Decisiones pendientes

Ninguna. Si surge una (p. ej. el contrato real del SIA, [R-02](../../docs/vision.md#r-02)), se registra primero un ADR.
