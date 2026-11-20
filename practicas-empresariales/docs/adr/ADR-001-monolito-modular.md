# ADR-001: Monolito modular con puertos y adaptadores

## Estado
Aceptado — 2026-11-17

## Contexto
El sistema atiende entre 170 y 250 prácticas activas a la vez, con decenas de usuarios concurrentes ([S-03](../vision.md#s-03)), pero sus reglas cambian por programa y por reglamento ([OB-05](../vision.md#ob-05), [S-07](../vision.md#s-07)). [EAC-01](../drivers.md#eac-01-mantenibilidad-modificabilidad) exige incorporar un programa nuevo tocando como máximo 2 módulos. Además depende de sistemas que no controla: el SIA, solo por sus servicios ([RT-03](../drivers.md#rt-03)), el proveedor de identidad ([RT-02](../drivers.md#rt-02)) y el correo institucional. [PA-01](../drivers.md#pa-01) pide decidir los grandes bloques y hacia dónde apuntan las dependencias; [R-04](../vision.md#r-04) advierte del riesgo de sobredimensionar.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Monolito en capas tradicional (presentación, negocio, datos) | Conocido por cualquier equipo; un solo despliegue | El negocio depende de la capa de datos y de cada integración; un cambio de reglas o del SIA atraviesa capas y pone en riesgo [EAC-01](../drivers.md#eac-01) |
| B) Monolito modular con puertos y adaptadores | Un solo desplegable dividido en módulos por capacidad; el dominio define puertos y las integraciones son adaptadores sustituibles | Exige disciplina para que los módulos solo se hablen por sus interfaces; más interfaces que en capas |
| C) Microservicios | Escalado y despliegue independientes | La carga de [S-03](../vision.md#s-03) no lo justifica; multiplica la operación para el Área de Sistemas ([RT-01](../drivers.md#rt-01)) y materializa [R-04](../vision.md#r-04) |

## Decisión
Se elige **B**. Es la única que cumple [EAC-01](../drivers.md#eac-01) sin sobredimensionar: la modularidad responde a [OB-05](../vision.md#ob-05) y la distribución no aporta nada con la carga de [S-03](../vision.md#s-03). Las dependencias apuntan siempre hacia el dominio. Módulos por capacidad: Postulaciones, Horas, Evaluaciones, Actas, Reglas, Seguimiento y Administración. Los puertos (consulta académica, identidad, notificaciones, persistencia, generación de documentos) los declara el dominio y los implementan adaptadores.

## Consecuencias
**Positivas.** El cambio de reglamento se concentra en el módulo de Reglas ([EAC-01](../drivers.md#eac-01)); SIA, identidad y correo se pueden simular o sustituir sin tocar el dominio; el Área de Sistemas opera un solo artefacto de aplicación.

**Negativas (costos aceptados).** Más código de interfaces y adaptadores que en capas; hay que vigilar que ningún módulo use atajos hacia el interior de otro.

**Riesgos.** Que un módulo crezca sin control. Mitigación: revisión de dependencias entre módulos (ciclos prohibidos) en cada Pull Request, con una prueba de arquitectura automática.

## Vistas que modifica
[Procesos](../vistas/02-procesos.md), [Desarrollo](../vistas/03-desarrollo.md)
