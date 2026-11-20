# Plan: 007 Evaluar el desempeño del practicante (CU-07)

Traza: [spec.md](spec.md) · [drivers.md](../../docs/drivers.md) · [arquitectura.md](../../docs/arquitectura.md)

## 1. Decisiones (ADR) que aplican

| ADR | Qué impone a esta funcionalidad |
|---|---|
| [ADR-004](../../docs/adr/ADR-004-autenticacion-dual.md) | Enlace con identificador aleatorio de 256 bits, de un solo uso, 15 días; solo se guarda su hash; respuesta genérica para enlaces usados, vencidos o alterados |
| [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md) | Se registra la evaluación y cada intento rechazado (fecha, hora, dirección de origen) |
| [ADR-003](../../docs/adr/ADR-003-integraciones-outbox.md) | El aviso al docente asesor es una tarea pendiente procesada en segundo plano, no se envía en la petición |
| [ADR-001](../../docs/adr/ADR-001-monolito-modular.md) | Módulo **Evaluaciones**; el dominio no conoce el correo ni la base de datos |
| [ADR-002](../../docs/adr/ADR-002-plataforma-institucional.md) | Python; adaptadores en memoria en esta etapa |

## 2. Componentes por capa (de la [vista de desarrollo](../../docs/vistas/03-desarrollo.md))

| Capa | Componente | Responsabilidad |
|---|---|---|
| dominio | `EnlaceAcceso` | Hash del identificador, vencimiento a 15 días y uso único |
| dominio | `Evaluacion` | Calificación y campos obligatorios de la evaluación |
| aplicacion/puertos | `RepositorioEnlaces`, `RepositorioEvaluaciones`, `RepositorioTareas`, `Reloj` | Contratos hacia el exterior |
| aplicacion/puertos | `Bitacora` (ya definido en la spec 001) | Registro de eventos |
| aplicacion | `AbrirEnlaceEvaluacion` | Valida el enlace, devuelve el formulario o rechaza y registra el intento |
| aplicacion | `RegistrarEvaluacion` | Valida la evaluación, la guarda, marca el enlace como usado |
| aplicacion/dto | `EvaluacionEntrada`, `EvaluacionSalida` | Entrada y salida |
| infraestructura | `RepositorioEnlacesEnMemoria`, `RepositorioEvaluacionesEnMemoria`, `RepositorioTareasEnMemoria`, `RelojFijo` | Adaptadores simulados (el reloj fijo permite probar el vencimiento) |

## 3. Flujo

Ver [ESC-02](../../docs/diagramas/secuencias/cu07-evaluar-practicante.puml): se busca por hash; si es válido se muestra el formulario y se registra la evaluación; si no, se rechaza con respuesta genérica, se registra en bitácora y se crea una tarea pendiente de aviso.

## 4. Datos que se guardan

`EnlaceAcceso`: hash, práctica, vence, usado. `Evaluacion`: práctica, calificación, fecha. `TareaPendiente`: tipo "aviso al docente asesor", estado.

## 5. Fuera de alcance

- Emisión del enlace y su envío por correo ([CU-08](../../docs/drivers.md#cu-08), recordatorios).
- Validación de horas por el supervisor ([CU-05](../../docs/drivers.md#cu-05)), aunque usa el mismo mecanismo.
- Controlador REST y aplicación web; envío real del correo de aviso (solo se crea la tarea).
- Plazo reglamentario de la evaluación (no se especifica en los documentos).

## 6. Decisiones pendientes

Ninguna.
