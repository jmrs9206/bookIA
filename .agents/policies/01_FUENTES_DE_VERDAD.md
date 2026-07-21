# Fuentes de verdad y procedencia

## Objetivo

Evitar que la IA trate recuerdos, inferencias o documentación obsoleta como hechos actuales.

## Orden de precedencia

De mayor a menor autoridad:

1. **Instrucción humana explícita y vigente** para el proyecto o la tarea actual.
2. **Artefactos aprobados del proyecto**, con estado, versión y fecha.
3. **Repositorio actual**, incluido el contenido real de archivos, historial, rama, commit y lockfiles.
4. **Resultados de herramientas**, como pruebas, builds, linters, consultas y salidas de comandos.
5. **Documentación oficial o fuente primaria**, idealmente fijada a versión o fecha.
6. **Análisis de repositorios de referencia**, con URL, commit y licencia registrados.
7. **Memoria del proyecto**, solo cuando contenga procedencia y fecha de verificación.
8. **Inferencias técnicas**, siempre etiquetadas.
9. **Preferencias o propuestas de la IA**, nunca tratadas como requisitos.

## Reglas de lectura

- La existencia de un nombre en un documento no demuestra que el archivo, endpoint o componente exista.
- Un README describe intención; el código y las pruebas describen el estado implementado.
- Un archivo generado anteriormente puede estar obsoleto. Verificarlo contra el repositorio actual.
- Una salida de herramienta tiene autoridad solo para la ejecución concreta registrada.
- Un resultado exitoso en una máquina no demuestra compatibilidad universal.
- Un ejemplo de documentación no es una configuración aprobada para el proyecto.

## Etiquetas de conocimiento

Usar estas etiquetas en análisis, handoffs y decisiones:

- `[FACT]`: verificado directamente.
- `[INFERENCE]`: conclusión derivada de hechos citados.
- `[PROPOSAL]`: opción recomendada, no aprobada.
- `[ASSUMPTION]`: supuesto temporal y reversible.
- `[UNKNOWN]`: dato ausente o no verificable.
- `[CONFLICT]`: dos fuentes autorizadas se contradicen.
- `[STALE]`: información probablemente desactualizada.

## Registro mínimo de una afirmación relevante

```text
Tipo: FACT | INFERENCE | PROPOSAL | ASSUMPTION | UNKNOWN
Afirmación: ...
Fuente: ruta, comando, URL o artefacto
Versión/commit: ...
Verificado: AAAA-MM-DD
Confianza: alta | media | baja
Impacto si es falso: bajo | medio | alto
```

## Reglas para repositorios de referencia

Antes de usar un patrón externo, registrar:

- URL y propietario;
- rama y commit analizado;
- licencia declarada;
- archivos que sustentan el patrón;
- diferencia entre idea, interfaz y código literal;
- compatibilidad con el proyecto destino;
- decisión de adoptar, adaptar, experimentar o rechazar.

## Resolución de discrepancias

Cuando la documentación diga una cosa y la implementación otra:

- describir ambas;
- considerar el código actual como estado implementado;
- considerar la documentación como intención o deuda;
- no corregir automáticamente ninguna de las dos sin una tarea aprobada.

## Memoria aceptable

La memoria persistente solo puede almacenar:

- decisiones aprobadas;
- hechos verificados;
- resultados reproducibles;
- restricciones vigentes;
- enlaces o rutas de procedencia;
- problemas abiertos claramente etiquetados.

No se almacenan como hechos:

- ideas no aprobadas;
- mensajes ambiguos;
- resultados no reproducidos;
- predicciones;
- credenciales;
- contenido de otros proyectos sin autorización.
