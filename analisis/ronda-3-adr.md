# Ronda 3: ADR (Registro de Decisión Arquitectónica) y documentación como código

**Fuentes:** `5. ADR Registro de Decisión Arquitectónica.pdf` y `Taller_ADR_Solucion_Practicas.pdf`.
**Nuestro entregable:** [`practicas-empresariales/docs/adr/`](../practicas-empresariales/docs/adr/) (ADR-001 a ADR-010)

---

## 1. Análisis de las diapositivas

### 1.1 Por qué documentar decisiones
Sin ADR, a los 14 meses nadie sabe por qué el pago va por cola; la decisión se vuelve permanente por miedo o se cambia sin saber por qué existía. Se documentan **tres cosas**: vistas (cómo está estructurado), decisiones (qué se decidió) y **razón** (por qué eso y no otra cosa). La tercera es la única irrecuperable.

### 1.2 Plantilla del ADR
`# ADR-00X: título en forma de decisión` → **Estado** (Propuesto/Aceptado/Rechazado/Obsoleto/Reemplazado por) → **Contexto** (con drivers por ID) → **Alternativas** (con pros y contras) → **Decisión** (se elige X *porque* driver) → **Consecuencias** (positivas, negativas y costos, riesgos).

### 1.3 Tres reglas de oro
1. **Un ADR por decisión.**
2. **No se editan ni se borran**: si cambia, un ADR nuevo reemplaza al anterior.
3. Viven en el repositorio (`docs/adr/`) y entran en el mismo Pull Request que el cambio.

### 1.4 De dónde sale un ADR
Driver(es) → pregunta de diseño → opciones → elección. **Siempre empieza por el driver, nunca por la tecnología.** Todo driver debe quedar cubierto por al menos un ADR. También surgen de: inicio del proyecto, una restricción, algo transversal, o una decisión anterior que deja de servir. Criterio: ¿es importante y difícil de cambiar? Si sí, se registra aunque haya una sola opción.

### 1.5 Qué mirar en el ejemplo (ADR-001 firma asíncrona)
El contexto cita drivers por ID; la alternativa descartada se documenta (evita reabrirla); las **consecuencias negativas se escriben sin maquillaje** (un ADR solo con ventajas es deshonesto). Traza completa: objetivo → atributo → drivers → pregunta → alternativas → decisión.

### 1.6 Documentación como código
- Estructura `docs/{vision,drivers,arquitectura}.md`, `adr/`, `diagramas/`, `src/`.
- Formatos versionables: `.puml`, Mermaid, Structurizr, D2 (texto → diff legible); `.drawio`/`.excalidraw` parcial; `.png`, `.vsdx`, Lucidchart **no**.
- Herramienta del curso: PlantUML (extensión de VS Code); Mermaid para cosas simples en README.
- Errores a evitar: qué sin el porqué, un solo diagrama gigante, documentar al final, herramientas que no versionan, **editar ADR retroactivamente**, copiar la especificación.
- Markdown mínimo para `vision.md` y `drivers.md`.

### 1.7 Estructura mínima del documento de arquitectura
Introducción y objetivos · Restricciones · Contexto · Estrategia · Vistas · Conceptos transversales · Decisiones (índice ADR) · Requisitos de calidad · Riesgos y deuda técnica. (Adaptación de arc42; en SDD se amplía a 10 secciones con glosario.)

---

## 2. Análisis del taller resuelto por el docente

### 2.1 Lo que pide
Parte 1: ADR que cubran **todos** los drivers (CU primarios, EAC, restricciones, PA), plantilla completa, ≥2 alternativas (o justificar si la impone una restricción), un ADR por decisión, decisión justificada por drivers. Parte 2: repositorio con `vision.md`, `drivers.md`, `adr/`, `arquitectura.md` (secciones 1, 2, 7 y 8; el resto "pendiente"), `diagramas/` y `src/` con `.gitkeep`. Se evalúa: estructura, **mismos IDs** en drivers y ADR, `arquitectura.md` que enlace en vez de copiar.

### 2.2 Qué entregó el docente (9 ADR para 22 drivers)

| ADR | Decisión | Drivers principales |
|---|---|---|
| 001 | Monolito modular con puertos y adaptadores | PA-01, EAC-01, S-03, R-04 |
| 002 | Plataforma e infraestructura institucional (impuesta) | RT-01, RT-04, RN-05 |
| 003 | Adaptadores + **cola de mensajes con bróker dedicado** y reintentos | CU-01, EAC-02, PA-04, RT-03 |
| 004 | SSO + enlaces de un solo uso | RT-02, RN-04, EAC-03, PA-02 |
| 005 | Autorización por roles en los casos de uso | PA-02, RN-01, CU-10 |
| 006 | Bitácora de solo inserción en BD | PA-03, OB-06, EAC-03, RN-02 |
| 007 | Reglas por programa como configuración con vigencia | CU-12, OB-05, EAC-01 |
| 008 | Acta desde plantilla externa, PDF inmutable | CU-09, CU-10, RN-02, RN-03 |
| 009 | Migración con plantilla normalizada y script único | PA-05, CU-15 |

