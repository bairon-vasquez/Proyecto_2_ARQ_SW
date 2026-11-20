# Tareas: 010 Aprobar el acta electrónicamente (CU-10)

Orden de adentro hacia afuera. Cada tarea toca **un solo archivo**. Depende de la spec 009 (`Acta`, `EstadoActa`, `RepositorioActas`), la spec 007 (`RepositorioTareas`) y la spec 001 (`Bitacora`).

| Hecho | ID | Tarea | Archivo | Escenarios | Depende de |
|:-:|----|-------|---------|------------|------------|
| [ ] | T-01 | Enumeración `Rol` | `src/dominio/rol.py` | Sin rol requerido | — |
| [ ] | T-02 | Entidad `AprobacionActa` (acta, rol, actor, fecha, versión) | `src/dominio/aprobacion_acta.py` | Asesor, director | spec 009 T-06 |
| [ ] | T-03 | Política de autorización: permisos por caso de uso, negación por defecto | `src/aplicacion/politica_autorizacion.py` | Sin rol, no es el asesor | T-01 |
| [ ] | T-04 | Puerto `AlmacenamientoDocumentos` (guardar una sola vez, leer) | `src/aplicacion/puertos/almacenamiento_documentos.py` | Director, inmutable | — |
| [ ] | T-05 | DTO `AprobacionEntrada` | `src/aplicacion/dto/aprobacion_entrada.py` | Todos | — |
| [ ] | T-06 | Caso de uso `AprobarActaComoAsesor` | `src/aplicacion/aprobar_acta_como_asesor.py` | Asesor, sin rol, no es el asesor | T-02, T-03, T-05, spec 009 T-08, spec 001 T-06 |
| [ ] | T-07 | Caso de uso `AprobarActaComoDirector`: exige aprobación previa, guarda PDF con huella, crea tarea de aviso | `src/aplicacion/aprobar_acta_como_director.py` | Director, director antes que asesor, inmutable | T-02…T-05, spec 007 T-05, spec 009 T-08 |
| [ ] | T-08 | Caso de uso `DevolverActa` con observaciones | `src/aplicacion/devolver_acta.py` | Devolución | T-02, T-03, T-05, spec 009 T-08 |
| [ ] | T-09 | Caso de uso `RechazarModificacionActa`: toda modificación o borrado de un acta aprobada se rechaza y se registra | `src/aplicacion/rechazar_modificacion_acta.py` | Inmutable | T-03, T-04, spec 001 T-06 |
| [ ] | T-10 | Adaptador en memoria del almacenamiento (rechaza reescritura) | `src/infraestructura/almacenamiento_documentos_en_memoria.py` | Director, inmutable | T-04 |
| [ ] | T-11 | Validación: `validacion.md` con evidencia por escenario y revisión de la regla de dependencia | `specs/010-aprobar-acta/validacion.md` | Todos | T-01…T-10 |

## Cobertura de escenarios

| Escenario de spec.md | Tareas |
|---|---|
| Aprobación del docente asesor | T-02, T-03, T-06 |
| Aprobación del director | T-02, T-04, T-07, T-10 |
| El director intenta aprobar antes que el asesor | T-07 |
| Usuario sin el rol requerido | T-01, T-03, T-06 |
| Docente que no es el asesor | T-03, T-06 |
| El director devuelve el acta | T-08 |
| Acta aprobada no se modifica ni se borra | T-04, T-09, T-10 |
