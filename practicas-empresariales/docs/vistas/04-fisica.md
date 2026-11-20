# Vista física: despliegue

Para: ingenieros de infraestructura. Notación: diagrama de despliegue de C4.

## 1. Presentación principal

Diagrama: [../diagramas/04-fisica.puml](../diagramas/04-fisica.puml). Todo corre en el centro de datos de la Universidad.

## 2. Catálogo de elementos

| Nodo | Contenedores que aloja | Características | Conexiones |
|---|---|---|---|
| Servidor web (Linux, Nginx) | Aplicación web | Sirve los archivos estáticos de la interfaz | Navegadores de los usuarios (HTTPS) |
| Servidor de aplicaciones (Linux, Docker) | API de prácticas, Procesador de tareas | Cada contenedor se reinicia y escala por separado | Servidor web (HTTPS), PostgreSQL (SQL), almacenamiento, SIA (HTTPS), correo (SMTP), IdP (OIDC) |
| Servidor de base de datos | PostgreSQL | Solo accesible desde la red interna; respaldo diario con restauración probada | API, Procesador y Comando (SQL) |
| Almacenamiento institucional | Almacenamiento de documentos | En el país, dentro del centro de datos; solo lectura tras escribir | API de prácticas |
| Estación de administración | Comando de migración | Acceso restringido; se usa una sola vez | PostgreSQL |

Entornos ([ADR-010](../adr/ADR-010-configuracion-y-entornos.md)): desarrollo, pruebas (datos ficticios) y producción, con la misma imagen y variables de entorno distintas.

## 3. Justificación

- [RT-01](../drivers.md#rt-01): todos los nodos están en la infraestructura institucional; no hay nube pública.
- [RN-01](../drivers.md#rn-01) y [RN-02](../drivers.md#rn-02): los datos personales y los PDF no salen del país; las actas aprobadas se conservan según retención.
- [ADR-002](../adr/ADR-002-plataforma-institucional.md): plataforma institucional; [ADR-003](../adr/ADR-003-integraciones-outbox.md): sin bróker, no hay un nodo de mensajería que operar; [ADR-008](../adr/ADR-008-acta-plantilla-inmutable.md): almacenamiento separado para PDF; [ADR-010](../adr/ADR-010-configuracion-y-entornos.md): entornos y configuración.
- [RT-04](../drivers.md#rt-04): PostgreSQL institucional.
- [EAC-04](../drivers.md#eac-04): CPU del servidor de aplicaciones por debajo de 70 % en el cierre; se monitorea con el Área de Sistemas.

## 4. Comportamiento

La secuencia de [CU-10](../drivers.md#cu-10) cruza nodos: API y almacenamiento por la red interna; el aviso por correo sale por SMTP institucional. Ver [ESC-04](../diagramas/secuencias/cu10-aprobar-acta.puml).

## 5. Vistas relacionadas

- [Procesos](02-procesos.md): cada contenedor aparece en un nodo de esta vista.
- [Contexto](../contexto.md): cada sistema externo aparece con su protocolo.
