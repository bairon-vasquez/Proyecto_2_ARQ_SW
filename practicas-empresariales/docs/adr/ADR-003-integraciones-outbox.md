# ADR-003: Integraciones externas con adaptadores y tareas pendientes persistentes (outbox) con reintentos

## Estado
Aceptado — 2026-11-17

## Contexto
[CU-01](../drivers.md#cu-01) verifica requisitos contra los servicios del SIA ([RT-03](../drivers.md#rt-03)), que pueden fallar ([R-02](../vision.md#r-02)). [EAC-02](../drivers.md#eac-02-fiabilidad-tolerancia-a-fallos) exige 0 postulaciones perdidas, confirmación en menos de 2 s en el 95 % de los casos y verificación completada en máximo 20 minutos tras la recuperación del SIA. [PA-04](../drivers.md#pa-04) pide una única estrategia para las fallas del SIA y del correo, que también usan [CU-07](../drivers.md#cu-07) y [CU-08](../drivers.md#cu-08) para enlaces y recordatorios. La carga es baja ([S-03](../vision.md#s-03)) y el catálogo ([RT-04](../drivers.md#rt-04)) no garantiza un bróker de mensajes.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Llamada síncrona al SIA, con error al usuario si falla | Sin componentes adicionales | Si el SIA cae la postulación se pierde o hay que reintentar a mano: incumple [EAC-02](../drivers.md#eac-02) |
| B) Tabla de tareas pendientes (*outbox*) en PostgreSQL, escrita en la misma transacción, procesada por un proceso en segundo plano con reintentos | Cumple [EAC-02](../drivers.md#eac-02) con lo que ya hay ([RT-04](../drivers.md#rt-04)); atomicidad: la postulación y su tarea se guardan juntas; un solo mecanismo para SIA y correo ([PA-04](../drivers.md#pa-04)); nada nuevo que operar | Reintentos, espera creciente y cola de fallidos se programan; el sondeo agrega una latencia pequeña |
| C) Bróker de mensajes dedicado (p. ej. RabbitMQ) | Reintentos y cola de errores estándar; desacopla | Componente de infraestructura extra que operar y respaldar ([RT-01](../drivers.md#rt-01)) para una carga baja ([S-03](../vision.md#s-03), [R-04](../vision.md#r-04)); puede no estar en el catálogo ([RT-04](../drivers.md#rt-04)) |

## Decisión
Se elige **B**. Cada sistema externo (SIA, correo) se accede por un adaptador detrás de un puerto ([ADR-001](ADR-001-monolito-modular.md)). La postulación y la tarea de verificación se guardan en una sola transacción con estado "pendiente de verificación"; el estudiante recibe la confirmación de recepción de inmediato. Un proceso en segundo plano (worker) sondea las tareas cada 15 segundos, llama al SIA con tiempo máximo de 4 s y, si falla, reintenta con espera creciente (máximo 5 minutos entre intentos, lo que garantiza los 20 minutos de [EAC-02](../drivers.md#eac-02)). Agotados 8 intentos, la tarea pasa a estado "fallida" y alerta al director de programa. Se prefiere B sobre C porque, con [S-03](../vision.md#s-03), no justifica un componente más y porque la atomicidad evita perder postulaciones por una falla entre guardar y encolar.

## Consecuencias
**Positivas.** Se cumple [EAC-02](../drivers.md#eac-02); una sola estrategia para SIA y correo ([PA-04](../drivers.md#pa-04)); no se agrega infraestructura; la tarea y el dato nunca se desincronizan.

**Negativas (costos aceptados).** Hay que construir y probar el procesador de tareas; el sondeo consume la base de datos y no escala a miles de tareas por segundo; aparece un estado intermedio "pendiente de verificación" que la interfaz debe explicar.

**Riesgos.** Que la carga crezca más allá de [S-03](../vision.md#s-03). Mitigación: el procesador está detrás de un puerto; migrar a un bróker sería un ADR nuevo que reemplace a este sin tocar el dominio. Alerta si hay más de 100 tareas pendientes.

## Vistas que modifica
[Procesos](../vistas/02-procesos.md), [Desarrollo](../vistas/03-desarrollo.md), [Lógica](../vistas/01-logica.md) (entidad `TareaPendiente`)
