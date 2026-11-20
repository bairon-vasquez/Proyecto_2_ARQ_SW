# Segundo Taller: Arquitectura de Soluciones de Software

Análisis por rondas del material del docente (diapositivas y talleres resueltos) y **nuestras propias versiones** del Sistema de Gestión de Prácticas Empresariales.

## Análisis por rondas (`analisis/`)

| Ronda | Tema | Análisis |
|---|---|---|
| 1 | Patrones y Visión | [ronda-1-patrones-y-vision.md](analisis/ronda-1-patrones-y-vision.md) |
| 2 | Drivers arquitectónicos | [ronda-2-drivers.md](analisis/ronda-2-drivers.md) |
| 3 | ADR y documentación como código | [ronda-3-adr.md](analisis/ronda-3-adr.md) |
| 4 | Vistas (4+1, C4, secuencias) | [ronda-4-vistas.md](analisis/ronda-4-vistas.md) |
| 5 | SDD (Spec Driven Development) | [ronda-5-sdd.md](analisis/ronda-5-sdd.md) |

Cada análisis contiene: resumen de las diapositivas, análisis crítico del taller del docente y una tabla con las decisiones en que nuestra versión difiere.

## Nuestro repositorio (`practicas-empresariales/`)

```
practicas-empresariales/
├── AGENTS.md
├── docs/
│   ├── vision.md  drivers.md  contexto.md  arquitectura.md
│   ├── adr/        ADR-001 … ADR-010
│   ├── vistas/     01-logica … 04-fisica, matriz-cobertura
│   └── diagramas/  *.puml y secuencias/
├── prompts/        0-arranque … 5-validar
├── specs/001-postularse/   spec, plan, tasks, validacion
└── src/            (vacío por ahora)
```

## Notas
- Los diagramas `.puml` no se renderizaron aquí: ábrelos con la extensión PlantUML de VS Code.
- `validacion.md` de `001-postularse` ya está llena; ver sus hallazgos H-01 a H-06.
- Algunos supuestos (catálogo tecnológico, políticas vigentes) están declarados en la visión (S-09, S-10) y deben validarse con el Área de Sistemas.
