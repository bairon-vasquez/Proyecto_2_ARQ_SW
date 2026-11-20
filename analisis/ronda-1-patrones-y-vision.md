# Ronda 1: Patrones y Visión

**Fuentes:** `3. Patrones, vision.pdf` (diapositivas) y `Taller_Vision_Solucion_Practicas.pdf` (solución del docente).
**Nuestro entregable de esta ronda:** [`practicas-empresariales/docs/vision.md`](../practicas-empresariales/docs/vision.md)

---

## 1. Análisis de las diapositivas

### 1.1 Idea central
La arquitectura existe cuando se juntan tres condiciones: el sistema no cabe en la cabeza de una persona, varias personas trabajan en paralelo y el sistema debe durar. Responde **dividiendo, definiendo fronteras y fijando conscientemente las decisiones caras de revertir**.

### 1.2 Conceptos clave (resumen propio)

| Tema | Lo que hay que retener |
|---|---|
| Definiciones | ISO 42010 (conceptos fundamentales en elementos y relaciones), Bass/Clements/Kazman (estructuras para razonar), Fowler (lo difícil de cambiar). Común: **estructuras + relaciones + decisiones**. |
| Criterio de "arquitectónico" | Cinco preguntas: alcance, costo de reversión, visibilidad, relación con drivers, momento. Cuantas más se cumplan, más arquitectónica es la decisión. |
| Tres familias de estructuras | Módulos (código), componentes y conectores (ejecución), asignación (despliegue). De aquí nacen las vistas. |
| Ciclo de la arquitectura | Requerimientos → Diseño → Documentación → Evaluación → Implementación. **No** es el ciclo de vida del software; corre en paralelo. |
| Patrón de diseño vs. arquitectónico | Diseño = escala meso (GoF, SOLID, dentro de un módulo). Arquitectónico = escala macro (capas, hexagonal, microservicios, EDA, CQRS…). Regla: si se explica con una o dos clases es de diseño; si hace falta un diagrama del sistema, es arquitectónico. |
| Deuda técnica vs. arquitectónica | La técnica es local y detectable con análisis estático (Sonar, Pylint). La arquitectónica vive *entre* componentes (ciclos, monolito distribuido, hubs, ausencia de ADR) y se paga reescribiendo. |
| Arquitecto de soluciones | Alcance más amplio que el de software: integraciones, infraestructura, políticas y procesos. Jerarquía Enterprise > Solution > Software > Technical. |
| Visión | Documento corto (2–3 páginas) anterior a los requisitos: para qué existe el sistema, a quién le importa y con qué no se puede contar. |
| Objetivo de negocio | Responde *para qué*, no *qué hace el software*. Prueba: si no se puede decir si se cumplió o no, no es objetivo. |
| Atributo de calidad | *Qué tan bien*. Prueba: si cambiar el número obliga a rediseñar, es atributo de calidad. |
| Cadena de trazabilidad | Objetivo → atributo → escenario → decisión (ADR). |
| Stakeholders | No solo usuarios. Mínimo 6, con **al menos 3 técnicos** en el proyecto del curso. Mapa poder/interés decide a quién entrevistar primero. |
| Restricciones | Decisiones impuestas, no negociables; reducen el espacio de solución (ayudan). Técnicas vs. de negocio/organizacionales. |

### 1.3 Ejercicio de la diapositiva 20 (¿A, D o I?) — nuestras respuestas

| # | Cambio | Clase | Razón |
|---|---|---|---|
| 1 | Angular en vez de React | **A** | Cambiarlo es reescribir toda la UI; es visible para el equipo y condiciona contratación/herramientas. (Se discute: algunos lo ven "frontera"). |
| 2 | `map` en vez de `for` | **I** | Segundos/horas, un solo método. |
| 3 | JWT en vez de sesiones | **A** | Afecta a todos los componentes, escalabilidad y seguridad; cruza fronteras. |
| 4 | Reportes por cola en vez de llamada directa | **A** | Cambia el conector entre componentes (síncrono→asíncrono) y el comportamiento ante fallos. |
| 5 | Strategy para descuentos | **D** | Patrón GoF dentro de un módulo. |
| 6 | Contenedores en vez de servidor físico | **A** | Cambia la estructura de asignación y la operación. |
| 7 | `calcularTotal()` en Factura | **D** | Reparto de responsabilidades en clases. |
| 8 | Cifrado en reposo | **A** | Responde a un atributo (seguridad/ley), atraviesa persistencia, backups y llaves. |

