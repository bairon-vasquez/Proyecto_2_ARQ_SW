# Plan: 012 Configurar las reglas de práctica de un programa (CU-12)

Traza: [spec.md](spec.md) · [drivers.md](../../docs/drivers.md) · [arquitectura.md](../../docs/arquitectura.md)

## 1. Decisiones (ADR) que aplican

| ADR | Qué impone a esta funcionalidad |
|---|---|
| [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md) | Reglas como datos versionados: borrador → validación → publicación con vigencia futura; cada práctica guarda la versión con la que inició |
| [ADR-001](../../docs/adr/ADR-001-monolito-modular.md) | Módulo **Reglas** aislado: no usa a ningún otro módulo; los demás lo usan. Un programa nuevo toca como máximo 2 módulos |
| [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md) | Solo el director del programa puede configurar sus reglas |
| [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md) | Creación y publicación de versiones quedan en la bitácora |
| [ADR-002](../../docs/adr/ADR-002-plataforma-institucional.md) | Python; adaptadores en memoria en esta etapa |

## 2. Componentes por capa (de la [vista de desarrollo](../../docs/vistas/03-desarrollo.md))

| Capa | Componente | Responsabilidad |
|---|---|---|
| dominio | `VersionReglas` (amplía la de la spec 009) | Horas mínimas, requisitos, vigencia, estado; una publicada no se modifica |
| dominio | `EstadoVersionReglas` | Borrador y publicada |
| dominio | `ValidadorReglas` | Detecta contradicciones (horas en cero, requisitos repetidos o incompatibles) |
| aplicacion/puertos | `RepositorioVersionesReglas`, `CalendarioAcademico`, `Bitacora` (spec 001) | Contratos hacia el exterior; el calendario entrega el periodo siguiente |
| aplicacion | `CrearBorradorReglas`, `PublicarVersionReglas` | Casos de uso |
| aplicacion/dto | `ReglasEntrada`, `ReglasSalida` | Entrada y salida |
| infraestructura | `RepositorioVersionesReglasEnMemoria`, `CalendarioAcademicoFijo` | Adaptadores simulados |

## 3. Flujo

Ver [ESC-05](../../docs/diagramas/secuencias/cu12-configurar-reglas.puml): se crea el borrador, se valida y se publica con vigencia desde el periodo siguiente.

## 4. Datos que se guardan

`VersionReglas`: programa, número de versión, horas mínimas, requisitos, vigencia desde, estado. `RegistroBitacora`: creación y publicación.

## 5. Fuera de alcance

- Interfaz de configuración (aplicación web) y controlador REST.
- Tipos nuevos de regla (se agregan en este módulo con un ADR si hace falta).
- Notificación a los estudiantes de un cambio de reglas.

## 6. Decisiones pendientes

Ninguna.
