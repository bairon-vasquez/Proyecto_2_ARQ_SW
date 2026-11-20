# Tareas: 007 Evaluar el desempeño del practicante (CU-07)

Orden de adentro hacia afuera. Cada tarea toca **un solo archivo**. Reutiliza `Bitacora` y `TareaPendiente` de la spec 001 (T-06, T-03, T-13).

| Hecho | ID | Tarea | Archivo | Escenarios | Depende de |
|:-:|----|-------|---------|------------|------------|
| [ ] | T-01 | Entidad `EnlaceAcceso`: hash, vencimiento a 15 días, uso único | `src/dominio/enlace_acceso.py` | Todos | — |
| [ ] | T-02 | Entidad `Evaluacion` con campos obligatorios y rango de calificación | `src/dominio/evaluacion.py` | Flujo básico, datos incompletos | — |
| [ ] | T-03 | Puerto `RepositorioEnlaces` (busca por hash) | `src/aplicacion/puertos/repositorio_enlaces.py` | Todos | T-01 |
| [ ] | T-04 | Puerto `RepositorioEvaluaciones` | `src/aplicacion/puertos/repositorio_evaluaciones.py` | Flujo básico | T-02 |
| [ ] | T-05 | Puerto `RepositorioTareas` | `src/aplicacion/puertos/repositorio_tareas.py` | Enlaces no válidos, [EAC-03](../../docs/drivers.md#eac-03) | spec 001 T-03 |
| [ ] | T-06 | Puerto `Reloj` | `src/aplicacion/puertos/reloj.py` | Enlace vencido | — |
| [ ] | T-07 | DTO `EvaluacionEntrada` | `src/aplicacion/dto/evaluacion_entrada.py` | Flujo básico, datos incompletos | — |
| [ ] | T-08 | DTO `EvaluacionSalida` | `src/aplicacion/dto/evaluacion_salida.py` | Todos | — |
| [ ] | T-09 | Caso de uso `AbrirEnlaceEvaluacion`: valida, rechaza con respuesta genérica, registra intento y crea tarea de aviso | `src/aplicacion/abrir_enlace_evaluacion.py` | Enlace usado, vencido, alterado, [EAC-03](../../docs/drivers.md#eac-03) | T-01, T-03, T-05, T-06, T-08, spec 001 T-06 |
| [ ] | T-10 | Caso de uso `RegistrarEvaluacion`: valida datos, guarda, marca el enlace como usado, registra en bitácora | `src/aplicacion/registrar_evaluacion.py` | Flujo básico, datos incompletos | T-01…T-08, spec 001 T-06 |
| [ ] | T-11 | Adaptador en memoria de enlaces | `src/infraestructura/repositorio_enlaces_en_memoria.py` | Todos | T-03 |
| [ ] | T-12 | Adaptador en memoria de evaluaciones | `src/infraestructura/repositorio_evaluaciones_en_memoria.py` | Flujo básico | T-04 |
| [ ] | T-13 | Adaptador en memoria de tareas | `src/infraestructura/repositorio_tareas_en_memoria.py` | [EAC-03](../../docs/drivers.md#eac-03) | T-05 |
| [ ] | T-14 | Reloj fijo configurable | `src/infraestructura/reloj_fijo.py` | Enlace vencido | T-06 |
| [ ] | T-15 | Validación: `validacion.md` con evidencia por escenario y revisión de la regla de dependencia | `specs/007-evaluar-practicante/validacion.md` | Todos | T-01…T-14 |

## Cobertura de escenarios

| Escenario de spec.md | Tareas |
|---|---|
| Evaluación registrada con enlace válido | T-01, T-02, T-04, T-10, T-11, T-12 |
| Datos incompletos o fuera de rango | T-02, T-07, T-10 |
| Enlace ya usado | T-01, T-09, T-11 |
| Enlace vencido | T-01, T-06, T-09, T-14 |
| Identificador alterado | T-03, T-09, T-11 |
| Rechazo de enlaces no válidos ([EAC-03](../../docs/drivers.md#eac-03)) | T-05, T-09, T-13 |
