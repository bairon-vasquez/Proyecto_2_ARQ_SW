# ADR-005: Autorización por roles centralizada en los casos de uso

## Estado
Aceptado — 2026-11-17

## Contexto
[PA-02](../drivers.md#pa-02) exige controlar los permisos de cinco roles: estudiante, docente asesor, director de programa, supervisor y administrador. [RN-01](../drivers.md#rn-01) (Ley 1581 de 2012) obliga a restringir el acceso a datos personales según su finalidad, a registrar la autorización de tratamiento y a cifrar en tránsito. [CU-10](../drivers.md#cu-10) exige que solo el docente asesor y el director aprueben el acta.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Verificar permisos en cada pantalla o controlador | Rápido de empezar | Reglas dispersas; una ruta sin verificación expone datos personales ([RN-01](../drivers.md#rn-01)) |
| B) Política de autorización por rol centralizada, aplicada en cada caso de uso, con verificación de pertenencia | Una regla por permiso, fácil de revisar y probar; el docente solo ve a sus practicantes | Hay que actualizar la política con cada caso de uso nuevo |
| C) Control de acceso por atributos con un motor de políticas | Muy flexible | Complejidad que cinco roles fijos no exigen ([R-04](../vision.md#r-04)); componente adicional |

## Decisión
Se elige **B**. Cada caso de uso declara el rol que puede ejecutarlo y verifica que el dato pertenezca al usuario (p. ej. que la práctica sea de un practicante de ese docente). La tabla de permisos vive en un solo lugar del módulo de aplicación y el acceso se **niega por defecto** a todo caso de uso sin rol declarado. Todo el tráfico va por HTTPS; la postulación registra la autorización de tratamiento de datos del estudiante.

## Consecuencias
**Positivas.** El cumplimiento de [RN-01](../drivers.md#rn-01) se puede verificar; los permisos están en un solo lugar; la aprobación del acta queda restringida a los roles de [CU-10](../drivers.md#cu-10).

**Negativas (costos aceptados).** Cada caso de uso nuevo obliga a actualizar la política; cambiar un permiso exige despliegue.

**Riesgos.** Que un caso de uso nuevo quede sin rol. Mitigación: negación por defecto y una prueba que falla si hay casos de uso sin rol.

## Vistas que modifica
[Desarrollo](../vistas/03-desarrollo.md), [Lógica](../vistas/01-logica.md)
