# Vista de procesos: contenedores

Para: integradores del sistema. Notación: C4 nivel 2. Un contenedor es cualquier cosa que se ejecuta o guarda datos por separado.

## 1. Presentación principal

Diagrama: [../diagramas/02-procesos.puml](../diagramas/02-procesos.puml).

## 2. Catálogo de elementos

| Elemento | Responsabilidad | Tecnología | Se comunica con |
|---|---|---|---|
| Aplicación web | Interfaz de estudiantes, docentes, directores y supervisores | Angular | API de prácticas (JSON / HTTPS) |
| API de prácticas | Casos de uso, reglas, autorización y generación de actas (monolito modular) | Python | Aplicación web; PostgreSQL (SQL); Almacenamiento de documentos; Proveedor de identidad (OIDC) |
| Procesador de tareas | Consulta al SIA y envía correos con reintentos; sondea tareas pendientes | Python (mismo código que la API) | PostgreSQL (SQL); SIA (HTTPS); Servicio de correo (SMTP) |
| PostgreSQL | Prácticas, reglas, tareas pendientes y bitácora | PostgreSQL | API, Procesador de tareas y Comando de migración (SQL) |
| Almacenamiento de documentos | Actas aprobadas en PDF, inmutables | Almacenamiento institucional | API de prácticas |
| Comando de migración | Carga única de prácticas en curso desde Excel | Python, CLI | PostgreSQL (por los casos de uso del dominio) |

## 3. Justificación

- [EAC-02](../drivers.md#eac-02) y [ADR-003](../adr/ADR-003-integraciones-outbox.md): el Procesador de tareas separa la consulta al SIA de la petición del estudiante; la tabla de tareas en PostgreSQL es el conector asíncrono.
- [RN-01](../drivers.md#rn-01)/[EAC-01](../drivers.md#eac-01) y [ADR-001](../adr/ADR-001-monolito-modular.md): una sola API como monolito modular.
- [RT-02](../drivers.md#rt-02), [RT-04](../drivers.md#rt-04) y [ADR-002](../adr/ADR-002-plataforma-institucional.md), [ADR-004](../adr/ADR-004-autenticacion-dual.md): PostgreSQL institucional; solo la API habla con el proveedor de identidad.
- [RT-03](../drivers.md#rt-03): solo el Procesador de tareas habla con el SIA.
- [EAC-03](../drivers.md#eac-03)/[PA-03](../drivers.md#pa-03) y [ADR-006](../adr/ADR-006-bitacora-auditoria.md): la bitácora vive en PostgreSQL.
- [EAC-04](../drivers.md#eac-04) y [ADR-008](../adr/ADR-008-acta-plantilla-inmutable.md): el acta se genera dentro de la API, sin cola; se guarda en almacenamiento aparte ([RN-02](../drivers.md#rn-02)).
- [CU-15](../drivers.md#cu-15) y [ADR-009](../adr/ADR-009-migracion-inicial.md): Comando de migración puntual.

## 4. Comportamiento

[ESC-01](../diagramas/secuencias/cu01-postularse.puml) (loop de reintentos, alt), [ESC-02](../diagramas/secuencias/cu07-evaluar-practicante.puml) (alt de enlace inválido), [ESC-03](../diagramas/secuencias/cu09-generar-acta.puml), [ESC-04](../diagramas/secuencias/cu10-aprobar-acta.puml), [ESC-06](../diagramas/secuencias/cu15-migrar-practicas.puml).

## 5. Vistas relacionadas

- [Contexto](../contexto.md): de dónde vienen actores y sistemas externos.
- [Física](04-fisica.md): en qué nodo corre cada contenedor.
- [Desarrollo](03-desarrollo.md): cómo se organiza por dentro la API.
