# ADR-002: Plataforma tecnológica y despliegue en la infraestructura institucional

## Estado
Aceptado — 2026-11-17. **Decisión impuesta por restricciones.**

## Contexto
[RT-01](../drivers.md#rt-01) obliga a desplegar en la infraestructura que administra la Universidad; [RT-04](../drivers.md#rt-04) obliga a usar el motor de base de datos y las tecnologías del catálogo institucional; [RN-05](../drivers.md#rn-05) prohíbe licencias comerciales de pago recurrente. [S-09](../vision.md#s-09) supone que el catálogo incluye PostgreSQL, Python y Angular, y [S-10](../vision.md#s-10) que las políticas están vigentes; ambos se confirman con el Área de Sistemas en la primera semana.

## Alternativas consideradas
No hay alternativas libres: la decisión viene impuesta. Se registra igual para que nadie la discuta después como si hubiera sido una elección. Quedan descartadas de entrada:

| Alternativa descartada | Restricción que la descarta |
|---|---|
| Servicios gestionados de nube pública (funciones sin servidor, BD como servicio) | [RT-01](../drivers.md#rt-01) |
| Plataformas comerciales de flujos de trabajo o de bajo código por suscripción | [RN-05](../drivers.md#rn-05) |
| Lenguajes, frameworks o motores fuera del catálogo institucional (p. ej. una base documental) | [RT-04](../drivers.md#rt-04) |

## Decisión
Se construye una aplicación web desplegada en servidores del Área de Sistemas, con PostgreSQL como base relacional, el servidor de aplicación en Python y la interfaz en Angular (sujeto a confirmar [S-09](../vision.md#s-09)), empaquetada en contenedores si el Área de Sistemas los soporta (ver [ADR-010](ADR-010-configuracion-y-entornos.md)), y solo con componentes de software libre. Cualquier cambio dentro del catálogo se registra en un ADR nuevo.

## Consecuencias
**Positivas.** El Área de Sistemas opera, respalda y da soporte con su personal; no hay costo de licencias; el equipo domina el stack.

**Negativas (costos aceptados).** Estamos limitados al catálogo aunque otras tecnologías convengan más; la capacidad de crecimiento depende de los servidores institucionales.

**Riesgos.** Que el catálogo no incluya algo necesario (p. ej. una librería de generación de PDF, [ADR-008](ADR-008-acta-plantilla-inmutable.md)). Mitigación: verificarlo en la primera semana junto con [S-09](../vision.md#s-09). Si [S-09](../vision.md#s-09) resulta falso, este ADR se reemplaza.

## Vistas que modifica
[Física](../vistas/04-fisica.md), [Procesos](../vistas/02-procesos.md)
