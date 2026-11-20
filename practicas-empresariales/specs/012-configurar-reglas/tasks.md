# Tareas: 012 Configurar las reglas de práctica de un programa (CU-12)

Orden de adentro hacia afuera. Cada tarea toca **un solo archivo**. Amplía `VersionReglas` de la spec 009 y reutiliza `Bitacora` de la spec 001 y `PoliticaAutorizacion` de la spec 010.

| Hecho | ID | Tarea | Archivo | Escenarios | Depende de |
|:-:|----|-------|---------|------------|------------|
| [ ] | T-01 | Enumeración `EstadoVersionReglas` (borrador, publicada) | `src/dominio/estado_version_reglas.py` | Todos | — |
| [ ] | T-02 | Ampliar `VersionReglas`: vigencia, estado, inmutabilidad si está publicada | `src/dominio/version_reglas.py` | Borrador, publicar, versión publicada | T-01, spec 009 T-01 |
| [ ] | T-03 | Servicio de dominio `ValidadorReglas` | `src/dominio/validador_reglas.py` | Reglas contradictorias | T-02 |
| [ ] | T-04 | Puerto `RepositorioVersionesReglas` | `src/aplicacion/puertos/repositorio_versiones_reglas.py` | Todos | T-02 |
| [ ] | T-05 | Puerto `CalendarioAcademico` (periodo actual y siguiente) | `src/aplicacion/puertos/calendario_academico.py` | Publicar | — |
| [ ] | T-06 | DTO `ReglasEntrada` | `src/aplicacion/dto/reglas_entrada.py` | Borrador, contradictorias | — |
| [ ] | T-07 | DTO `ReglasSalida` | `src/aplicacion/dto/reglas_salida.py` | Todos | — |
| [ ] | T-08 | Caso de uso `CrearBorradorReglas`: rol y pertenencia al programa, bitácora | `src/aplicacion/crear_borrador_reglas.py` | Borrador, director de otro programa | T-02, T-04, T-06, T-07, spec 010 T-03, spec 001 T-06 |
| [ ] | T-09 | Caso de uso `PublicarVersionReglas`: valida, fija vigencia, no toca prácticas en curso, bitácora | `src/aplicacion/publicar_version_reglas.py` | Publicar, contradictorias, prácticas en curso, versión publicada, [EAC-01](../../docs/drivers.md#eac-01) | T-02…T-07, spec 010 T-03, spec 001 T-06 |
| [ ] | T-10 | Adaptador en memoria de versiones de reglas | `src/infraestructura/repositorio_versiones_reglas_en_memoria.py` | Todos | T-04 |
| [ ] | T-11 | Calendario académico fijo | `src/infraestructura/calendario_academico_fijo.py` | Publicar | T-05 |
| [ ] | T-12 | Validación: `validacion.md` con evidencia por escenario, incluyendo la prueba de [EAC-01](../../docs/drivers.md#eac-01) (programa nuevo solo con datos) y la regla de dependencia | `specs/012-configurar-reglas/validacion.md` | Todos | T-01…T-11 |

## Cobertura de escenarios

| Escenario de spec.md | Tareas |
|---|---|
| Crear una versión en borrador | T-02, T-08, T-10 |
| Publicar con vigencia desde el periodo siguiente | T-05, T-09, T-11 |
| Reglas contradictorias no se publican | T-03, T-09 |
| Prácticas en curso conservan su versión | T-09, T-10 |
| Una versión publicada no se edita | T-01, T-02, T-09 |
| Director de otro programa | T-08, T-09 |
| Programa nuevo sin tocar el código ([EAC-01](../../docs/drivers.md#eac-01)) | T-09, T-12 |
