# Tareas: 009 Generar el acta final (CU-09)

Orden de adentro hacia afuera. Cada tarea toca **un solo archivo**. Reutiliza `Bitacora` de la spec 001 (T-06, T-13).

| Hecho | ID | Tarea | Archivo | Escenarios | Depende de |
|:-:|----|-------|---------|------------|------------|
| [ ] | T-01 | Entidad `VersionReglas` mínima: horas mínimas y requisitos | `src/dominio/version_reglas.py` | Horas insuficientes | — |
| [ ] | T-02 | Entidad `RegistroHoras` con estado (registrado, validado, observado) | `src/dominio/registro_horas.py` | Flujo básico, horas insuficientes | — |
| [ ] | T-03 | Entidad `Practica`: docente asesor, versión de reglas, horas y evaluación recibida | `src/dominio/practica.py` | Todos | T-01, T-02 |
| [ ] | T-04 | Enumeración `EstadoActa` (borrador, aprobada por asesor, aprobada, devuelta) | `src/dominio/estado_acta.py` | Flujo básico, acta aprobada | — |
| [ ] | T-05 | Entidad `PlantillaActa` versionada | `src/dominio/plantilla_acta.py` | Plantilla vigente | — |
| [ ] | T-06 | Entidad `Acta` con versión, huella y referencia al acta anterior | `src/dominio/acta.py` | Flujo básico, acta aprobada | T-04, T-05 |
| [ ] | T-07 | Puerto `RepositorioPracticas` (lectura) | `src/aplicacion/puertos/repositorio_practicas.py` | Todos | T-03 |
| [ ] | T-08 | Puerto `RepositorioActas` | `src/aplicacion/puertos/repositorio_actas.py` | Flujo básico, acta aprobada, plantilla vigente | T-06 |
| [ ] | T-09 | Puerto `GeneradorPdf` (plantilla + datos → bytes) | `src/aplicacion/puertos/generador_pdf.py` | Flujo básico, [EAC-04](../../docs/drivers.md#eac-04) | T-05 |
| [ ] | T-10 | DTO `ActaSalida` | `src/aplicacion/dto/acta_salida.py` | Flujo básico | — |
| [ ] | T-11 | Caso de uso `GenerarActa`: rol, pertenencia, horas, evaluación, plantilla vigente, huella, bitácora | `src/aplicacion/generar_acta.py` | Todos | T-03…T-10, spec 001 T-06 |
| [ ] | T-12 | Adaptador en memoria de prácticas | `src/infraestructura/repositorio_practicas_en_memoria.py` | Todos | T-07 |
| [ ] | T-13 | Adaptador en memoria de actas | `src/infraestructura/repositorio_actas_en_memoria.py` | Flujo básico, acta aprobada | T-08 |
| [ ] | T-14 | Generador de PDF simulado (documento mínimo con retardo configurable) | `src/infraestructura/generador_pdf_simulado.py` | Flujo básico, [EAC-04](../../docs/drivers.md#eac-04) | T-09 |
| [ ] | T-15 | Validación: `validacion.md` con evidencia por escenario y revisión de la regla de dependencia | `specs/009-generar-acta/validacion.md` | Todos | T-01…T-14 |

## Cobertura de escenarios

| Escenario de spec.md | Tareas |
|---|---|
| Acta generada correctamente | T-03, T-06, T-09, T-11, T-13, T-14 |
| Horas validadas insuficientes | T-01, T-02, T-11 |
| Falta la evaluación de la empresa | T-03, T-11 |
| El docente no es el asesor | T-03, T-11 |
| Ya tiene un acta aprobada | T-04, T-06, T-11, T-13 |
| Plantilla vigente sin afectar anteriores | T-05, T-06, T-08, T-11 |
| Generación en el cierre ([EAC-04](../../docs/drivers.md#eac-04)) | T-09, T-11, T-14 |
