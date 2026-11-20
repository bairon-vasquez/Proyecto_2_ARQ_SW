# Ronda 4: Vistas arquitectónicas (4+1, C4 y secuencias)

**Fuente:** `6. Vistas arquitectonicas.pdf` (no hay solución del docente para este taller; solo el enunciado, con el caso de los certificados como ejemplo).
**Nuestro entregable:** [`contexto.md`](../practicas-empresariales/docs/contexto.md), [`vistas/`](../practicas-empresariales/docs/vistas/) y [`diagramas/`](../practicas-empresariales/docs/diagramas/)

---

## 1. Análisis de las diapositivas

### 1.1 Por qué varias vistas
Un diagrama único mezcla clases, servidores, colas y personas y no sirve a nadie. Varias vistas: cada una responde la pregunta de un grupo de stakeholders, es pequeña y se actualiza sola. Vocabulario ISO 42010: **stakeholder → preocupación → punto de vista (plantilla) → vista (aplicación) → modelo/diagrama**. Una vista que no responde ninguna preocupación es "documentación de adorno". Estructura (lo que existe) ≠ vista (representación para una preocupación) ≠ diagrama (dibujo concreto).

### 1.2 Las tres familias de estructuras

| Familia | Qué muestra | Sirve a |
|---|---|---|
| Módulos | Estático: descomposición, usos, capas, clases | Desarrollo y mantenimiento |
| Componentes y conectores | Dinámico: procesos, servicios, BD, colas; **el conector pesa tanto como el componente** | Desempeño, disponibilidad, seguridad |
| Asignación | Despliegue, implementación (archivos), asignación de trabajo | Operación e infraestructura |

Ejercicio rápido de las diapositivas (quién pregunta determina la familia): servidores → asignación (despliegue); cambiar motor → módulos (usos/capas); qué pasa si el proveedor no responde → C&C; responsable del módulo → asignación (trabajo); ¿dominio depende de infraestructura? → módulos (capas); protocolo web–API → C&C.

### 1.3 Modelo 4+1 (Kruchten)
Cuatro vistas + escenarios que las recorren y validan:

| Vista | Para | Se dibuja con |
|---|---|---|
| Lógica | Usuarios finales, analistas | UML: modelo de dominio (C4 no aplica) |
| Procesos | Integradores | C4 nivel 2 (contenedores) |
| Desarrollo | Programadores | C4 nivel 3 (componentes) + vista de usos |
| Física | Ingenieros de infraestructura | C4 despliegue |
| +1 Escenarios | Validar | Diagramas de secuencia **arquitectónicos** |

Contexto (C4 nivel 1) **no es** una vista de 4+1: las encuadra. Un escenario por cada CU primario (máx. 6) + uno por cada EAC no cubierto; si un escenario no se puede recorrer, falta o está mal una vista.

### 1.4 C4
Cuatro niveles (Contexto, Contenedores, Componentes, Código) como zoom de mapa. Abstracciones: persona, sistema, contenedor (**no es Docker**: todo lo que se ejecuta o guarda datos por separado), componente, código. Define *qué* se dibuja y cómo rotular (nombre, tipo, tecnología, descripción).

### 1.5 Una vista documentada tiene cinco partes
Presentación principal · catálogo de elementos · justificación (drivers y ADR) · comportamiento · vistas relacionadas. **Un diagrama es solo la parte 1.**

### 1.6 Trazabilidad
Cada ADR dice qué vistas modifica; cada vista dice qué drivers atiende; matriz de cobertura sin filas vacías. Modelo de dominio ≠ diagrama de clases del diseño (nivel y propósito distintos).

### 1.7 Diagramas de secuencia arquitectónicos
Participantes = contenedores/componentes (no clases); mensajes = HTTP, colas, SQL. Fragmentos: **alt** (excluyente), **opt**, **loop** (siempre con máximo), **par**, **break** (a diferencia de alt, el escenario termina). Se escribe en 5 pasos: elegir → participantes de la vista de procesos → flujo principal → flujos alternos → verificar que se ve la decisión del ADR y se cumple el EAC. **Sin IA** primero.

