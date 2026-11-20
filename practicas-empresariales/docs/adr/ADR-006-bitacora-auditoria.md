# ADR-006: Bitácora de auditoría de solo inserción en la base de datos

## Estado
Aceptado — 2026-11-17

## Contexto
[PA-03](../drivers.md#pa-03) pide decidir qué eventos se registran, dónde y por cuánto tiempo. [OB-06](../vision.md#ob-06) exige entregar el consolidado de cualquier periodo en máximo 1 día hábil; [CU-10](../drivers.md#cu-10) requiere saber quién aprobó el acta y cuándo ([S-06](../vision.md#s-06)); [EAC-03](../drivers.md#eac-03-seguridad-confidencialidad-y-responsabilidad) exige registrar cada intento rechazado con fecha, hora y dirección de origen en menos de 1 minuto; [RN-01](../drivers.md#rn-01) exige controlar el acceso a datos personales y [RN-02](../drivers.md#rn-02) exige conservar evidencias según la tabla de retención.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Archivos de registro (logs) del servidor | Ya existen | Se rotan y se pierden; difíciles de consultar para un consolidado ([OB-06](../vision.md#ob-06)); no prueban quién aprobó qué |
| B) Tabla de bitácora de solo inserción en PostgreSQL, escrita en la misma transacción que la operación | Consultable y consistente con los datos; registro inmediato ([EAC-03](../drivers.md#eac-03)) | Crece con el tiempo; obliga a definir la conservación |
| C) Plataforma externa de gestión de eventos de seguridad | Análisis avanzado | Fuera del catálogo y con posible costo recurrente ([RT-04](../drivers.md#rt-04), [RN-05](../drivers.md#rn-05)); sobredimensionada ([R-04](../vision.md#r-04)) |

## Decisión
Se elige **B**. Se registran: aprobaciones del acta (quién, cuándo, versión), cambios de estado de cada práctica, publicación de versiones de reglas, accesos a datos personales y los intentos de acceso rechazados. La aplicación solo puede insertar en la bitácora: el usuario de base de datos de la aplicación no tiene permiso de modificar ni borrar. Se conserva según la tabla de retención documental ([RN-02](../drivers.md#rn-02)) y se particiona por periodo académico para consolidar rápido.

## Consecuencias
**Positivas.** Aprobación trazable ([CU-10](../drivers.md#cu-10), [S-06](../vision.md#s-06)); el consolidado de auditoría sale de una consulta ([OB-06](../vision.md#ob-06)); registro inmediato ([EAC-03](../drivers.md#eac-03)); la mesa de ayuda puede diagnosticar.

**Negativas (costos aceptados).** Cada operación hace una escritura más; la tabla crece de forma permanente y su almacenamiento debe presupuestarse.

**Riesgos.** Que alguien con acceso directo a la base de datos altere registros. Mitigación: permisos de solo inserción administrados por el Área de Sistemas y encadenamiento de hash entre registros consecutivos para detectar alteraciones.

## Vistas que modifica
[Lógica](../vistas/01-logica.md) (entidad `RegistroBitacora`), [Procesos](../vistas/02-procesos.md)
