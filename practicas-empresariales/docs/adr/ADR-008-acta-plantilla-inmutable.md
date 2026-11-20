# ADR-008: Acta final generada de forma síncrona desde una plantilla externa y conservada como documento inmutable

## Estado
Aceptado — 2026-11-17

## Contexto
[CU-09](../drivers.md#cu-09) genera el acta final, razón de ser del sistema, de la que dependen [OB-01](../vision.md#ob-01) y [OB-04](../vision.md#ob-04) (menos del 1 % de actas reemitidas). [EAC-04](../drivers.md#eac-04-eficiencia-de-desempeño-comportamiento-temporal) exige generarla en menos de 10 s (p95) con hasta 30 docentes a la vez. [RN-03](../drivers.md#rn-03) obliga a seguir el formato del reglamento, que puede cambiar por decisión del Consejo, y [RN-02](../drivers.md#rn-02) a conservar actas según la tabla de retención. [CU-10](../drivers.md#cu-10) exige aprobación del docente asesor y del director ([S-06](../vision.md#s-06)), aunque [R-03](../vision.md#r-03) advierte que podría exigirse firma digital certificada.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| A) Acta construida directamente en el código | Sin dependencias adicionales | Cambiar el formato ([RN-03](../drivers.md#rn-03)) exige programar y desplegar |
| B) Plantilla separada del código, llenada con los datos de la práctica y convertida a PDF **en la misma petición**; el PDF aprobado se guarda como documento inmutable con su hash | El formato cambia sin reprogramar; sin transcripción ([OB-04](../vision.md#ob-04)); el acta aprobada no se altera ([RN-02](../drivers.md#rn-02)) | Hay que versionar plantillas y mantener la librería de PDF; la petición dura segundos |
| C) Generar un Word que el docente complete a mano | Fácil | Reintroduce los errores de transcripción que [OB-04](../vision.md#ob-04) quiere eliminar |
| D) Variante de B con generación asíncrona por cola | No bloquea al usuario | Complejidad innecesaria: con 30 usuarios y un PDF de 1–2 páginas, B cumple [EAC-04](../drivers.md#eac-04) |

## Decisión
Se elige **B** (síncrona, sin cola). El acta se genera con los datos registrados y pasa por dos aprobaciones: primero el docente asesor y después el director ([CU-10](../drivers.md#cu-10)), ambas en la bitácora ([ADR-006](ADR-006-bitacora-auditoria.md)). Al aprobarse se guarda el PDF con su hash SHA-256 en el almacenamiento institucional; no se modifica ni se borra. Un error se corrige emitiendo una nueva acta que referencia a la anterior. La aprobación queda detrás de un puerto, de modo que una futura firma digital certificada ([R-03](../vision.md#r-03)) sea un adaptador nuevo.

## Consecuencias
**Positivas.** El formato sigue al reglamento sin reprogramar ([RN-03](../drivers.md#rn-03)); actas íntegras ([RN-02](../drivers.md#rn-02)); sin transcripción ([OB-04](../vision.md#ob-04)); se cumple [EAC-04](../drivers.md#eac-04) sin infraestructura extra.

**Negativas (costos aceptados).** Se agrega la librería de PDF y el versionado de plantillas; la generación consume CPU del servidor de aplicaciones en el pico de cierre.

**Riesgos.** Que se exija firma digital certificada ([R-03](../vision.md#r-03)) o que el pico supere [EAC-04](../drivers.md#eac-04). Mitigación: puerto de aprobación sustituible; si el p95 supera 10 s, un ADR nuevo pasa la generación a segundo plano (alternativa D).

## Vistas que modifica
[Lógica](../vistas/01-logica.md) (`Acta`, `PlantillaActa`), [Procesos](../vistas/02-procesos.md), [Física](../vistas/04-fisica.md) (almacenamiento institucional)
