# Ronda 2: Drivers arquitectónicos

**Fuentes:** `4. Drivers.pdf` y `Taller_Drivers_Solucion_Practicas.pdf`.
**Nuestro entregable:** [`practicas-empresariales/docs/drivers.md`](../practicas-empresariales/docs/drivers.md)

---

## 1. Análisis de las diapositivas

### 1.1 Qué es un driver
Un driver es un requisito que, si cambiara radicalmente, **obligaría a rediseñar la estructura**. Son un subconjunto pequeño (10–20 de ~150 requisitos) y permiten empezar a diseñar antes de terminar la especificación. Son la salida de "requerimientos de la arquitectura" y la entrada del "diseño".

### 1.2 Los cuatro tipos

| # | Tipo | Peso | Idea |
|---|---|---|---|
| 1 | Casos de uso primarios (5–10, si hay 40 no se priorizó) | Medio | Los que son razón de ser, complejos, frecuentes, riesgosos o atados a un atributo crítico |
| 2 | Escenarios de atributos de calidad | **Alto** | Mandan: dos sistemas con igual funcionalidad tienen arquitecturas distintas por sus atributos (blog vs. red social) |
| 3 | Restricciones | Alto | Eliminan alternativas; en drivers se enriquecen con "impacto arquitectónico" (p. ej. PostgreSQL ⇒ relacional) |
| 4 | Preocupaciones arquitectónicas | Medio | Transversales que nadie pidió: estructura, authN/authZ, errores, trazabilidad, configuración, entornos, migración |

### 1.3 ISO/IEC 25010:2023
9 características / 40 subcaracterísticas. Puntos que la diapositiva destaca y que es fácil confundir:
- La **escalabilidad** es subcaracterística de *Flexibilidad*; la **disponibilidad** de *Fiabilidad*; la **testabilidad** de *Mantenibilidad*.
- **Seguridad (security)** protege al sistema de personas; **Protección (safety)** protege a las personas del sistema.
- Parejas confusas: desempeño≠escalabilidad, escalabilidad≠elasticidad, disponibilidad≠ausencia de fallos, tolerar≠recuperar.
- La adecuación funcional casi nunca es driver; la cubren los casos de uso primarios.

### 1.4 Trade-offs
- "No hay tácticas gratis": cada táctica mejora un atributo y paga otro (caché ↔ consistencia; cifrado ↔ latencia; capas ↔ saltos; distribuir ↔ simplicidad).
- Cuatro ejemplos numéricos: seguridad vs. desempeño (135→102 ms optimizando sin quitar controles), disponibilidad vs. costo (cada nueve ×3, ×10, ×30), mantenibilidad vs. desempeño (2 vs. 5 saltos), escalabilidad vs. simplicidad (**monolito modular primero**; separar solo con un escenario medido).
- Proceso: priorizar 3–4 atributos con el cliente → escenarios medibles → evaluar tácticas → ADR (método formal: ATAM).

### 1.5 Escenario de atributo de calidad (6 partes)
Fuente, estímulo, artefacto, entorno, respuesta, **medida de respuesta**. "Debe ser rápido" no sirve porque no es verificable ni diseñable ni negociable. La medida con número es lo que más pesa en la evaluación.

### 1.6 Priorización
Matriz importancia (la da el cliente) × dificultad técnica (la da el arquitecto): *hacer ya*, **atender primero**, *si sobra tiempo*, *cuestionar*.

---

## 2. Análisis del taller resuelto por el docente

### 2.1 Lo que pide
≥12 casos de uso con ≤6 primarios y criterio justificado; 3 EAC completos de atributos distintos (≥1 de mantenibilidad); tabla de restricciones (ID, tipo, origen, impacto); 5 preocupaciones; matriz con los cuatro cuadrantes.

### 2.2 Qué entregó el docente
- **15 casos de uso**, 5 primarios: CU-01 Postularse (complejidad, SIA), CU-07 Evaluar (riesgo, usuario externo), CU-09 Acta (importancia), CU-10 Aprobar acta (atributo crítico), CU-12 Reglas (mantenibilidad).
- **3 EAC:** EAC-01 modificabilidad (16 h, ≤2 módulos, 0 prácticas afectadas), EAC-02 tolerancia a fallos del SIA (5 s, 30 usuarios, confirmación <3 s p95, 30 min), EAC-03 seguridad del enlace (100 % rechazados, <1 min en bitácora).
- **9 restricciones** con impacto (descartan nube pública, obligan adaptador SIA, etc.).
- **5 PA:** estructura, authN/authZ, trazabilidad, errores de integración, **migración inicial**.
- **22 drivers** en total y matriz con 4 cuadrantes ocupados (PA-05 migración en "cuestionar").

### 2.3 Qué hace bien
- Cada CU no primario explica *por qué no*, con razones arquitectónicas (CU-07 de horas "es frecuente pero son ≤250 registros por semana").
- Las medidas son todas numéricas y verificables.
- Trazas a la visión (OB, S, RT, R) en cada escenario.
- Usa la matriz para decidir orden de ADR e implementación posterior.

### 2.4 Observaciones críticas
- Los EAC cubren **mantenibilidad, fiabilidad y seguridad**, pero **no hay ninguno de eficiencia de desempeño**, pese a que OB-01 es un objetivo de tiempo (días hábiles hasta el acta). Es un hueco: nadie verifica que generar el acta sea rápido.
- **CU-07 aparece como "baja dificultad"** en la matriz a pesar de haber sido justificado como primario por *riesgo*; es una inconsistencia entre CU y matriz.
- Un CU primario por "riesgo" (migración) se degrada a **preocupación** (PA-05) y termina en "cuestionar": decisión defendible, pero la migración define el primer despliegue y es incierta; en nuestra versión es primaria.
- Las restricciones RT-04 y RN-05 quedan en baja prioridad aunque descartan alternativas completas (plataformas comerciales, tecnologías fuera de catálogo); su influencia es alta aunque su dificultad sea baja.
- La traza del EAC-01 menciona CU-12 pero no se verifica en qué specs se probaría (es el vínculo que SDD pide después).

---

## 3. Nuestra versión: decisiones de diferencia

| Aspecto | Docente | Nuestra versión | Por qué |
|---|---|---|---|
| CU primarios | 5 | **6** (CU-01, 07, 09, 10, 12 y **15**) | La migración es riesgo (criterio 4) y define el primer despliegue |
| EAC | 3 (mant., fiab., seg.) | **4**: se agrega **eficiencia de desempeño** (EAC-04, acta <10 s p95, CPU <70 %) | Cubrir OB-01/OB-04 con un número verificable |
| EAC-01 | 16 h, 2 módulos | **12 h**, 2 módulos, **0 min de indisponibilidad** | Se añade operación continua |
| EAC-02 | SIA 5 s, 30 usuarios, 30 min | SIA **4 s**, **40** usuarios, confirmación <**2 s**, **20 min** | Medidas propias, más exigentes |
| EAC-03 | Rechazo + bitácora <1 min | Igual + **aviso al docente en <10 min** | Cierra el ciclo de respuesta |
| PA | 5 (incluye migración) | 5 (**cambia migración por configuración y entornos**, PA-05) | Migración ya es CU-15 |
| Matriz | CU-07 en baja dificultad | CU-07 en **alta dificultad** | Coherencia con su justificación |
| Extras | — | Sección 6 con la **tabla de escenarios (+1)** | Lo exigen las diapositivas de vistas; se prepara desde ahora |

➡️ Documento final: [`docs/drivers.md`](../practicas-empresariales/docs/drivers.md).
