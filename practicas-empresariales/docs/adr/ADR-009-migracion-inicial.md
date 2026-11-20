# ADR-009: Migración inicial con plantilla normalizada y comando de carga con validación previa

## Estado
Aceptado — 2026-11-17

## Contexto
[CU-15](../drivers.md#cu-15) carga las prácticas en curso desde archivos de Excel con formatos distintos por docente asesor (entre 170 y 250 prácticas activas, [S-03](../vision.md#s-03)). Es caso de uso primario por **riesgo**: hay incertidumbre sobre la calidad de los datos y de ella depende el primer despliegue. [R-05](../vision.md#r-05) advierte que los docentes pueden resistirse al cambio.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Digitación manual de las prácticas en curso | Sin desarrollo | Lenta y con errores de transcripción ([OB-04](../vision.md#ob-04)) para 170–250 prácticas |
| B) Plantilla de Excel normalizada que cada docente llena y un comando de carga única con modo de simulación (*dry-run*) que valida y reporta errores antes de importar | Esfuerzo acotado; los errores se detectan antes de cargar; reutiliza los casos de uso del dominio | Trabajo adicional, una sola vez, para los docentes asesores |
| C) Importador permanente que lee cada formato existente | Reutilizable | Mucho esfuerzo para algo que se usa una vez; contradice el carácter único de [CU-15](../drivers.md#cu-15) |

## Decisión
Se elige **B**. El comando se ejecuta primero en modo simulación y genera un reporte de errores por docente; solo cuando el reporte queda en cero errores se ejecuta la carga real. La carga crea las prácticas a través de los **mismos casos de uso del dominio**, de modo que respeta las reglas del programa ([ADR-007](ADR-007-reglas-versionadas.md)), asigna la versión de reglas vigente y deja rastro en la bitácora ([ADR-006](ADR-006-bitacora-auditoria.md)). Después del lanzamiento el comando se archiva y no forma parte de la aplicación.

## Consecuencias
**Positivas.** Carga validada y controlada; sin código de un solo uso dentro de la aplicación; trazabilidad de lo migrado.

**Negativas (costos aceptados).** El lanzamiento depende de que los docentes llenen la plantilla a tiempo; el reporte de errores consume tiempo del director de programa.

**Riesgos.** Que queden prácticas sin migrar. Mitigación: reporte de pendientes por docente, revisión del director antes del lanzamiento y posibilidad de registrar manualmente casos excepcionales.

## Vistas que modifica
[Procesos](../vistas/02-procesos.md) (comando de migración como proceso puntual)