### 1.8 Repositorio
`docs/contexto.md`, `vistas/01-logica…04-fisica.md`, `diagramas/*.puml` con el mismo nombre, `diagramas/secuencias/cuNN-nombre.puml` y tabla de escenarios en `drivers.md`.

---

## 2. Análisis del taller (enunciado)

### 2.1 Qué pide
**Parte 1:** contexto C4-1; vista lógica UML sin tipos ni métodos; contenedores; componentes con capas de Clean Architecture y **vista de usos sin ciclos**; despliegue sobre infraestructura institucional; cada vista con catálogo, justificación y vistas relacionadas; matriz de cobertura.
**Parte 2:** tabla de escenarios (uno por CU primario + EAC sin cubrir), un secuencia por escenario sin IA, participantes con los mismos nombres de la vista de procesos, fragmentos con guardas, recorrido de validación.
**Parte 3:** todo versionado como texto.
Se evalúa: cada decisión de ADR se ve en alguna vista (p. ej. el bróker del ADR-003); RT-01 verificable en la física; nombres idénticos; toda flecha con verbo y protocolo; el contexto es caja negra; matriz sin filas vacías; **EAC-02 visible (qué pasa cuando el SIA no responde)**.

### 2.2 Observaciones críticas sobre el material
- El enunciado del taller habla del "bróker del ADR-003" como si fuera obligatorio en la solución, ligando la ronda 4 a la decisión más discutible de la ronda 3. En nuestra versión el equivalente es la tabla de tareas del ADR-003 y se ve en procesos y lógica.
- Las diapositivas usan el caso de los certificados con numeración distinta a la de prácticas (ADR-001 firma, ADR-002 estructura, ADR-003 persistencia) mientras la solución del docente tiene ADR-001 monolito, 002 plataforma y 003 cola. Hay que reasignar los números al "traducir" ejemplos.
- El diagrama de contexto de las diapositivas muestra el *contexto* con nombres de tecnologías (Angular, RabbitMQ) solo en niveles 2 y 3; en el 1 no, bien. Pero el catálogo del ejemplo mezcla "Aplicación web: Angular" con responsabilidades: conviene separar siempre responsabilidad de tecnología.
- La matriz de cobertura del ejemplo tiene filas con pocas marcas y ADR con una sola vista (p. ej. ADR-002 solo en desarrollo): válido, pero la regla "cada ADR se ve en alguna vista" se cumple por poco.
- El taller exige "Participantes con el mismo nombre": exige un glosario de nombres único, que se anticipa en la sección 10 de `arquitectura.md` (ronda 5).

---

## 3. Nuestra versión: decisiones de diferencia

| Tema | Decisión propia | Razón |
|---|---|---|
| Notación | PlantUML con C4 estándar (`!include <C4/...>`) y Mermaid solo para la vista de usos | Texto versionable (diff legible) |
| Procesos | 6 contenedores: web, API, **Procesador de tareas**, PostgreSQL, almacenamiento de documentos, **Comando de migración** | Hace visible ADR-003 y ADR-009 |
| Sin bróker | Cola = tabla `TareaPendiente` | Coherente con ADR-003 de nuestra versión y con RT-04 |
| Desarrollo | Un solo código para API, Procesador y Comando; módulos por capacidad; vista de usos explícita sin ciclos | Cumple "sin ciclos" y deja claro dónde está cada adaptador |
| Lógica | 15 entidades con `VersionReglas`, `EnlaceAcceso`, `TareaPendiente`, `RegistroBitacora` | Refleja ADR-004, 003, 006 y 007 en la vista lógica |
| Física | Estación de administración para el comando de migración, 3 entornos en texto | RT-01 y ADR-010 |
| Escenarios | **6** (uno por cada CU primario), los 4 EAC quedan cubiertos | Evita escenarios sin driver |
| Verificación | Matriz de cobertura + **tabla de recorrido** por escenario | Valida que ningún escenario quede sin camino |

⚠️ Los `.puml` se escribieron sin renderizarlos; se recomienda abrirlos con la extensión PlantUML de VS Code y ajustar si el motor marca algún error de sintaxis.

➡️ Entregables: [`contexto.md`](../practicas-empresariales/docs/contexto.md), [`vistas/matriz-cobertura.md`](../practicas-empresariales/docs/vistas/matriz-cobertura.md).
