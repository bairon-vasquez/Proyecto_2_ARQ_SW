# Documento de visión: Sistema de Gestión de Prácticas Empresariales

> **Enunciado.** La Facultad de Ingenierías quiere un sistema para gestionar las prácticas empresariales de los estudiantes: postulación, asignación de tutor, seguimiento de horas, evaluación de la empresa y generación del acta final. Hoy todo se maneja en Excel y correo electrónico. Hay 500 estudiantes en práctica al año y 50 tutores.

## 1. Problema u oportunidad

La Facultad gestiona cada año las prácticas empresariales de 500 estudiantes con 50 docentes asesores usando hojas de Excel y correo electrónico. No existe una fuente única de información: cada docente asesor lleva sus archivos a su manera, las horas se consolidan a mano, las evaluaciones de las empresas llegan sin control de plazos y el acta final se arma juntando datos dispersos. Esto es insatisfactorio porque el director de programa no sabe en tiempo real qué estudiantes van atrasados, el cierre de la práctica (y con él el grado) se demora, las actas salen con errores de transcripción y cada auditoría o proceso de acreditación obliga a reconstruir la información manualmente.

## 2. Objetivos de negocio

| ID | Objetivo de negocio (qué gana la Facultad, medible) | Atributo de calidad que implica |
|----|------------------------------------------------------|----------------------------------|
| <a id="ob-01"></a>**OB-01** | Reducir a máximo **3 días hábiles** el tiempo entre el cumplimiento de las horas del estudiante y la emisión de su acta final, en el **90 %** de las prácticas del primer periodo de operación. | Eficiencia de desempeño (comportamiento temporal) |
| <a id="ob-02"></a>**OB-02** | Recibir dentro del plazo reglamentario al menos el **90 %** de las evaluaciones que las empresas hacen de sus practicantes, durante el primer año de operación. | Capacidad de interacción (usuarios externos) |
| <a id="ob-03"></a>**OB-03** | Reducir en **60 %** las horas semanales que cada docente asesor dedica a consolidar información, medidas por encuesta antes y después del primer periodo. | Adecuación funcional / Capacidad de interacción |
| <a id="ob-04"></a>**OB-04** | Bajar a **menos del 1 %** las actas que deben reemitirse por errores en los datos, durante el primer año de operación. | Seguridad (integridad) |
| <a id="ob-05"></a>**OB-05** | Aplicar un cambio del reglamento o las reglas de un programa nuevo **desde el periodo académico siguiente a su aprobación**, sin suspender la gestión de las prácticas en curso. | Mantenibilidad (modificabilidad) |
| <a id="ob-06"></a>**OB-06** | Entregar a auditoría o acreditación el consolidado de prácticas de **cualquier periodo en máximo 1 día hábil**. | Seguridad (responsabilidad/trazabilidad) |
| <a id="ob-07"></a>**OB-07** | Que el director de programa identifique en **menos de 1 minuto** de consulta los estudiantes con atraso (sin horas registradas en la última semana o evaluación vencida), con datos actualizados a no más de **24 horas**. | Fiabilidad / Eficiencia |

## 3. Alcance

### Qué SÍ incluye
- Postulación del estudiante a la práctica ante la Facultad, con verificación de requisitos académicos.
- Aprobación de la postulación y asignación del docente asesor por el director de programa, según la carga de cada docente.
- Registro semanal de horas por el estudiante, validación por el supervisor de la empresa y revisión por el docente asesor.
- Evaluación del practicante por parte de la empresa, con plazos y recordatorios.
- Acta final en el formato oficial, con aprobación electrónica trazable.
- Seguimiento del estado de cada práctica, consolidado para auditoría y acreditación.
- Migración de las prácticas en curso desde los archivos de Excel actuales.

### Qué NO incluye
- Bolsa de empleo o búsqueda de la plaza de práctica (el estudiante llega con la plaza conseguida).
- Gestión y firma de convenios con las empresas (solo se consulta si están vigentes).
- Afiliación a ARL, pagos o apoyos de sostenimiento del practicante.
- Evaluación de la empresa por parte del estudiante.
- Firma digital certificada del acta, carga automática de la nota en el SIA e histórico de prácticas de años anteriores.

## 4. Stakeholders

