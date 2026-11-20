# Fase 1: Especificar

**Lee:** `AGENTS.md`, `docs/arquitectura.md` y, en `docs/drivers.md`, la fila del caso de uso indicado y los EAC que lo tocan.

**Produce:** `specs/<NNN>-<nombre>/spec.md` en Gherkin (`# language: es`):
- Cabecera de traza: `# Traza: CU-xx, EAC-xx, ADR-xxx`.
- Un `Escenario` por el flujo básico, uno por cada flujo alterno o excepción y uno por cada EAC que toca el caso de uso, con su medida.
- Sin pantallas, campos, clases, tablas ni tecnologías: eso es diseño y va en `plan.md`.

**Reglas:**
- No inventes lo que no esté en los documentos: márcalo `[NECESITA ACLARACIÓN: ...]`.
- No adelantes fases.

**Detente** al terminar para la revisión humana.
