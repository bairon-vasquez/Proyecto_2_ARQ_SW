# Plan: 015 Migrar las prácticas en curso desde Excel (CU-15)

Traza: [spec.md](spec.md) · [drivers.md](../../docs/drivers.md) · [arquitectura.md](../../docs/arquitectura.md)

## 1. Decisiones (ADR) que aplican

| ADR | Qué impone a esta funcionalidad |
|---|---|
| [ADR-009](../../docs/adr/ADR-009-migracion-inicial.md) | Plantilla normalizada y comando de carga única con modo de simulación; la carga real solo con 0 errores; se archiva tras el lanzamiento |
| [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md) | Cada práctica migrada se asocia a la versión de reglas vigente de su programa |
| [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md) | Cada práctica creada queda en la bitácora |
| [ADR-001](../../docs/adr/ADR-001-monolito-modular.md) | El comando es un adaptador de entrada que invoca los casos de uso; no accede a la base de datos por su cuenta |
| [ADR-002](../../docs/adr/ADR-002-plataforma-institucional.md) | Python; el lector de Excel real queda fuera de esta etapa |

## 2. Componentes por capa (de la [vista de procesos](../../docs/vistas/02-procesos.md) y de desarrollo)

| Capa | Componente | Responsabilidad |
|---|---|---|
| dominio | `FilaMigracion` | Fila ya leída de la plantilla, con sus campos |
| dominio | `ErrorMigracion` | Fila, docente asesor y causa |
| aplicacion/puertos | `LectorPlantilla`, `RepositorioPracticas` (spec 009, ampliado con escritura), `RepositorioVersionesReglas` (spec 012), `Bitacora` (spec 001) | Contratos hacia el exterior |
| aplicacion | `ValidarPlantillaMigracion`, `CargarPracticasMigracion` | Casos de uso: simulación y carga real |
| aplicacion/dto | `ReporteMigracion` | Errores, migradas, omitidas y pendientes por docente |
| infraestructura | `LectorPlantillaEnMemoria`, `ComandoMigracion` | Lector simulado y entrada por línea de comandos (`--simulacion` / `--cargar`) |

## 3. Flujo

Ver [ESC-06](../../docs/diagramas/secuencias/cu15-migrar-practicas.puml): simulación, corrección de errores por los docentes, carga real y reporte final.

## 4. Datos que se guardan

Solo en la carga real: `Practica` con la versión de reglas vigente y `RegistroBitacora`. La simulación no escribe nada.

## 5. Fuera de alcance

- Lector real de archivos `.xlsx` (se simula con filas en memoria).
- Diseño de la plantilla de Excel para los docentes.
- Migración de históricos de años anteriores (fuera del alcance de la visión).

## 6. Decisiones pendientes

Ninguna.
