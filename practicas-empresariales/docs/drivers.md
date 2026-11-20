# Drivers arquitectónicos: Sistema de Gestión de Prácticas Empresariales

> **Enunciado.** Partiendo del documento de visión ([vision.md](vision.md)), producir: casos de uso (mínimo 12) marcando los primarios (máximo 6), tres escenarios de atributos de calidad completos, tabla de restricciones, cinco preocupaciones arquitectónicas y matriz de priorización.

Se identifican **24 drivers**: 6 casos de uso primarios, 4 escenarios de atributos de calidad, 9 restricciones y 5 preocupaciones arquitectónicas.

Criterios para que un caso de uso sea primario: (1) importancia para el negocio, (2) complejidad técnica, (3) alta frecuencia de uso, (4) riesgo, (5) atado a un atributo de calidad crítico.

## 1. Casos de uso y casos de uso primarios

| ID | Caso de uso | Actor | ¿Primario? | Justificación | Se especifica en |
|----|-------------|-------|:---:|---------------|------------------|
| <a id="cu-01"></a>**CU-01** | Postularse a la práctica empresarial | Estudiante | **Sí** | (2) Complejidad técnica: verifica requisitos contra los servicios del SIA ([RT-03](#rt-03)), única integración con otro sistema, y debe tolerar sus fallas. | [specs/001-postularse](../specs/001-postularse/spec.md) |
| <a id="cu-02"></a>**CU-02** | Aprobar o rechazar la postulación | Director de programa | No | Decide sobre datos ya verificados en [CU-01](#cu-01); no ejercita nada nuevo. | (sin especificar) |
| <a id="cu-03"></a>**CU-03** | Asignar el docente asesor | Director de programa | No | Registro simple con consulta de carga de cada docente. | (sin especificar) |
| <a id="cu-04"></a>**CU-04** | Registrar las horas semanales | Estudiante | No | Es frecuente, pero son a lo sumo 250 registros por semana ([S-03](vision.md#s-03)): formulario simple. | (sin especificar) |
| <a id="cu-05"></a>**CU-05** | Validar las horas registradas | Supervisor de empresa | No | Usa el mismo acceso por enlace que [CU-07](#cu-07); el mecanismo se decide una vez en [CU-07](#cu-07). | (sin especificar) |
| <a id="cu-06"></a>**CU-06** | Revisar horas y avance del practicante | Docente asesor | No | Consulta de datos ya registrados. | (sin especificar) |
| <a id="cu-07"></a>**CU-07** | Evaluar el desempeño del practicante | Supervisor de empresa | **Sí** | (4) Riesgo: sin evaluación no hay acta ([R-01](vision.md#r-01), [OB-02](vision.md#ob-02)) y el actor externo no tiene cuenta ([RN-04](#rn-04)). | [specs/007-evaluar-practicante](../specs/007-evaluar-practicante/spec.md) |
| <a id="cu-08"></a>**CU-08** | Enviar recordatorios de plazos | Sistema (tarea programada) | No | Envío de bajo volumen por correo institucional; la estructura ya la cubre [PA-04](#pa-04). | (sin especificar) |
| <a id="cu-09"></a>**CU-09** | Generar el acta final | Sistema, a solicitud del docente asesor | **Sí** | (1) Importancia para el negocio: es la razón de ser del sistema; de ella dependen [OB-01](vision.md#ob-01) y [OB-04](vision.md#ob-04). | [specs/009-generar-acta](../specs/009-generar-acta/spec.md) |
| <a id="cu-10"></a>**CU-10** | Aprobar el acta electrónicamente | Docente asesor y director de programa | **Sí** | (5) Atado a un atributo crítico: seguridad (quién aprobó el acta y cuándo, [S-06](vision.md#s-06), [OB-06](vision.md#ob-06)). | [specs/010-aprobar-acta](../specs/010-aprobar-acta/spec.md) |
| <a id="cu-11"></a>**CU-11** | Consultar el estado del trámite | Estudiante | No | Consulta simple. | (sin especificar) |
| <a id="cu-12"></a>**CU-12** | Configurar las reglas de práctica de un programa | Director de programa | **Sí** | (5) Atado a mantenibilidad ([OB-05](vision.md#ob-05)): requisitos y horas varían por programa ([S-07](vision.md#s-07)). | [specs/012-configurar-reglas](../specs/012-configurar-reglas/spec.md) |
| <a id="cu-13"></a>**CU-13** | Monitorear prácticas y alertas de atraso | Director de programa | No | Reporte sobre datos que ya registran los demás casos de uso. | (sin especificar) |
| <a id="cu-14"></a>**CU-14** | Generar el consolidado para auditoría o acreditación | Director de programa | No | Importante ([OB-06](vision.md#ob-06)), pero es una consulta sobre datos existentes; el desempeño lo cubre [EAC-04](#eac-04) por analogía con [CU-09](#cu-09). | (sin especificar) |
| <a id="cu-15"></a>**CU-15** | Migrar las prácticas en curso desde Excel | Administrador del sistema | **Sí** | (4) Riesgo: formatos heterogéneos por docente asesor, incertidumbre sobre su calidad, define el primer despliegue ([R-05](vision.md#r-05)). | [specs/015-migrar-practicas](../specs/015-migrar-practicas/spec.md) |

## 2. Escenarios de atributos de calidad

<a id="eac-01"></a>

### EAC-01: Mantenibilidad (modificabilidad)

| Parte | Pregunta | Contenido |
|-------|----------|-----------|
| **1. Fuente del estímulo** | ¿Quién o qué lo provoca? | Un desarrollador con un mes en el proyecto |
| **2. Estímulo** | ¿Qué ocurre? | Debe incorporar las reglas de un programa nuevo aprobadas por el Consejo de Facultad: horas mínimas distintas y un requisito académico adicional |
| **3. Artefacto** | ¿Sobre qué parte? | El módulo de reglas de práctica y su configuración |
| **4. Entorno** | ¿En qué condiciones? | Desarrollo con el sistema en operación y prácticas de otros programas en curso |
| **5. Respuesta** | ¿Qué debe hacer el sistema? | Se agrega y publica el programa sin interrumpir el servicio y sin afectar las prácticas en curso |
| **6. Medida de respuesta** | ¿Cómo se verifica? | **En máximo 12 horas de trabajo, tocando como máximo 2 módulos, con 0 prácticas en curso de otros programas que cambien de estado o de reglas y 0 minutos de indisponibilidad** |

**Escenario redactado.** Un desarrollador con un mes en el proyecto incorpora, con el sistema en operación, las reglas de un programa nuevo (horas mínimas distintas y un requisito académico adicional) en el módulo de reglas. Lo termina y publica en máximo 12 horas de trabajo, tocando como máximo 2 módulos, sin ninguna indisponibilidad y sin que cambie el estado o las reglas de ninguna práctica en curso.

**Traza:** [OB-05](vision.md#ob-05), [S-07](vision.md#s-07), [CU-12](#cu-12)

<a id="eac-02"></a>

### EAC-02: Fiabilidad (tolerancia a fallos)

| Parte | Pregunta | Contenido |
|-------|----------|-----------|
| **1. Fuente del estímulo** | ¿Quién o qué lo provoca? | El servicio de consulta del SIA |
| **2. Estímulo** | ¿Qué ocurre? | No responde en 4 segundos o responde con error cuando un estudiante envía su postulación |
| **3. Artefacto** | ¿Sobre qué parte? | El componente de integración con el SIA usado por [CU-01](#cu-01) |
| **4. Entorno** | ¿En qué condiciones? | Pico de inicio de periodo, hasta 40 usuarios concurrentes ([S-03](vision.md#s-03)) |
| **5. Respuesta** | ¿Qué debe hacer el sistema? | Guarda la postulación como "pendiente de verificación", confirma su recepción y reintenta la verificación sin intervención humana |
| **6. Medida de respuesta** | ¿Cómo se verifica? | **0 postulaciones perdidas; confirmación al estudiante en menos de 2 segundos en el 95 % de los casos; verificación completada en máximo 20 minutos después de que el SIA se recupera, en el 100 % de los casos** |

**Escenario redactado.** Cuando el SIA no responde en 4 segundos durante una postulación, en el pico de inicio de periodo con hasta 40 usuarios concurrentes, el sistema guarda la postulación como pendiente, confirma su recepción en menos de 2 segundos (95 % de los casos) y completa la verificación en máximo 20 minutos tras la recuperación del SIA, sin perder ninguna postulación.

**Traza:** [OB-01](vision.md#ob-01), [RT-03](#rt-03), [R-02](vision.md#r-02), [CU-01](#cu-01)

<a id="eac-03"></a>

### EAC-03: Seguridad (confidencialidad y responsabilidad)

| Parte | Pregunta | Contenido |
|-------|----------|-----------|
| **1. Fuente del estímulo** | ¿Quién o qué lo provoca? | Una persona distinta del supervisor al que se envió el enlace |
| **2. Estímulo** | ¿Qué ocurre? | Intenta abrir un enlace de evaluación o de validación de horas ya usado, con más de 15 días de emitido o con el identificador alterado |
| **3. Artefacto** | ¿Sobre qué parte? | El mecanismo de acceso por enlace de [CU-05](#cu-05) y [CU-07](#cu-07) |
| **4. Entorno** | ¿En qué condiciones? | Operación normal |
| **5. Respuesta** | ¿Qué debe hacer el sistema? | Niega el acceso sin mostrar datos del practicante, registra el intento y avisa al docente asesor |
| **6. Medida de respuesta** | ¿Cómo se verifica? | **100 % de los intentos rechazados; 0 datos personales mostrados; intento en la bitácora con fecha, hora y dirección de origen en menos de 1 minuto; aviso al docente asesor en menos de 10 minutos** |

**Escenario redactado.** Cuando alguien intenta abrir un enlace usado, vencido o alterado, el sistema rechaza el 100 % de los intentos sin mostrar datos personales, registra cada uno en la bitácora en menos de 1 minuto y avisa al docente asesor en menos de 10 minutos.

**Traza:** [RN-01](#rn-01), [RN-04](#rn-04), [OB-02](vision.md#ob-02), [OB-06](vision.md#ob-06), [CU-05](#cu-05), [CU-07](#cu-07)

<a id="eac-04"></a>

### EAC-04: Eficiencia de desempeño (comportamiento temporal)

| Parte | Pregunta | Contenido |
|-------|----------|-----------|
| **1. Fuente del estímulo** | ¿Quién o qué lo provoca? | Un docente asesor autenticado |
| **2. Estímulo** | ¿Qué ocurre? | Solicita generar el acta final de un practicante con horas validadas y evaluación recibida |
| **3. Artefacto** | ¿Sobre qué parte? | El módulo de actas (plantilla y generación del PDF) |
| **4. Entorno** | ¿En qué condiciones? | Cierre de periodo, hasta 30 docentes generando actas a la vez |
| **5. Respuesta** | ¿Qué debe hacer el sistema? | Genera el acta en el formato oficial con los datos registrados y la deja disponible para aprobación |
| **6. Medida de respuesta** | ¿Cómo se verifica? | **En menos de 10 segundos en el 95 % de los casos, con 0 campos transcritos manualmente y CPU del servidor de aplicaciones por debajo del 70 %** |

**Escenario redactado.** En el cierre de periodo, con hasta 30 docentes generando actas simultáneamente, cada acta se genera en el formato oficial en menos de 10 segundos en el 95 % de los casos, sin transcripción manual y sin superar el 70 % de CPU.

**Traza:** [OB-01](vision.md#ob-01), [OB-04](vision.md#ob-04), [RN-03](#rn-03), [CU-09](#cu-09)

## 3. Restricciones

Las restricciones de la visión entran como drivers sin transformación; aquí se agrega su tipo y su impacto arquitectónico.

| ID | Restricción | Tipo | Origen | Impacto arquitectónico esperado |
|----|-------------|------|--------|----------------------------------|
| <a id="rt-01"></a>**RT-01** | Desplegar en la infraestructura que administra la Universidad | Técnica | Área de Sistemas | Descarta servicios gestionados de nube pública (funciones sin servidor, BD como servicio). |
| <a id="rt-02"></a>**RT-02** | Autenticar con la cuenta institucional (inicio de sesión único) | Técnica | Administrador del SIA / seguridad | El sistema no guarda contraseñas; obliga a un adaptador hacia el proveedor de identidad. |
| <a id="rt-03"></a>**RT-03** | Consultar datos académicos solo por los servicios del SIA | Técnica | Administrador del SIA | Obliga a un componente de integración aislado y a manejar sus fallas ([EAC-02](#eac-02)). |
| <a id="rt-04"></a>**RT-04** | Usar el motor de base de datos y las tecnologías del catálogo institucional | Técnica | Área de Sistemas | Limita lenguaje, framework y persistencia (modelo relacional); descarta bases documentales o infraestructura nueva. |
| <a id="rn-01"></a>**RN-01** | Tratar datos personales según Ley 1581 de 2012 | Negocio | Legislación, área jurídica | Autorización por rol sobre datos personales, registro de la autorización de tratamiento y cifrado en tránsito. |
| <a id="rn-02"></a>**RN-02** | Conservar actas y evidencias según la tabla de retención | Negocio | Gestión documental (Ley 594) | Las actas aprobadas no se modifican ni se borran; política de conservación. |
| <a id="rn-03"></a>**RN-03** | El acta sigue el formato del reglamento | Negocio | Consejo de Facultad | El formato vive en una plantilla separada del código. |
| <a id="rn-04"></a>**RN-04** | No exigir cuenta ni registro a supervisores | Negocio | Director de programa | Segundo mecanismo de acceso: enlace de un solo uso con vencimiento ([EAC-03](#eac-03)). |
| <a id="rn-05"></a>**RN-05** | Sin licencias comerciales de pago recurrente | Negocio | Decanatura | Descarta plataformas comerciales de flujos de trabajo o de firma por suscripción. |

## 4. Preocupaciones arquitectónicas

| ID | Preocupación | Qué hay que decidir | Por qué importa en este sistema |
|----|--------------|---------------------|---------------------------------|
| <a id="pa-01"></a>**PA-01** | Estructura general | En qué bloques se divide el sistema y hacia dónde apuntan sus dependencias | Carga baja ([S-03](vision.md#s-03)) pero reglas cambiantes ([OB-05](vision.md#ob-05)): pide modularidad, no distribución. |
| <a id="pa-02"></a>**PA-02** | Autenticación y autorización | Cómo conviven dos formas de acceso y cómo se controlan los permisos de cinco roles | SSO institucional ([RT-02](#rt-02)) y enlace sin cuenta ([RN-04](#rn-04)); estudiante, docente asesor, director, supervisor y administrador. |
| <a id="pa-03"></a>**PA-03** | Registro y trazabilidad | Qué eventos se registran, dónde y por cuánto tiempo | Auditoría y acreditación ([OB-06](vision.md#ob-06)), datos personales ([RN-01](#rn-01)) y diagnóstico de la mesa de ayuda. |
| <a id="pa-04"></a>**PA-04** | Fallas de integración y estados pendientes | Una sola estrategia para fallas del SIA y del correo: reintentos, estados pendientes y mensajes | Sin ella, cada caso de uso trata distinto la caída del SIA ([R-02](vision.md#r-02), [EAC-02](#eac-02)). |
| <a id="pa-05"></a>**PA-05** | Configuración y entornos | Cómo se parametriza sin recompilar, qué entornos existen y cómo se despliega | El Área de Sistemas opera el sistema ([RT-01](#rt-01)) y las reglas varían por programa y periodo ([S-07](vision.md#s-07)). |

## 5. Matriz de priorización

La importancia la asigna el cliente (director de programa) y la dificultad técnica el arquitecto.

### Alta importancia, alta dificultad: atender primero
[CU-01](#cu-01), [CU-07](#cu-07), [CU-12](#cu-12), [CU-15](#cu-15), [EAC-01](#eac-01), [EAC-02](#eac-02), [RT-02](#rt-02), [RT-03](#rt-03), [PA-02](#pa-02), [PA-04](#pa-04)

### Alta importancia, baja dificultad: hacer ya
[CU-09](#cu-09), [CU-10](#cu-10), [EAC-03](#eac-03), [EAC-04](#eac-04), [RT-01](#rt-01), [RT-04](#rt-04), [RN-01](#rn-01), [RN-02](#rn-02), [RN-03](#rn-03), [RN-04](#rn-04), [PA-01](#pa-01), [PA-03](#pa-03)

### Baja importancia, baja dificultad: hacer si sobra tiempo
[RN-05](#rn-05), [PA-05](#pa-05)

### Baja importancia, alta dificultad: cuestionar
*(vacío)* — Se cuestionó una candidata, el mecanismo de firma digital certificada ([R-03](vision.md#r-03)), y se sacó del alcance ([S-06](vision.md#s-06)).

## 6. Escenarios (+1 de 4+1)

Inventario de escenarios que se diagraman en [`diagramas/secuencias/`](diagramas/secuencias/). Un escenario por caso de uso primario, y uno por cada EAC que no queda cubierto.

| ID | Escenario | Origen | Por qué es escenario | Archivo en secuencias/ |
|----|-----------|--------|----------------------|------------------------|
| <a id="esc-01"></a>**ESC-01** | Postularse con el SIA caído | [CU-01](#cu-01) | Caso primario; cubre [EAC-02](#eac-02) (ninguna postulación se pierde) | `cu01-postularse.puml` |
| <a id="esc-02"></a>**ESC-02** | Evaluar al practicante por enlace | [CU-07](#cu-07) | Caso primario; cubre [EAC-03](#eac-03) (enlace inválido rechazado) | `cu07-evaluar-practicante.puml` |
| <a id="esc-03"></a>**ESC-03** | Generar el acta final | [CU-09](#cu-09) | Caso primario; cubre [EAC-04](#eac-04) (menos de 10 s) | `cu09-generar-acta.puml` |
| <a id="esc-04"></a>**ESC-04** | Aprobar el acta electrónicamente | [CU-10](#cu-10) | Caso primario; trazabilidad ([PA-03](#pa-03)) | `cu10-aprobar-acta.puml` |
| <a id="esc-05"></a>**ESC-05** | Configurar reglas de un programa nuevo | [CU-12](#cu-12) | Caso primario; cubre [EAC-01](#eac-01) | `cu12-configurar-reglas.puml` |
| <a id="esc-06"></a>**ESC-06** | Migrar prácticas en curso | [CU-15](#cu-15) | Caso primario por riesgo | `cu15-migrar-practicas.puml` |

Los cuatro EAC quedan cubiertos dentro de los seis escenarios, por eso no hace falta un escenario adicional por EAC.
