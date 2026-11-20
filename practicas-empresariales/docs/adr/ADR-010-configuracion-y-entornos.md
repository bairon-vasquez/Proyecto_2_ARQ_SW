# ADR-010: Configuración por variables de entorno, tres entornos y migraciones de base de datos versionadas

## Estado
Aceptado — 2026-11-17

## Contexto
[PA-05](../drivers.md#pa-05) pide decidir cómo se parametriza el sistema sin recompilar, qué entornos existen y cómo se despliega. El Área de Sistemas opera y respalda el sistema ([RT-01](../drivers.md#rt-01)); la configuración sensible (conexión a la base de datos, credenciales del SIA y del proveedor de identidad, servidor de correo) no puede vivir en el repositorio ([RN-01](../drivers.md#rn-01)). Las reglas de negocio ya son datos ([ADR-007](ADR-007-reglas-versionadas.md)); aquí se trata de la configuración técnica.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Archivos de configuración en el repositorio por entorno | Simple y versionado | Secretos expuestos; un cambio exige commit y despliegue |
| B) Variables de entorno inyectadas por el Área de Sistemas, con la imagen única para todos los entornos | Los secretos nunca están en el repositorio; misma imagen en pruebas y producción | Hay que documentar todas las variables y validarlas al arrancar |
| C) Configuración técnica en tablas de la base de datos | Editable en caliente | Mezcla secretos con datos de negocio; se complica el arranque |

## Decisión
Se elige **B**. El sistema se empaqueta como una imagen única y se despliega en tres entornos (desarrollo, pruebas con datos ficticios y producción). Al arrancar valida que estén todas las variables obligatorias y falla con un mensaje claro si falta alguna. El esquema de base de datos se versiona con migraciones aplicadas automáticamente y de forma reversible, y existe una verificación en cada Pull Request. Los adaptadores del SIA y del correo tienen una versión simulada para desarrollo.

## Consecuencias
**Positivas.** Misma imagen en todos los entornos; secretos fuera del repositorio; despliegues repetibles; el desarrollo no depende del SIA real.

**Negativas (costos aceptados).** El Área de Sistemas debe mantener las variables y los secretos en cada entorno; se debe mantener un entorno de pruebas con su base de datos.

**Riesgos.** Que una variable mal configurada llegue a producción. Mitigación: validación al arrancar y lista de verificación de despliegue.

## Vistas que modifica
[Física](../vistas/04-fisica.md)
