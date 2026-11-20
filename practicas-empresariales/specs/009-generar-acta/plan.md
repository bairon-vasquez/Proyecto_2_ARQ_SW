# Plan: 009 Generar el acta final (CU-09)

Traza: [spec.md](spec.md) · [drivers.md](../../docs/drivers.md) · [arquitectura.md](../../docs/arquitectura.md)

## 1. Decisiones (ADR) que aplican

| ADR | Qué impone a esta funcionalidad |
|---|---|
| [ADR-008](../../docs/adr/ADR-008-acta-plantilla-inmutable.md) | Plantilla separada del código; PDF generado **en la misma petición** (sin cola); el acta nace en borrador con huella; un error se corrige con una nueva acta que referencia a la anterior |
| [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md) | Las horas mínimas salen de la `VersionReglas` con la que inició la práctica |
| [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md) | Rol docente asesor y verificación de que la práctica sea de su practicante; negación por defecto |
| [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md) | Se registra la generación y los intentos denegados |
| [ADR-001](../../docs/adr/ADR-001-monolito-modular.md) | Módulo **Actas**; usa Horas, Evaluaciones y Reglas, sin ciclos |
| [ADR-002](../../docs/adr/ADR-002-plataforma-institucional.md) | Python; librería de PDF libre detrás de un puerto; adaptadores simulados en esta etapa |

## 2. Componentes por capa (de la [vista de desarrollo](../../docs/vistas/03-desarrollo.md))

| Capa | Componente | Responsabilidad |
|---|---|---|
| dominio | `Practica`, `RegistroHoras`, `VersionReglas` (mínimos) | Lo necesario para verificar horas y reglas; la spec 012 amplía `VersionReglas` |
| dominio | `Acta`, `EstadoActa`, `PlantillaActa` | Acta con versión, estado y huella; plantilla versionada |
| aplicacion/puertos | `RepositorioPracticas`, `RepositorioActas`, `GeneradorPdf` | Contratos hacia el exterior |
| aplicacion/puertos | `Bitacora` (spec 001) | Registro de eventos |
| aplicacion | `GenerarActa` | Verifica rol, pertenencia, horas y evaluación; genera el borrador |
| aplicacion/dto | `ActaSalida` | Salida del caso de uso |
| infraestructura | `RepositorioPracticasEnMemoria`, `RepositorioActasEnMemoria`, `GeneradorPdfSimulado` | Adaptadores simulados |

## 3. Flujo

Ver [ESC-03](../../docs/diagramas/secuencias/cu09-generar-acta.puml): lee práctica, horas, evaluación y versión de reglas; si faltan requisitos rechaza con el detalle; si no, llena la plantilla, genera el PDF y guarda el borrador con huella.

## 4. Datos que se guardan

`Acta`: práctica, versión, estado, huella, versión de plantilla, referencia a acta anterior. `RegistroBitacora`: evento y actor.

## 5. Fuera de alcance

- Aprobación del acta ([CU-10](../../docs/drivers.md#cu-10), spec 010) y su almacenamiento inmutable.
- Controlador REST y aplicación web; librería de PDF real; medición real de CPU (se mide en el entorno de pruebas del Área de Sistemas).
- Gestión de plantillas por el Consejo (solo se consume la vigente).

## 6. Decisiones pendientes

Ninguna. Si el p95 supera 10 s en el cierre, se registra un ADR nuevo que pase la generación a segundo plano (alternativa D del [ADR-008](../../docs/adr/ADR-008-acta-plantilla-inmutable.md)).
