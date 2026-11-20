# Validación: 001 Postularse a la práctica empresarial (CU-01)

> Segunda ronda (T-17) · 2026-11-20 · Python 3.11.9 · `python -m pytest tests` → **11 passed**.
> Regla: no se marca "Cumple" sin evidencia. Este documento solo reporta. La primera ronda (T-14) encontró los hallazgos H-01 y H-02, resueltos con T-15 y T-16.

| Escenario | Resultado | Evidencia (`tests/test_postularse.py`) |
|---|---|---|
| Postulación verificada correctamente | **Cumple** | `test_postulacion_verificada_correctamente`: queda "pendiente de verificación", el procesador la deja "verificada" y la bitácora registra `postulacion_recibida`, `postulacion_verificada`. |
| No cumple los requisitos académicos | **Cumple** | `test_estudiante_no_cumple_requisitos` y `test_mensaje_indica_requisito_faltante`: estado "no cumple requisitos" y el mensaje nombra el requisito. La forma en que el estudiante lo recibe sigue sin definirse (H-04). |
| No autoriza el tratamiento de datos | **Cumple** | `test_sin_autorizacion_de_datos_no_se_guarda`: rechazo con aviso y sin postulación ni tarea guardadas. |
| Ya tiene una postulación activa | **Cumple** | `test_postulacion_activa_se_rechaza_e_informa_estado`: rechazo con el estado existente; tras verificarse sigue considerándose activa. |
| Programa sin reglas publicadas | **Cumple** | `test_programa_sin_reglas_publicadas`: rechazo con "contacte al director de programa" y sin guardar. |
| Usuario no es estudiante | **Cumple** | `test_usuario_no_estudiante_se_deniega_y_se_registra`: `PermissionError`, bitácora `['acceso_denegado']`, nada guardado. |
| SIA no responde ([EAC-02](../../docs/drivers.md#eac-02)) | **Cumple a nivel de lógica; medición real pendiente** | `test_sia_caido_guarda_confirma_y_reintenta_sin_intervencion`: guarda en "pendiente de verificación", confirma en < 2 s, el procesador reintenta solo y verifica a ≤ 315 s de recuperarse el SIA (≪ 20 min). `test_sia_lento_cuenta_como_no_responde`: demora de 5 s > 4 s cuenta como fallo. `test_cuarenta_postulaciones_simultaneas_no_se_pierden`: 40 postulaciones, ninguna perdida. Límites: el timeout real de 4 s, la concurrencia verdadera y el p95 no se pueden medir con adaptadores en memoria (H-03). |
| Reintentos agotados | **Cumple** | `test_reintentos_agotados_dejan_tarea_fallida_visible`: tarea `fallida` con 8 intentos, postulación en "pendiente de verificación", `tareas_fallidas()` la lista, bitácora `verificacion_fallida` y no se reprocesa. El correo al director queda fuera de alcance según `plan.md`. |

## Revisión de la regla de dependencia

- `dominio/` no importa `aplicacion/` ni `infraestructura/`: **Cumple** (`grep` sin coincidencias).
- `aplicacion/` solo importa `dominio/`: **Cumple** (sin referencias a `infraestructura` en `src/aplicacion/`).
- `infraestructura/` importa `aplicacion/` y `dominio/` (adaptadores y procesador): sentido permitido.

## Hallazgos

| ID | Estado | Detalle |
|---|---|---|
| H-01 | **Resuelto** | `ProcesadorDeTareas` (T-15) y plan actualizado. |
| H-02 | **Resuelto** | 11 pruebas `pytest` (T-16). |
| H-03 | Aceptado | Medir 4 s, 20 min, 40 simultáneas y p95 con el SIA real y PostgreSQL cuando existan. |
| H-04 | **Abierto** | Falta decidir cómo se entera el estudiante del requisito faltante (verificación asíncrona). Marcado `[NECESITA ACLARACIÓN]` en `spec.md`; requiere decisión humana. |
| H-05 | Abierto | `AGENTS.md` pide Python 3.12; el entorno local es 3.11.9. El código no usa nada exclusivo de 3.12. |
| H-06 | Aceptado | La versión de reglas la resuelve quien invoca el caso de uso; decidir puerto o ADR en CU-12. |
