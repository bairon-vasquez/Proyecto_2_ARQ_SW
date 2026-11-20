# language: es
# Traza: [CU-12](../../docs/drivers.md#cu-12), [EAC-01](../../docs/drivers.md#eac-01), [OB-05](../../docs/vision.md#ob-05), [S-07](../../docs/vision.md#s-07), [ADR-007](../../docs/adr/ADR-007-reglas-versionadas.md), [ADR-006](../../docs/adr/ADR-006-bitacora-auditoria.md), [ADR-001](../../docs/adr/ADR-001-monolito-modular.md), [ADR-005](../../docs/adr/ADR-005-autorizacion-por-roles.md)
Característica: Configurar las reglas de práctica de un programa

  Como director de programa
  quiero configurar las reglas de práctica de mi programa
  para aplicar un cambio del reglamento o abrir un programa nuevo sin tocar el código ni afectar las prácticas en curso.

  Antecedentes:
    Dado un director de programa autenticado
    Y un programa que dirige

  Escenario: Crear una versión de reglas en borrador (flujo básico)
    Cuando el director define las horas mínimas y los requisitos académicos del programa
    Entonces se crea una versión de reglas en estado "borrador"
    Y el evento queda registrado en la bitácora

  Escenario: Publicar una versión con vigencia desde el periodo siguiente
    Dado una versión de reglas en "borrador" sin contradicciones
    Cuando el director la publica
    Entonces la versión queda "publicada" con vigencia desde el periodo académico siguiente
    Y el evento queda registrado en la bitácora

  Escenario: Reglas contradictorias no se publican
    Dado una versión de reglas con horas mínimas iguales a cero o con requisitos repetidos o incompatibles
    Cuando el director intenta publicarla
    Entonces la publicación se rechaza
    Y se le indica cada contradicción encontrada
    Pero la versión sigue en "borrador"

  Escenario: Las prácticas en curso conservan su versión de reglas
    Dado una práctica en curso regida por la versión 1 de las reglas
    Cuando se publica la versión 2 del programa
    Entonces la práctica en curso sigue regida por la versión 1
    Y su estado y sus reglas no cambian

  Escenario: Una versión publicada no se edita
    Dado una versión de reglas "publicada"
    Cuando el director intenta modificarla
    Entonces la modificación se rechaza
    Y se le indica que debe crear una versión nueva

  Escenario: Director de otro programa
    Dado un director que no dirige el programa
    Cuando intenta configurar sus reglas
    Entonces el acceso se deniega
    Y el intento queda registrado en la bitácora

  Escenario: Programa nuevo sin tocar el código ([EAC-01](../../docs/drivers.md#eac-01))
    Dado el sistema en operación con prácticas de otros programas en curso
    Cuando un desarrollador con un mes en el proyecto incorpora un programa nuevo con horas mínimas distintas y un requisito adicional
    Entonces lo hace en máximo 12 horas de trabajo
    Y toca como máximo 2 módulos
    Y 0 prácticas en curso de otros programas cambian de estado o de reglas
    Y el servicio no se interrumpe
