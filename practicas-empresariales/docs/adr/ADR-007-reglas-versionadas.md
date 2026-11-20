# ADR-007: Reglas de práctica por programa como datos versionados con vigencia

## Estado
Aceptado — 2026-11-17

## Contexto
[CU-12](../drivers.md#cu-12) permite al director configurar las reglas de práctica de su programa, porque requisitos y horas mínimas varían ([S-07](../vision.md#s-07)). [OB-05](../vision.md#ob-05) exige aplicar un cambio desde el periodo siguiente sin suspender las prácticas en curso. [EAC-01](../drivers.md#eac-01-mantenibilidad-modificabilidad) exige incorporar un programa nuevo en máximo 12 horas, tocando como máximo 2 módulos, con 0 prácticas en curso afectadas y sin indisponibilidad.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Reglas en el código, con condicionales por programa | Rápido para el primer programa | Cada programa nuevo exige modificar y desplegar código en varios sitios: incumple [EAC-01](../drivers.md#eac-01) |
| B) Reglas como datos parametrizados (horas mínimas, requisitos, plazos) versionados por programa y vigencia, evaluados por el módulo de Reglas | El director configura sin programar; cada práctica queda ligada a la versión con la que inició | Solo cubre los tipos de regla previstos; un tipo nuevo exige programar |
| C) Motor de reglas de propósito general | Expresa cualquier regla | Curva de aprendizaje alta, reglas difíciles de verificar, posible incumplimiento de [RT-04](../drivers.md#rt-04) |

## Decisión
Se elige **B**. Cada práctica guarda la referencia a la `VersionReglas` con la que inició, de modo que publicar una versión nueva nunca altera las prácticas en curso. Una versión nueva nace como *borrador*, se valida (sin reglas contradictorias) y se publica con vigencia desde el periodo siguiente. Un tipo nuevo de regla se agrega solo en el módulo de Reglas ([ADR-001](ADR-001-monolito-modular.md)).

## Consecuencias
**Positivas.** Un programa nuevo es configuración y no código ([EAC-01](../drivers.md#eac-01)); las prácticas en curso conservan sus reglas ([OB-05](../vision.md#ob-05)); no hay despliegue para la mayoría de cambios.

**Negativas (costos aceptados).** Hay que construir y mantener la interfaz de configuración y el validador; coexisten varias versiones de reglas activas, lo que complica soporte y reportes.

**Riesgos.** Que el director publique reglas erróneas. Mitigación: borrador → validación → publicación con vigencia futura y registro en bitácora ([ADR-006](ADR-006-bitacora-auditoria.md)).

## Vistas que modifica
[Lógica](../vistas/01-logica.md) (`ReglasPrograma`, `VersionReglas`), [Desarrollo](../vistas/03-desarrollo.md) (módulo Reglas)
