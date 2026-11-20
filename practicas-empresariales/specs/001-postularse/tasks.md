# Tareas: 001 Postularse a la práctica empresarial (CU-01)

Orden de adentro hacia afuera. Cada tarea toca **un solo archivo**.

| Hecho | ID | Tarea | Archivo | Escenarios | Depende de |
|:-:|----|-------|---------|------------|------------|
| [x] | T-01 | Enumeración `EstadoPostulacion` (pendiente de verificación, verificada, no cumple requisitos, aprobada, rechazada) | `src/dominio/estado_postulacion.py` | Todos | — |
| [x] | T-02 | Entidad `Postulacion` con transiciones válidas de estado | `src/dominio/postulacion.py` | Flujo básico, no cumple, SIA caído | T-01 |
| [x] | T-03 | Entidad `TareaPendiente` con intentos, próximo intento y estado | `src/dominio/tarea_pendiente.py` | SIA caído, reintentos agotados | — |
| [x] | T-04 | Puerto `ConsultaAcademica` (Protocol) | `src/aplicacion/puertos/consulta_academica.py` | Flujo básico, no cumple, SIA caído | T-02 |
| [x] | T-05 | Puerto `RepositorioPostulaciones` (Protocol), incluye tareas pendientes | `src/aplicacion/puertos/repositorio_postulaciones.py` | Todos | T-02, T-03 |
| [x] | T-06 | Puerto `Bitacora` (Protocol) | `src/aplicacion/puertos/bitacora.py` | Flujo básico, no es estudiante | — |
| [x] | T-07 | DTO `PostulacionEntrada` | `src/aplicacion/dto/postulacion_entrada.py` | Todos | — |
| [x] | T-08 | DTO `PostulacionSalida` | `src/aplicacion/dto/postulacion_salida.py` | Flujo básico, SIA caído | — |
| [x] | T-09 | Caso de uso `PostularseAPractica`: rol, autorización de datos, unicidad, reglas publicadas; guarda postulación y tarea; registra en bitácora | `src/aplicacion/postularse_a_practica.py` | Sin autorización, ya activa, sin reglas, no estudiante, confirmación < 2 s | T-02…T-08 |
| [x] | T-10 | Caso de uso `VerificarPostulacion`: consulta el SIA (4 s), actualiza estado, reprograma con espera creciente, marca fallida tras 8 intentos | `src/aplicacion/verificar_postulacion.py` | Flujo básico, no cumple, SIA caído, reintentos agotados | T-02…T-06 |
| [x] | T-11 | Adaptador en memoria del SIA (configurable: responde, falla o tarda) | `src/infraestructura/consulta_academica_en_memoria.py` | SIA caído | T-04 |
| [x] | T-12 | Adaptador en memoria del repositorio | `src/infraestructura/repositorio_postulaciones_en_memoria.py` | Todos | T-05 |
| [x] | T-13 | Adaptador en memoria de la bitácora | `src/infraestructura/bitacora_en_memoria.py` | Flujo básico, no es estudiante | T-06 |
| [x] | T-14 | Validación: `validacion.md` con evidencia por escenario y revisión de la regla de dependencia | `specs/001-postularse/validacion.md` | Todos | T-01…T-13 |
| [ ] | T-15 | Procesador de tareas: sondea las tareas listas cada 15 s e invoca `VerificarPostulacion` (hallazgo H-01) | `src/infraestructura/procesador_de_tareas.py` | SIA caído, reintentos agotados | T-10, T-12 |
| [ ] | T-16 | Pruebas `pytest` de los escenarios de `spec.md` (hallazgo H-02) | `tests/test_postularse.py` | Todos | T-01…T-15 |
| [ ] | T-17 | Revalidación: actualizar `validacion.md` con la evidencia de las pruebas | `specs/001-postularse/validacion.md` | Todos | T-15, T-16 |

> T-14 fue la primera ronda de validación; T-15 a T-17 salen de sus hallazgos H-01 y H-02.

## Cobertura de escenarios

| Escenario de spec.md | Tareas |
|---|---|
| Postulación verificada correctamente | T-02, T-06, T-09, T-10, T-11, T-12, T-13 |
| No cumple los requisitos | T-02, T-10, T-11 |
| No autoriza el tratamiento de datos | T-07, T-09 |
| Ya tiene postulación activa | T-09, T-12 |
| Programa sin reglas publicadas | T-09 |
| Usuario no es estudiante | T-06, T-09, T-13 |
| SIA no responde ([EAC-02](../../docs/drivers.md#eac-02)) | T-03, T-09, T-10, T-11, T-15 |
| Reintentos agotados | T-03, T-10, T-15 |
