# Validación: 010 Aprobar el acta electrónicamente (CU-10)

> **Estado: pendiente.** Se llena en T-11, cuando exista el código de `src/`. No se marca "Cumple" sin evidencia.

| Escenario | Resultado | Evidencia |
|---|---|---|
| Aprobación del docente asesor (flujo básico, primera firma) | Pendiente | — |
| Aprobación del director de programa (segunda firma) | Pendiente | — |
| El director intenta aprobar antes que el asesor | Pendiente | — |
| Usuario sin el rol requerido | Pendiente | — |
| Docente que no es el asesor de la práctica | Pendiente | — |
| El director devuelve el acta con observaciones | Pendiente | — |
| Un acta aprobada no se puede modificar ni borrar | Pendiente | — |

## Revisión de la regla de dependencia

- `dominio/` no importa `aplicacion/` ni `infraestructura/`: pendiente.
- `aplicacion/` solo importa `dominio/`: pendiente.

## Hallazgos

Ninguno todavía.