| Nombre / rol | Tipo | Preocupaciones (y atributo de calidad) | Poder / interés |
|---|---|---|---|
| Decanatura y Consejo de Facultad (patrocinador) | Negocio | Costo, plazo de puesta en marcha e indicadores de acreditación (costo, tiempo al mercado) | Alto / alto: gestionar de cerca |
| Director de programa (coordinador de práctica, cliente) | Negocio | Conocer el estado de todas las prácticas y cerrarlas a tiempo (adecuación funcional) | Alto / alto: gestionar de cerca |
| Docentes asesores de práctica (50) | Negocio | Revisar horas y avance sin trabajo adicional (capacidad de interacción, eficiencia) | Bajo / alto: mantener informado |
| Estudiantes en práctica (500 al año) | Negocio | Saber en qué va su trámite y registrar horas desde el celular (capacidad de interacción) | Bajo / alto: mantener informado |
| Supervisores de empresa (externos) | Negocio | Evaluar y validar horas en pocos minutos, sin crear cuentas (capacidad de interacción) | Bajo / alto: mantener informado |
| Área jurídica y gestión documental | Negocio | Protección de datos personales, validez y conservación del acta (seguridad, auditabilidad) | Alto / bajo: mantener satisfecho |
| Auditor / líder de acreditación | Negocio | Obtener evidencias y consolidados por periodo sin reconstruirlos (responsabilidad, trazabilidad) | Alto / bajo: mantener satisfecho |
| Área de Sistemas (infraestructura) | **Técnico** | Desplegar, monitorear y respaldar el sistema con su personal (operabilidad, recuperabilidad) | Alto / alto: gestionar de cerca |
| Administrador del SIA y de seguridad de la información | **Técnico** | Integración solo por los servicios del SIA y autenticación institucional sin romper sus controles (interoperabilidad, seguridad) | Alto / alto: gestionar de cerca |
| Desarrolladores que mantendrán el sistema | **Técnico** | Cambiar reglas del reglamento sin romper lo existente (modificabilidad, capacidad de prueba) | Bajo / alto: mantener informado |
| Mesa de ayuda (soporte) | **Técnico** | Diagnosticar por qué un usuario no puede postularse o registrar horas (analizabilidad) | Bajo / alto: mantener informado |
| Usuario ocasional de consulta (secretaría de programa) | Negocio | Consultar el estado de un trámite sin formación previa (capacidad de interacción) | Bajo / bajo: monitorear |

## 5. Restricciones