Pregunta abierta de la diapositiva 39 (¿por qué "4 personas y 16 semanas" es restricción de negocio y no técnica?): porque la impone la organización/el curso sobre *recursos y plazo*, no sobre la tecnología; sin embargo **sí tiene impacto técnico** (descarta microservicios por costo operativo).

---

## 2. Análisis del taller resuelto por el docente (Visión)

### 2.1 Lo que pide el taller
Documento de visión completo del Sistema de Gestión de Prácticas Empresariales (500 estudiantes/año, 50 tutores, hoy en Excel y correo). Se evalúa: objetivos **medibles**, ≥3 stakeholders técnicos, restricciones **con origen declarado**, supuestos que hacen explícito lo que el enunciado no dice.

### 2.2 Estructura de la solución del docente
1. Problema → 1 párrafo con cifras (500/50), dolores (sin fuente única, actas con errores, auditoría manual).
2. 6 objetivos de negocio (OB-01…OB-06), cada uno con su atributo de calidad.
3. Alcance con lista de **SÍ** / **NO** (bolsa de empleo, convenios, ARL, firma digital certificada, carga a SIA, históricos).
4. 11 stakeholders (7 negocio/técnicos mezclados), con poder/interés y atributo implicado.
5. 9 restricciones: RT-01…RT-04 (infraestructura, SSO, SIA solo por servicios, catálogo tecnológico) y RN-01…RN-05 (Ley 1581, retención documental, formato de acta, sin cuenta para supervisores, sin licencias recurrentes).
6. 9 supuestos (S-01…S-09) y 4 riesgos (R-01…R-04).

### 2.3 Qué hace bien (patrones que replicamos)
- Los objetivos cuantifican **qué gana la Facultad** (días hábiles, %, horas) y no describen funciones.
- Cada restricción responde *quién la impone* y *por qué*, y cada una luego se vuelve driver sin transformarse.
- Los supuestos cierran huecos del enunciado con un responsable de validación (S-03: carga real de 170–250 prácticas activas → **no** justifica arquitectura distribuida; ya prepara la decisión del monolito).
- Riesgos enlazados a objetivos y con mitigación concreta.

### 2.4 Observaciones críticas
- Algunos objetivos mezclan más de un atributo de calidad en una celda y la tabla del PDF queda desalineada (OB-01/OB-02 comparten celda de atributo): conviene una fila = un objetivo = un atributo principal.
- "Reducir 50% las horas del docente" depende de una línea base que S-08 admite que **no existe**; es medible solo si se levanta la encuesta *antes*. Lo registramos como acción en nuestro supuesto de líneas base.
- Los stakeholders técnicos aparecen pero sin separar visualmente negocio/técnico en la tabla; en el nuestro se ordena por tipo.
- Falta un stakeholder **auditor/acreditación** como actor propio (aparece solo en el objetivo OB-06). Lo agregamos.
- La visión da por sentado el catálogo institucional (RT-04) sin decir cuál es; lo tratamos como supuesto a validar con el Área de Sistemas.

---

## 3. Nuestra versión: decisiones de diferencia

Mantuvimos la plantilla (6 secciones, 2–3 páginas) pero tomamos decisiones propias:

| Aspecto | Docente | Nuestra versión |
|---|---|---|
| Objetivos | 6 | **7** (se agrega visibilidad en tiempo casi real del estado, OB-07) |
| Meta de acta | ≤5 días hábiles | ≤**3** días hábiles (más ambiciosa, factible al no depender de firma digital) |
| Stakeholders | 11 | 12, con **auditor/acreditación** y un usuario ocasional de consulta; 4 técnicos explícitos, la tabla ordenada por tipo |
| Supuestos | 9 | 10 (se explicita el catálogo tecnológico supuesto, S-09, y la encuesta de línea base, S-08) |
| Riesgos | 4 | 5 (se añade resistencia al cambio de los docentes asesores, R-05) |
| Alcance | Igual en lo esencial | Se añade la *migración de prácticas en curso* como ítem explícito del SÍ y el seguimiento/consolidado para auditoría |

➡️ Ver el documento final en [`docs/vision.md`](../practicas-empresariales/docs/vision.md).
