# Contexto del sistema

Marco que encuadra las cuatro vistas de 4+1; **no es una vista** de 4+1. Nivel 1 de C4.

## 1. Presentación principal

Diagrama: [diagramas/contexto.puml](diagramas/contexto.puml). El sistema es una caja negra con cinco tipos de persona y tres sistemas externos.

## 2. Catálogo de elementos

| Elemento | Tipo | Rol o responsabilidad | Interacción con el sistema |
|---|---|---|---|
| Estudiante | Persona | Se postula, registra horas semanales y consulta el estado de su práctica | Aplicación web (HTTPS) |
| Docente asesor | Persona | Revisa horas y avance, solicita y aprueba el acta | Aplicación web (HTTPS) |
| Director de programa | Persona | Aprueba postulaciones, asigna asesor, configura reglas, monitorea y consolida | Aplicación web (HTTPS) |
| Supervisor de empresa | Persona (externo) | Valida horas y evalúa al practicante, sin cuenta | Aplicación web por enlace de un solo uso (HTTPS) |
| Administrador del sistema | Persona | Ejecuta la migración inicial y opera la configuración | Línea de comandos |
| Sistema de Gestión de Prácticas Empresariales | Sistema en alcance | Gestiona postulación, asesor, horas, evaluación y acta final | Con todos los elementos |
| SIA | Sistema externo | Fuente de datos y requisitos académicos; administrado por el Área de Sistemas | HTTPS / REST (solo por sus servicios, [RT-03](drivers.md#rt-03)) |
| Proveedor de identidad institucional | Sistema externo | Autentica con la cuenta institucional ([RT-02](drivers.md#rt-02)) | OpenID Connect |
| Servicio de correo institucional | Sistema externo | Entrega enlaces, recordatorios y notificaciones | SMTP |

## 3. Justificación

- [CU-01](drivers.md#cu-01) (SIA), [CU-07](drivers.md#cu-07) (supervisor externo), [CU-09](drivers.md#cu-09)/[CU-10](drivers.md#cu-10) (acta) definen los actores y las integraciones críticas.
- [RT-03](drivers.md#rt-03): el SIA es externo y no se controla, por eso aparece como sistema aparte y solo se accede por sus servicios.
- [RT-02](drivers.md#rt-02) y [ADR-004](adr/ADR-004-autenticacion-dual.md): el proveedor de identidad es un sistema externo; el supervisor **no** interactúa con él ([RN-04](drivers.md#rn-04)).
- Interesados: el administrador del SIA necesita ver qué se consulta y por qué canal.

## 4. Comportamiento

Aquí empiezan los escenarios (+1): [CU-01 con el SIA caído](diagramas/secuencias/cu01-postularse.puml) y [CU-07 por enlace](diagramas/secuencias/cu07-evaluar-practicante.puml).

## 5. Vistas relacionadas

- [Procesos](vistas/02-procesos.md): qué contenedor habla con cada sistema externo.
- [Física](vistas/04-fisica.md): por qué red sale cada conexión.
