# Ronda 5: SDD (Spec Driven Development)

**Fuente:** `7. SDD (Spec Driven Development).pdf` (no hay solución del docente; el taller se resuelve sobre el repositorio de las rondas anteriores).
**Nuestro entregable:** [`arquitectura.md`](../practicas-empresariales/docs/arquitectura.md), [`AGENTS.md`](../practicas-empresariales/AGENTS.md), [`prompts/`](../practicas-empresariales/prompts/) y [`specs/001-postularse/`](../practicas-empresariales/specs/001-postularse/)

---

## 1. Análisis de las diapositivas

### 1.1 Qué es SDD
Se describe con claridad *qué* debe hacer el software **antes** de generar el código; la especificación es el **contrato** para la IA y la **fuente de verdad** (si código y spec no coinciden, se revisa el código). Formato: Markdown en carpetas con estructura definida.

| Nivel | Qué se edita | Riesgo |
|---|---|---|
| Spec-first | El código; la spec puede quedar vieja | Documentación se pierde |
| **Spec-anchored** | Ambos, en el mismo cambio | Exige disciplina |
| Spec-as-source | Solo la spec | Hoy solo viable con herramientas que garanticen calidad |

### 1.2 Por qué SDD
Vibe coding (el contexto vive en una conversación), prompt engineering (en muchas conversaciones) y SDD (**en archivos del repositorio**). El problema no es la IA: es dejar el contexto dentro de una conversación.

### 1.3 Cinco fases (la persona o la IA lidera; ninguna termina sin revisión humana)

| Fase | Produce | Lo que verifica la persona | Si se omite |
|---|---|---|---|
| 1 Especificar | `spec.md` (Gherkin) | ¿Cada escenario se comprueba con sí/no? | Se construye algo que nadie pidió |
| 2 Planear | `plan.md` | ¿Respeta ADR y vistas, sin inventar? | Se rompe la arquitectura sin decidirlo |
| 3 Descomponer | `tasks.md` | ¿Tareas pequeñas y completas? | Tareas imposibles de revisar |
| 4 Implementar | Código | ¿Solo toca lo de la tarea y se entiende? | Código que nadie sabe explicar |
| 5 Validar | `validacion.md` | ¿Cada escenario tiene evidencia? | Darlo por bueno sin evidencia |

### 1.4 El documento de arquitectura (arc42 adaptado)
Un solo `arquitectura.md` que **enlaza, no copia** (un dato en dos lugares termina diciendo dos cosas). Diez secciones; la sección 8 tiene la columna **"Se verifica en"** que conecta cada EAC con un escenario de spec: *un EAC sin spec queda en evidencia*. Faltaban 9 (riesgos y deuda técnica) y 10 (glosario / lenguaje ubicuo con el nombre en el código).

### 1.5 Anatomía del repositorio SDD
`AGENTS.md` (reglas permanentes, corto, enlaza docs) · `docs/` · `specs/NNN-nombre/{spec,plan,tasks,validacion}.md` · `prompts/{0-arranque,1…5}.md` · `src/`. **Nueve pasos:** dos una sola vez (arquitectura.md, AGENTS.md + prompts) y el resto por funcionalidad (crear carpeta → especificar → planear → descomponer → implementar → validar → siguiente). Primero los CU del cuadrante "atender primero". El mensaje de arranque se pega tal cual y solo cambia la última línea; **una sesión nueva por fase y por tarea**.

### 1.6 Gherkin
`Característica / Escenario / Dado / Cuando / Entonces / Y / Pero`, con `# language: es`. Flujo básico = escenario principal; cada flujo alterno o excepción = un escenario; cada EAC = un escenario con su medida; la traza va en un comentario. **No** lleva pantallas, campos, clases, tablas ni tecnologías. Lo que falta se marca `[NECESITA ACLARACIÓN]`.

### 1.6 Compuertas y errores frecuentes
Una sesión por fase, revisión y commit al cierre, una tarea = un commit, si cambia el comportamiento primero `spec.md`, no editar los prompts por funcionalidad. Riesgos: specs muy largas, demasiado detalle técnico, especificar todo desde el inicio (cascada disfrazada), aceptar sin leer, deriva spec–código.

### 1.7 Herramientas
Método del curso ("a pedal") vs. GitHub Spec Kit (`/speckit.constitution|specify|clarify|plan|tasks|analyze|implement|converge`), Kiro, OpenSpec, Tessl (spec-as-source). Lo que no cambia: `docs/`, trazabilidad por IDs, compuertas humanas y defensa del código.

### 1.8 "Dónde se cortó la cadena" (certificados)
Cada decisión documentada (Angular, Docker, PostgreSQL, RabbitMQ, autenticación, API REST, pruebas) no llegó al código porque ninguna spec ni tarea lo pidió y `AGENTS.md` lo prohibía o lo excluía. **Moraleja:** lo que no está en AGENTS.md, plan.md y tasks.md no se construye; lo que está en AGENTS.md como prohibición, no se construye aunque el ADR lo pida.

