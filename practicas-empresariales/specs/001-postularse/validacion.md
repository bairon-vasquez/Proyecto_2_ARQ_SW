# Validación: 001 Postularse a la práctica empresarial (CU-01)

> Ronda final (T-24) · 2026-11-20 · Python 3.11.9 · `python -m pytest tests` → **17 passed** (`tests/test_postularse.py`: 11, `tests/test_consultar_estado.py`: 6).
> Regla: no se marca "Cumple" sin evidencia. Este documento solo reporta.

| Escenario | Resultado | Evidencia |
|---|---|---|
| Postulación verificada correctamente | **Cumple** | `test_postulacion_verificada_correctamente`: "pendiente de verificación" → "verificada"; bitácora `postulacion_recibida`, `postulacion_verificada`. |
| No cumple los requisitos académicos | **Cumple** | `test_estudiante_no_cumple_requisitos`, `test_mensaje_indica_requisito_faltante` y, para la consulta posterior, `test_consulta_muestra_requisitos_faltantes_si_no_cumple` (los requisitos quedan guardados en la postulación). |
| No autoriza el tratamiento de datos | **Cumple** | `test_sin_autorizacion_de_datos_no_se_guarda`. |
| Ya tiene una postulación activa | **Cumple** | `test_postulacion_activa_se_rechaza_e_informa_estado`. |
| Programa sin reglas publicadas | **Cumple** | `test_programa_sin_reglas_publicadas`. |
| Usuario no es estudiante | **Cumple** | `test_usuario_no_estudiante_se_deniega_y_se_registra`. |
| SIA no responde ([EAC-02](../../docs/drivers.md#eac-02)) | **Cumple a nivel de lógica; medición real pendiente** | `test_sia_caido_guarda_confirma_y_reintenta_sin_intervencion`, `test_sia_lento_cuenta_como_no_responde`, `test_cuarenta_postulaciones_simultaneas_no_se_pierden`. El timeout real de 4 s, la concurrencia verdadera y el p95 no se miden con adaptadores en memoria (H-03). |
| Reintentos agotados | **Cumple** | `test_reintentos_agotados_dejan_tarea_fallida_visible`. |
| El estudiante consulta el estado de su postulación | **Cumple** | `test_consulta_muestra_estado_actual` (pendiente → verificada), `test_consulta_devuelve_la_ultima_postulacion` y `test_consulta_solo_devuelve_la_postulacion_propia`. |
| El estudiante consulta sin haber postulado | **Cumple** | `test_consulta_sin_haber_postulado`: "Aún no tiene postulaciones". |
| El usuario no es estudiante y consulta el estado | **Cumple** | `test_consulta_de_no_estudiante_se_deniega_y_se_registra`: `PermissionError` y bitácora `['acceso_denegado']`. |

## Revisión de la regla de dependencia

- `dominio/` no importa `aplicacion/` ni `infraestructura/`: **Cumple** (`grep` sin coincidencias).
- `aplicacion/` solo importa `dominio/`: **Cumple** (sin referencias a `infraestructura` en `src/aplicacion/`).
- `infraestructura/` importa `aplicacion/` y `dominio/`: sentido permitido.

## Hallazgos

| ID | Estado | Detalle |
|---|---|---|
| H-01 | Resuelto | `ProcesadorDeTareas` (T-15). |
| H-02 | Resuelto | Pruebas `pytest` (T-16, T-23). |
| H-03 | Aceptado | Medir 4 s, 20 min, 40 simultáneas y p95 con el SIA real y PostgreSQL cuando existan. |
| H-04 | **Resuelto** | Decisión: consulta del estado en la aplicación (`ConsultarEstadoPostulacion`, T-18 a T-23). El correo al estudiante se evalúa en CU-08. |
| H-05 | Abierto (menor) | `AGENTS.md` pide Python 3.12; el entorno local es 3.11.9. El código no usa nada exclusivo de 3.12. |
| H-06 | Aceptado | La versión de reglas la resuelve quien invoca el caso de uso; decidir puerto o ADR en CU-12. |
| H-07 | Aceptado | La consulta de estado solo existe como caso de uso: no hay controlador REST ni pantalla (fuera de alcance en `plan.md`). |
