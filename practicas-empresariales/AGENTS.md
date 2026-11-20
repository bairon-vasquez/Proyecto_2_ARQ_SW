# AGENTS.md: Sistema de Gestión de Prácticas Empresariales

## Fuentes de verdad
- `docs/arquitectura.md`: mapa de visión, drivers, ADR, vistas y glosario.
- `specs/`: una carpeta por caso de uso de `docs/drivers.md`, con el mismo número ([CU-01](docs/drivers.md#cu-01) → `specs/001-postularse/`).
- Si el código contradice una especificación, gana la especificación. Si la especificación parece incorrecta, detenerse y preguntar.

## Arquitectura
- Monolito modular ([ADR-001](docs/adr/ADR-001-monolito-modular.md)), con Clean Architecture por dentro.
- `dominio/` no importa nada de `aplicacion/` ni de `infraestructura/`; `aplicacion/` solo importa `dominio/`.
- Puertos como `Protocol` en `aplicacion/puertos/`; los adaptadores los implementan en `infraestructura/`.
- Persistencia PostgreSQL ([ADR-002](docs/adr/ADR-002-plataforma-institucional.md)) y tareas pendientes en tabla ([ADR-003](docs/adr/ADR-003-integraciones-outbox.md)); en esta etapa, **adaptadores en memoria**.
- Autorización en los casos de uso, negación por defecto ([ADR-005](docs/adr/ADR-005-autorizacion-por-roles.md)).

## Convenciones de código
- Python 3.12; una clase por archivo; nombres en español según el glosario (sección 10 de `docs/arquitectura.md`).
- DTO en la entrada y la salida de los casos de uso.
- Archivos en `snake_case`, clases en `PascalCase`.
- Se permiten pruebas automáticas con `pytest` además de la validación manual por escenario.

## Forma de trabajar
- Una tarea de `tasks.md` a la vez.
- Al terminar: marcar la tarea, listar los archivos cambiados, proponer el mensaje de commit y detenerse.
- No inventar requisitos: lo que no esté en `spec.md` se pregunta.
- No cambiar `docs/` ni `prompts/` sin que lo pida la persona.