---

## 2. Análisis del taller (enunciado)

### 2.1 Qué pide
**Parte 1:** `arquitectura.md` con 10 secciones; `AGENTS.md`; `prompts/`; columna "Se especifica en" en `drivers.md`; `specs/001-postularse/spec.md` (CU-01 en Gherkin con ≥3 escenarios: básico, alterno, EAC); `plan.md` que cite ADR y componentes de la vista de desarrollo; `tasks.md` pequeñas, ordenadas, trazables y **una clase/archivo por tarea**.
**Parte 2:** implementar tarea por tarea con el agente de su elección, un commit por tarea con el ID, `validacion.md` con evidencia y revisión de la regla de dependencia, defensa en clase. **No se piden pruebas automatizadas.**

### 2.2 Observaciones críticas
- **Inconsistencia de nombre:** el enunciado habla de "CU-01 *Postularse a una oferta*"; en la visión y los drivers es "*Postularse a la práctica empresarial*" (la plaza se consigue fuera, S-04). Usamos el segundo, que es el coherente con el alcance.
- **Cascada disfrazada:** el propio material advierte contra especificar todo antes de codificar; aquí ya hay visión, drivers, 10 ADR, 4 vistas y 6 secuencias antes de la primera tarea. Se mitiga especificando **solo** CU-01.
- **Ambigüedad "sin pruebas":** el taller no pide pruebas automáticas y el ejemplo de certificados mostraba que `AGENTS.md` que las prohibía rompió la cadena. Nuestro `AGENTS.md` las **permite** y la validación sigue siendo por escenario.
- **Riesgo de adaptadores en memoria:** "en esta etapa adaptadores en memoria" deja sin construir PostgreSQL, SIA real y el worker; es explícito en el plan como fuera de alcance, pero deja ADR-003 sin implementar. Es deuda consciente.
- La columna "Se verifica en" revela que de 4 EAC solo uno (EAC-02) tiene spec con CU-01; los demás quedan "pendientes" hasta especificar sus CU. Es una señal de que el resto de funcionalidades (CU-07, 09, 12) deben ir en la siguiente iteración.

---

## 3. Nuestra versión: decisiones de diferencia

| Tema | Decisión | Razón |
|---|---|---|
| `arquitectura.md` | 10 secciones con 4 ADR de más riesgo en la sección 9 (RA-01…RA-04) y 3 deudas (DT-01…DT-03) | La sección 9 lista lo "que ya se sabe que está mal" |
| Sección 8 | "Se verifica en" marca EAC sin spec como **pendiente** | Hace visible el hueco, como pide la diapositiva |
| Glosario | 15 términos con su nombre en el código | Lenguaje ubicuo; los nombres de clases en tasks.md salen de aquí |
| `AGENTS.md` | Permite `pytest`; adaptadores en memoria; "no cambiar docs ni prompts sin que lo pida la persona" | Evita el corte de cadena de los certificados |
| Prompts | 0 a 5 propios, cada uno con *lee / produce / reglas / detente* | Tres reglas repetidas: no inventar, no adelantar, detenerse |
| spec.md | **8 escenarios** (1 básico, 6 alternos/excepciones, EAC-02 y reintentos agotados) en Gherkin | El taller exige ≥3 |
| plan.md | Cita ADR 001, 002, 003, 005, 006, 007 y componentes de la vista de desarrollo | Sin inventar componentes |
| tasks.md | **14 tareas**, un archivo por tarea, de adentro hacia afuera, con tabla de cobertura de escenarios | Exigencia de trazabilidad |
| validacion.md | Esqueleto en estado **pendiente** | No se marca "Cumple" sin evidencia; el código no se ha implementado aún |

## 4. Cadena de trazabilidad resultante

```
Visión (OB-01, S-03, R-02)
  → Drivers (CU-01, EAC-02, RT-03)
    → ADR (001, 003, 005, 006, 007)
      → Vistas (procesos: Procesador de tareas; desarrollo: módulo Postulaciones)
        → spec 001 (8 escenarios) → plan → T-01…T-14 → validacion
```

## 5. Siguientes pasos para la parte 2 del taller
1. Repetir los pasos 4–6 ya hechos y, en una **sesión nueva por tarea**, ejecutar `prompts/4-implementar.md` de T-01 a T-13 con el mensaje de arranque.
2. Un commit por tarea (`T-xx …`).
3. Ejecutar `prompts/5-validar.md` (T-14) y llenar `validacion.md`.
4. Si un escenario falla: tarea nueva (código) o corregir primero `spec.md` (especificación).