### 2.3 Qué hace bien
- Cita drivers por ID en cada contexto y mantiene la cadena de trazabilidad.
- ADR-002 es el modelo de "decisión impuesta": lista lo descartado y por qué restricción.
- Consecuencias negativas reales y **riesgos con mitigación** medible (alertas de 100 mensajes, etc.).
- Elige explícitamente contra la intuición de carga baja con razones (PA-04 una sola estrategia).

### 2.4 Observaciones críticas
- **ADR-003 es la decisión más discutible.** Admite que la carga es baja (S-03) y que un bróker es "un componente más que operar" (RT-01, R-04), pero lo elige igual; además su propio riesgo reconoce que el catálogo (RT-04) quizá no lo incluya. Con la alternativa B (tabla de tareas + tarea programada) se cumple EAC-02 sin infraestructura nueva. Es una tensión entre sus propios ADR (el 001 aboga por simplicidad y el 003 la rompe).
- El ADR-002 posterga la tecnología concreta ("se registrará en un ADR posterior"), pero ningún ADR posterior aparece: queda una decisión pendiente sin ID.
- No existe ADR para la **configuración técnica y entornos** (en drivers no hay PA para ello, pero el SDD lo reclama después: AGENTS.md y despliegue).
- Los ADR no indican **qué vistas modifican**, algo que la siguiente unidad (vistas) exige explícitamente.
- Los estados llevan fecha única (26-oct-2026) para todos: bien para un taller, pero oculta la historia que el método valora.
- EAC-01 y OB-05 se cubren en ADR-001 y ADR-007, pero no hay un ADR sobre cómo se **prueba** la regla de dependencia entre módulos (se menciona solo "revisar en cada PR").

---

## 3. Nuestra versión: decisiones de diferencia

| Tema | Docente | Nuestra versión | Razón |
|---|---|---|---|
| N.º de ADR | 9 | **10** | Se agrega ADR-010 (configuración y entornos) para PA-05 |
| Integraciones asíncronas | Bróker dedicado (ADR-003 opción C) | **Outbox transaccional en PostgreSQL** + worker (opción B) | Cumple EAC-02 sin infraestructura nueva (RT-04, R-04); atomicidad guardar+encolar. Dejamos la salida a un bróker como ADR futuro |
| Acta | Una sola decisión (plantilla + inmutable) | Misma decisión, pero se documenta la alternativa **D (asíncrona)** y se justifica **síncrona** con EAC-04 | Antes no había un driver de desempeño que la sostuviera |
| Migración | Script único (PA-05) | Comando con **dry-run** y reporte previo a la carga real (CU-15 primario) | Mitiga el riesgo que lo hizo primario |
| Bitácora | Solo inserción | Solo inserción + **hash encadenado** y partición por periodo | Detecta alteración y acelera OB-06 |
| Autorización | Roles + pertenencia | Igual + **negación por defecto** y prueba que falla si hay casos de uso sin rol | Convierte la mitigación en verificación |
| Vistas | No se enlazan | Cada ADR incluye **"Vistas que modifica"** | Requisito de la ronda 4 |
| ADR posterior prometido | Sin ID | El stack se fija en ADR-002 (condicionado a S-09) | No dejar decisiones sin registro |

## 4. Matriz de cobertura driver → ADR

| Driver | ADR |
|---|---|
| CU-01 | 003 |
| CU-07 | 004, 003 |
| CU-09 | 008 |
| CU-10 | 008, 005 |
| CU-12 | 007 |
| CU-15 | 009 |
| EAC-01 | 001, 007 |
| EAC-02 | 003 |
| EAC-03 | 004, 006 |
| EAC-04 | 008 |
| RT-01 | 002 |
| RT-02 | 004 |
| RT-03 | 003, 001 |
| RT-04 | 002 |
| RN-01 | 005 |
| RN-02 | 006, 008 |
| RN-03 | 008 |
| RN-04 | 004 |
| RN-05 | 002 |
| PA-01 | 001 |
| PA-02 | 004, 005 |
| PA-03 | 006 |
| PA-04 | 003 |
| PA-05 | 010 |

Los 24 drivers quedan cubiertos por al menos un ADR; ningún ADR se queda sin driver.

## 5. Estructura del repositorio (parte 2 del taller)

```
practicas-empresariales/
├── docs/
│   ├── vision.md  drivers.md  contexto.md  arquitectura.md
│   ├── adr/  ADR-001 … ADR-010
│   ├── vistas/   01-logica … 04-fisica, matriz-cobertura
│   └── diagramas/ (*.puml, secuencias/)
├── specs/001-postularse/
├── prompts/  AGENTS.md
└── src/
```
