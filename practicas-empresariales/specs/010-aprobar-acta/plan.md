# Plan: 010 Aprobar el acta electrónicamente (CU-10)

Traza: [spec.md](spec.md) · [drivers.md](../../docs/drivers.md) · [arquitectura.md](../../docs/arquitectura.md)

## 1. Decisiones (ADR) que aplican

| ADR | Qué impone a esta funcionalidad |
|---|---|
| [ADR-008](../../docs/adr/ADR-008-acta-plantilla-inmutable.md) | Dos aprobaciones (asesor y luego director); el PDF aprobado se guarda con hash SHA-256 y no se modifica ni se borra; la aprobación va detrás de un puerto |
| [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md) | Rol y pertenencia verificados en el caso de uso; negación por defecto |
| [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md) | Cada aprobación, devolución e intento denegado queda en la bitácora (quién, cuándo, versión) |
| [ADR-003](../../docs/adr/ADR-003-integraciones-outbox.md) | El aviso al estudiante es una tarea pendiente, no se envía en la petición |
| [ADR-001](../../docs/adr/ADR-001-monolito-modular.md) | Módulo **Actas**; sin ciclos hacia otros módulos |

## 2. Componentes por capa (de la [vista de desarrollo](../../docs/vistas/03-desarrollo.md))

| Capa | Componente | Responsabilidad |
|---|---|---|
| dominio | `Rol` | Roles del sistema (estudiante, docente asesor, director, supervisor, administrador) |
| dominio | `Acta`, `EstadoActa` (spec 009) | Transiciones: borrador → aprobada por asesor → aprobada, o devuelta |
| dominio | `AprobacionActa` | Quién aprobó, cuándo y qué versión |
| aplicacion | `PoliticaAutorizacion` | Tabla de permisos por caso de uso, negación por defecto |
| aplicacion/puertos | `AlmacenamientoDocumentos`, `RepositorioActas` (spec 009), `RepositorioTareas` (spec 007), `Bitacora` | Contratos hacia el exterior |
| aplicacion | `AprobarActaComoAsesor`, `AprobarActaComoDirector`, `DevolverActa` | Casos de uso |
| aplicacion/dto | `AprobacionEntrada` | Entrada con actor y observaciones |
| infraestructura | `AlmacenamientoDocumentosEnMemoria` | Adaptador simulado, solo escritura única |

## 3. Flujo

Ver [ESC-04](../../docs/diagramas/secuencias/cu10-aprobar-acta.puml): aprobación del asesor, aprobación del director con guardado del PDF y tarea de aviso, o devolución con observaciones.

## 4. Datos que se guardan

`AprobacionActa`: acta, rol, actor, fecha, versión. Documento aprobado: PDF y huella. `TareaPendiente`: aviso al estudiante.

## 5. Fuera de alcance

- Firma digital certificada ([R-03](../../docs/vision.md#r-03)); se mantiene detrás de un puerto para un adaptador futuro.
- Envío real del correo al estudiante.
- Controlador REST, aplicación web y almacenamiento institucional real.

## 6. Decisiones pendientes

Ninguna.
