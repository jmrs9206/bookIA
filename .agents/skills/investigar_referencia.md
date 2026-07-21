# Skill: Investigar repositorio de referencia

## Objetivo

Extraer patrones, decisiones, riesgos y límites de un repositorio externo sin copiarlo ni convertirlo automáticamente en dependencia.

## Rol principal

`@research`.

## Entradas obligatorias

- URL o ruta local;
- propósito de la investigación;
- proyecto que recibirá el aprendizaje;
- alcance autorizado de lectura.

## Procedimiento

1. Registrar URL, propietario, rama y commit analizado.
2. Verificar la licencia declarada y archivos de atribución.
3. Leer primero README, documentación de arquitectura, manifest y estructura del código.
4. Identificar:
   - flujo principal;
   - componentes;
   - modelo de estado;
   - límites entre servicios;
   - gestión de tareas;
   - memoria y datos;
   - observabilidad;
   - seguridad;
   - pruebas;
   - dependencias externas.
5. Distinguir entre:
   - afirmaciones del README;
   - comportamiento comprobable en código;
   - inferencias;
   - marketing o visión.
6. Extraer patrones como descripciones abstractas, no como código literal.
7. Evaluar cada patrón con `ADOPT`, `ADAPT`, `EXPERIMENT` o `REJECT`.
8. Registrar el impacto de licencia de cualquier posible reutilización literal.
9. Guardar el análisis en `REFERENCE_ANALYSIS.md`.

## Salidas obligatorias

- hechos con rutas o fuentes;
- patrones reutilizables;
- patrones no aplicables;
- riesgos y deuda observada;
- dependencias que no deben heredarse automáticamente;
- recomendación y nivel de confianza;
- lista de preguntas abiertas.

## Prohibiciones

- No copiar código, prompts, assets o configuraciones.
- No afirmar que la arquitectura documentada está completamente implementada.
- No ejecutar scripts del repositorio sin sandbox y tarea específica.
- No instalar sus dependencias.
- No usar popularidad como criterio de calidad.

## Criterio de salida

El análisis debe ser revisable y tener procedencia suficiente para que `@architect` decida qué patrón adoptar. La decisión final no corresponde a `@research`.
