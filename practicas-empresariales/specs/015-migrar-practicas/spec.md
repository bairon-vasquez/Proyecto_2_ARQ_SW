# language: es
# Traza: [CU-15](../../docs/drivers.md#cu-15), [R-05](../../docs/vision.md#r-05), [OB-04](../../docs/vision.md#ob-04), [ADR-009](../../docs/adr/ADR-009-migracion-inicial.md), [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md), [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md)
Característica: Migrar las prácticas en curso desde Excel

  Como administrador del sistema
  quiero cargar las prácticas en curso desde la plantilla normalizada
  para iniciar la operación con datos validados sin digitarlos manualmente.

  Antecedentes:
    Dado un administrador del sistema autenticado
    Y una plantilla de Excel normalizada con las prácticas de un docente asesor

  Escenario: Simulación sin errores (flujo básico, primera fase)
    Dado que todas las filas de la plantilla cumplen el formato y las reglas de su programa
    Cuando el administrador ejecuta la migración en modo simulación
    Entonces el reporte indica 0 errores y el total de prácticas que se cargarían
    Y no se escribe ningún dato en el sistema

  Escenario: Simulación con errores
    Dado que algunas filas tienen datos faltantes o inválidos
    Cuando el administrador ejecuta la migración en modo simulación
    Entonces el reporte lista cada error con su fila y su docente asesor
    Y no se escribe ningún dato en el sistema

  Escenario: Carga real después de una simulación sin errores
    Dado que la última simulación terminó con 0 errores
    Cuando el administrador ejecuta la carga real
    Entonces cada práctica se crea por los mismos casos de uso del dominio
    Y cada práctica queda asociada a la versión de reglas vigente de su programa
    Y cada creación queda registrada en la bitácora

  Escenario: La carga real se rechaza si hay errores
    Dado que la simulación reportó errores
    Cuando el administrador intenta la carga real
    Entonces la carga se rechaza
    Y no se crea ninguna práctica

  Escenario: Práctica ya existente
    Dado que una fila corresponde a una práctica ya cargada
    Cuando se ejecuta la migración
    Entonces esa fila se omite sin duplicar la práctica
    Y se informa como "ya migrada" en el reporte

  Escenario: Programa sin reglas publicadas
    Dado una fila de un programa sin versión de reglas publicada
    Cuando se ejecuta la migración
    Entonces la fila se informa como error
    Y no se crea la práctica

  Escenario: Reporte final de pendientes
    Cuando termina la carga real
    Entonces el reporte final indica las prácticas migradas y las pendientes por docente asesor
    Y el director de programa puede revisarlo antes del lanzamiento
