# Validación: 001 Postularse a la práctica empresarial (CU-01)

> Fecha: 2026-11-20 · Python 3.11.9 · Evidencia: ejecución real de los casos de uso de `src/` con los adaptadores en memoria (script manual, sin pruebas `pytest` en el repo; ver hallazgo H-02).
> Regla: no se marca "Cumple" sin evidencia. Este documento solo reporta; no se corrigió nada.

| Escenario | Resultado | Evidencia |
|---|---|---|
| Postulación verificada correctamente | **Cumple** | `PostularseAPractica` devolvió `aceptada=True`, estado "pendiente de verificación" y mensaje "Postulación recibida, en verificación". `VerificarPostulacion` la dejó en "verificada". Bitácora: `['postulacion_recibida', 'postulacion_verificada']`. Archivos: `aplicacion/postularse_a_practica.py`, `aplicacion/verificar_postulacion.py`. |
| No cumple los requisitos académicos | **Cumple** | Con el SIA simulado devolviendo `['promedio']`: estado "no cumple requisitos", mensaje "No cumple requisitos. Falta: promedio". La entrega al estudiante de ese mensaje no existe aún (ver H-04). |
| No autoriza el tratamiento de datos | **Cumple** | `aceptada=False`, "Debe autorizar el tratamiento de sus datos personales"; postulaciones guardadas: 0. |
| Ya tiene una postulación activa | **Cumple** | Segunda postulación rechazada: "Ya tiene una postulación en estado 'pendiente de verificación'" (incluye el estado existente). |
| Programa sin reglas publicadas | **Cumple** | `version_reglas_vigente=None` → rechazo con "contacte al director de programa". |
| Usuario no es estudiante | **Cumple** | Rol "docente asesor" → `PermissionError("Solo un estudiante puede postularse")`; bitácora registra `acceso_denegado`. |
| SIA no responde ([EAC-02](../../docs/drivers.md#eac-02)) | **No cumple (parcial)** | Cumple: la postulación se guarda en "pendiente de verificación" sin llamar al SIA; confirmación en 0,00001 s con adaptadores en memoria; ante `TimeoutError` (demora 5 s > 4 s) o `ConnectionError` la tarea se reprograma con espera 15→300 s y la postulación no se pierde. **No demostrado:** reintento "sin intervención humana" (no existe el procesador que sondea tareas, H-01); verificación en ≤ 20 min tras la recuperación; 40 postulaciones simultáneas; 95 % < 2 s con carga real (H-03). |
| Reintentos agotados | **Cumple** | Tras 8 fallos: tarea `fallida` (intentos=8), postulación en "pendiente de verificación", `tareas_fallidas()` devuelve 1 y la bitácora registra `verificacion_fallida`. El aviso por correo queda fuera de alcance según `plan.md`. |

## Revisión de la regla de dependencia

- `dominio/` no importa `aplicacion/` ni `infraestructura/`: **Cumple** (búsqueda con `grep` sin coincidencias).
- `aplicacion/` solo importa `dominio/`: **Cumple** (sin referencias a `infraestructura` en `src/aplicacion/`; solo importa `dominio` y su propio paquete).

## Hallazgos

| ID | Origen | Hallazgo | Acción |
|---|---|---|---|
| H-01 | Especificación/plan | La spec exige reintento sin intervención humana, pero `plan.md` y `tasks.md` no incluyen el **Procesador de tareas** que aparece en la vista de desarrollo y en la secuencia ESC-01 (sondeo cada 15 s). Nada invoca `VerificarPostulacion` automáticamente. | Primero corregir `plan.md` (agregar el componente); luego tarea nueva **T-15** `src/infraestructura/procesador_de_tareas.py`. |
| H-02 | Código | No hay pruebas automáticas; la evidencia es un script manual no versionado. | Tarea nueva **T-16**: pruebas `pytest` de los 8 escenarios (permitidas por `AGENTS.md`). |
| H-03 | Código | Los umbrales de EAC-02 (4 s, 20 min, 40 simultáneas, p95 < 2 s) no se pueden medir con adaptadores en memoria; el adaptador del SIA solo simula la demora. | Se acepta en esta etapa; medir con el adaptador real y PostgreSQL cuando existan. |
| H-04 | Especificación | "Se le indica qué requisito falta" se produce de forma asíncrona (en la salida de `VerificarPostulacion`) y no hay mecanismo para mostrárselo al estudiante (consulta de estado o correo). | Aclarar en `spec.md` cómo se entera el estudiante; hoy es `[NECESITA ACLARACIÓN]`. |
| H-05 | Entorno | `AGENTS.md` pide Python 3.12; el entorno local tiene 3.11.9. El código no usa nada propio de 3.12. | Confirmar la versión objetivo. |
| H-06 | Código | `PostulacionEntrada.version_reglas_vigente` la resuelve quien llama porque el plan no define un puerto de reglas. | Decidir en CU-12 si se agrega un puerto o un ADR. |