| ID | Restricción (decisión ya tomada) | Quién la impone | Por qué |
|----|----------------------------------|-----------------|---------|
| **[RT-01](drivers.md#rt-01)** | Debe desplegarse en la infraestructura que administra la Universidad. | Área de Sistemas | Política de control, respaldo y soporte de los sistemas institucionales. |
| **[RT-02](drivers.md#rt-02)** | Debe autenticar a estudiantes, docentes y personal con la cuenta institucional (inicio de sesión único). | Administrador del SIA / seguridad de la información | Política institucional de gestión de identidades. |
| **[RT-03](drivers.md#rt-03)** | Debe consultar datos académicos solo mediante los servicios que el SIA expone, sin conexión directa a su base de datos. | Administrador del SIA | Una conexión directa afecta su rendimiento y evade sus controles; solo da soporte a ese catálogo. |
| **[RT-04](drivers.md#rt-04)** | Debe usar el motor de base de datos y las tecnologías del catálogo institucional. | Área de Sistemas | El personal de la Universidad solo puede dar soporte a ese catálogo. |
| **[RN-01](drivers.md#rn-01)** | Debe tratar los datos personales conforme a la Ley 1581 de 2012 y el Decreto 1377 de 2013. | Legislación colombiana, aplicada por el área jurídica | Obligación legal sobre autorización, finalidad y acceso. |
| **[RN-02](drivers.md#rn-02)** | Debe conservar actas y evidencias según la tabla de retención documental. | Gestión documental (Ley 594 de 2000) | Obligación legal archivística. |
| **[RN-03](drivers.md#rn-03)** | El acta debe seguir el formato y contenido del reglamento de prácticas. | Consejo de Facultad | Es un documento académico oficial. |
| **[RN-04](drivers.md#rn-04)** | No puede exigir a los supervisores de empresa cuenta institucional ni registro con contraseña. | Director de programa | La participación de las empresas es voluntaria; un trámite pesado pone en riesgo [OB-02](#ob-02). |
| **[RN-05](drivers.md#rn-05)** | No puede requerir licencias comerciales de pago recurrente. | Decanatura | Presupuesto de funcionamiento disponible. |

## 6. Supuestos y riesgos iniciales

### Supuestos

| ID | Lo que el enunciado no dice | Supuesto adoptado | Validar con |
|----|-----------------------------|-------------------|-------------|
| <a id="s-01"></a>**S-01** | Qué es "evaluación de la empresa" | La empresa califica el desempeño del practicante con un formulario corto y esa nota alimenta el acta. | Director de programa |
| <a id="s-02"></a>**S-02** | Contra qué se verifican los requisitos académicos | Contra el SIA, mediante los servicios que expone para otros sistemas ([RT-03](drivers.md#rt-03)). | Administrador del SIA |
| <a id="s-03"></a>**S-03** | Cuál es la carga real | Cada práctica dura de 4 a 6 meses: de las 500 anuales hay entre 170 y 250 activas a la vez, con decenas de usuarios concurrentes y picos al inicio de periodo y al cierre. No justifica una arquitectura distribuida. | Director de programa |
| <a id="s-04"></a>**S-04** | Ante quién se postula el estudiante | Ante la Facultad, con la plaza ya conseguida. | Director de programa |
| <a id="s-05"></a>**S-05** | Quién valida las horas | El estudiante las registra cada semana, el supervisor las valida y el docente asesor las revisa. | Director de programa |
| <a id="s-06"></a>**S-06** | Qué firmas exige el acta | Basta la aprobación electrónica trazable del docente asesor y del director de programa. | Área jurídica |
| <a id="s-07"></a>**S-07** | Si todos los programas usan las mismas reglas | Requisitos y horas mínimas varían por programa y pueden cambiar cada periodo. | Directores de programa |
| <a id="s-08"></a>**S-08** | Cómo está hoy el proceso en cifras | No hay indicadores; la línea base se reconstruye con correos y archivos del último año y con una encuesta previa a los 50 docentes asesores. | Director de programa |
| <a id="s-09"></a>**S-09** | Qué contiene el catálogo tecnológico institucional | Incluye al menos un motor relacional (PostgreSQL), Python o equivalente para el servidor y Angular o equivalente para la interfaz; se confirma en la primera semana. | Área de Sistemas |
| <a id="s-10"></a>**S-10** | Si las políticas RT/RN siguen vigentes | [RT-01](drivers.md#rt-01) a [RT-04](drivers.md#rt-04) y [RN-01](drivers.md#rn-01) a [RN-05](drivers.md#rn-05) están vigentes; cada dueño las confirma en la primera semana. | Área de Sistemas, Decanatura, Área jurídica |

### Riesgos

| ID | Riesgo inicial | Objetivo afectado | Mitigación |
|----|----------------|-------------------|------------|
| <a id="r-01"></a>**R-01** | Los supervisores de empresa no responden a tiempo. | [OB-01](#ob-01), [OB-02](#ob-02) | Acceso por enlace sin cuenta ([RN-04](drivers.md#rn-04)), formulario corto y recordatorios con copia al docente asesor. |
| <a id="r-02"></a>**R-02** | El SIA no ofrece servicios de consulta o fallan con frecuencia. | [OB-01](#ob-01) | Confirmar servicios en la primera semana; si no existen, acordar una exportación periódica y aislar la integración. |
| <a id="r-03"></a>**R-03** | Se exige firma digital certificada del acta (contradice [S-06](#s-06)). | [OB-01](#ob-01), [OB-04](#ob-04) | Validar [S-06](#s-06) con el área jurídica antes de diseñar; dejar la aprobación detrás de una interfaz sustituible. |
| <a id="r-04"></a>**R-04** | Sobredimensionar la solución para una carga que no existe. | Costo (Decanatura) | Justificar cada decisión con [S-03](#s-03) y [RT-01](drivers.md#rt-01); preferir lo simple de operar. |
| <a id="r-05"></a>**R-05** | Los docentes asesores se resisten a abandonar su Excel y no usan el sistema. | [OB-03](#ob-03), [OB-07](#ob-07) | Migración inicial asistida (plantilla normalizada), capacitación corta y beneficio visible desde la primera semana. |
