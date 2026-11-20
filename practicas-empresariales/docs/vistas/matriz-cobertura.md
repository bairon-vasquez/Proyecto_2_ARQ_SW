# Matriz de cobertura de drivers y ADR por vista

Ninguna fila vacía: todo driver y todo ADR se ve en al menos una vista (Ctx = contexto, Log = lógica, Proc = procesos, Des = desarrollo, Fís = física).

| Driver o ADR | Ctx | Log | Proc | Des | Fís |
|---|:-:|:-:|:-:|:-:|:-:|
| [CU-01](../drivers.md#cu-01) Postularse | ✓ | ✓ | ✓ | ✓ | |
| [CU-07](../drivers.md#cu-07) Evaluar practicante | ✓ | ✓ | ✓ | ✓ | |
| [CU-09](../drivers.md#cu-09) Generar acta | | ✓ | ✓ | ✓ | |
| [CU-10](../drivers.md#cu-10) Aprobar acta | | ✓ | ✓ | ✓ | ✓ |
| [CU-12](../drivers.md#cu-12) Configurar reglas | | ✓ | | ✓ | |
| [CU-15](../drivers.md#cu-15) Migrar prácticas | ✓ | | ✓ | | ✓ |
| [EAC-01](../drivers.md#eac-01) Modificabilidad | | ✓ | | ✓ | |
| [EAC-02](../drivers.md#eac-02) Tolerancia a fallos del SIA | | ✓ | ✓ | ✓ | |
| [EAC-03](../drivers.md#eac-03) Enlace inválido | | | ✓ | ✓ | |
| [EAC-04](../drivers.md#eac-04) Acta en < 10 s | | | ✓ | | ✓ |
| [RT-01](../drivers.md#rt-01) Infraestructura institucional | | | | | ✓ |
| [RT-02](../drivers.md#rt-02) SSO | ✓ | | ✓ | ✓ | ✓ |
| [RT-03](../drivers.md#rt-03) SIA solo por servicios | ✓ | | ✓ | ✓ | ✓ |
| [RT-04](../drivers.md#rt-04) Catálogo tecnológico | | | ✓ | ✓ | ✓ |
| [RN-01](../drivers.md#rn-01) Ley 1581 (datos personales) | | | | ✓ | ✓ |
| [RN-02](../drivers.md#rn-02) Retención documental | | ✓ | ✓ | | ✓ |
| [RN-03](../drivers.md#rn-03) Formato del acta | | ✓ | | ✓ | |
| [RN-04](../drivers.md#rn-04) Supervisor sin cuenta | ✓ | | ✓ | | |
| [RN-05](../drivers.md#rn-05) Sin licencias recurrentes | | | | ✓ | ✓ |
| [PA-01](../drivers.md#pa-01) Estructura general | | | ✓ | ✓ | |
| [PA-02](../drivers.md#pa-02) Autenticación y autorización | ✓ | ✓ | | ✓ | |
| [PA-03](../drivers.md#pa-03) Registro y trazabilidad | | ✓ | ✓ | ✓ | |
| [PA-04](../drivers.md#pa-04) Fallas de integración | | ✓ | ✓ | ✓ | |
| [PA-05](../drivers.md#pa-05) Configuración y entornos | | | | | ✓ |
| [ADR-001](../adr/ADR-001-monolito-modular.md) Monolito modular | | | ✓ | ✓ | |
| [ADR-002](../adr/ADR-002-plataforma-institucional.md) Plataforma institucional | | | ✓ | | ✓ |
| [ADR-003](../adr/ADR-003-integraciones-outbox.md) Outbox y reintentos | | ✓ | ✓ | ✓ | |
| [ADR-004](../adr/ADR-004-autenticacion-dual.md) Autenticación dual | ✓ | | ✓ | ✓ | |
| [ADR-005](../adr/ADR-005-autorizacion-por-roles.md) Autorización por roles | | ✓ | | ✓ | |
| [ADR-006](../adr/ADR-006-bitacora-auditoria.md) Bitácora de auditoría | | ✓ | ✓ | ✓ | |
| [ADR-007](../adr/ADR-007-reglas-versionadas.md) Reglas versionadas | | ✓ | | ✓ | |
| [ADR-008](../adr/ADR-008-acta-plantilla-inmutable.md) Acta inmutable | | ✓ | ✓ | ✓ | ✓ |
| [ADR-009](../adr/ADR-009-migracion-inicial.md) Migración inicial | | | ✓ | | ✓ |
| [ADR-010](../adr/ADR-010-configuracion-y-entornos.md) Configuración y entornos | | | | | ✓ |

## Recorrido de validación de los escenarios (+1)

| Escenario | Contexto | Lógica | Procesos | Desarrollo | Física |
|---|---|---|---|---|---|
| [ESC-01](../drivers.md#esc-01) [CU-01](../drivers.md#cu-01) ([EAC-02](../drivers.md#eac-02)) | Estudiante, SIA, correo | Postulacion, TareaPendiente | Web, API, Procesador, PostgreSQL | Controlador, Postulaciones, Adaptador SIA, Adaptador PostgreSQL | Servidor de aplicaciones, BD |
| [ESC-02](../drivers.md#esc-02) [CU-07](../drivers.md#cu-07) ([EAC-03](../drivers.md#eac-03)) | Supervisor, correo | EnlaceAcceso, Evaluacion, RegistroBitacora | Web, API, Procesador, PostgreSQL | Controlador, Evaluaciones, Adaptador de correo | Servidor web, de aplicaciones |
| [ESC-03](../drivers.md#esc-03) [CU-09](../drivers.md#cu-09) ([EAC-04](../drivers.md#eac-04)) | Docente asesor | Acta, PlantillaActa | Web, API, PostgreSQL | Controlador, Actas, Generador de PDF | Servidor de aplicaciones (CPU) |
| [ESC-04](../drivers.md#esc-04) [CU-10](../drivers.md#cu-10) | Docente asesor, director, correo | Acta, RegistroBitacora | Web, API, Almacenamiento, Procesador | Actas, Política de autorización, Adaptador de documentos | Almacenamiento institucional |
| [ESC-05](../drivers.md#esc-05) [CU-12](../drivers.md#cu-12) ([EAC-01](../drivers.md#eac-01)) | Director | VersionReglas | Web, API, PostgreSQL | Módulo Reglas | Servidor de aplicaciones |
| [ESC-06](../drivers.md#esc-06) [CU-15](../drivers.md#cu-15) | Administrador | Practica, VersionReglas | Comando de migración, PostgreSQL | (mismo código del backend) | Estación de administración |
