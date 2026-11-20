# Tareas: 015 Migrar las prácticas en curso desde Excel (CU-15)

Orden de adentro hacia afuera. Cada tarea toca **un solo archivo**. Reutiliza `Practica` (spec 009), `RepositorioVersionesReglas` (spec 012) y `Bitacora` (spec 001).

| Hecho | ID | Tarea | Archivo | Escenarios | Depende de |
|:-:|----|-------|---------|------------|------------|
| [ ] | T-01 | Entidad `FilaMigracion` | `src/dominio/fila_migracion.py` | Todos | — |
| [ ] | T-02 | Entidad `ErrorMigracion` (fila, docente asesor, causa) | `src/dominio/error_migracion.py` | Simulación con errores, programa sin reglas | — |
| [ ] | T-03 | Puerto `LectorPlantilla` (devuelve filas) | `src/aplicacion/puertos/lector_plantilla.py` | Todos | T-01 |
| [ ] | T-04 | DTO `ReporteMigracion` (errores, migradas, omitidas, pendientes por docente) | `src/aplicacion/dto/reporte_migracion.py` | Simulación, reporte final | T-02 |
| [ ] | T-05 | Caso de uso `ValidarPlantillaMigracion`: valida filas y reglas sin escribir nada | `src/aplicacion/validar_plantilla_migracion.py` | Simulación sin errores, con errores, programa sin reglas | T-01…T-04, spec 012 T-04 |
| [ ] | T-06 | Caso de uso `CargarPracticasMigracion`: exige simulación sin errores, crea prácticas con la versión vigente, omite duplicadas, bitácora | `src/aplicacion/cargar_practicas_migracion.py` | Carga real, rechazo con errores, práctica existente, reporte final | T-01…T-05, spec 009 T-07, spec 001 T-06 |
| [ ] | T-07 | Lector de plantilla en memoria | `src/infraestructura/lector_plantilla_en_memoria.py` | Todos | T-03 |
| [ ] | T-08 | Comando de migración por línea de comandos (`--simulacion` / `--cargar`) | `src/infraestructura/comando_migracion.py` | Todos | T-05, T-06, T-07 |
| [ ] | T-09 | Validación: `validacion.md` con evidencia por escenario y revisión de la regla de dependencia | `specs/015-migrar-practicas/validacion.md` | Todos | T-01…T-08 |

## Cobertura de escenarios

| Escenario de spec.md | Tareas |
|---|---|
| Simulación sin errores | T-01, T-04, T-05, T-07, T-08 |
| Simulación con errores | T-02, T-05 |
| Carga real tras simulación sin errores | T-06, T-08 |
| La carga real se rechaza si hay errores | T-06 |
| Práctica ya existente | T-06 |
| Programa sin reglas publicadas | T-02, T-05 |
| Reporte final de pendientes | T-04, T-06 |
