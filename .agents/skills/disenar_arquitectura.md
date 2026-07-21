# Skill: Diseñar arquitectura

## Objetivo

Definir una arquitectura objetivo compatible con requisitos, restricciones y estado actual, distinguiendo claramente lo existente de lo propuesto.

## Rol principal

`@architect`.

## Precondiciones

- charter aprobado;
- requisitos prioritarios identificados;
- contexto verificado;
- referencias registradas;
- riesgos y restricciones conocidos.

## Procedimiento

1. Documentar el estado `CURRENT` con evidencia del repositorio.
2. Identificar atributos de calidad: seguridad, mantenibilidad, aislamiento, trazabilidad, rendimiento y coste.
3. Proponer al menos dos opciones cuando la decisión sea significativa.
4. Comparar trade-offs, riesgos, reversibilidad y dependencias.
5. Diseñar el estado `TARGET`:
   - componentes;
   - responsabilidades;
   - interfaces;
   - modelo de datos;
   - flujo de trabajo;
   - estados y errores;
   - aislamiento por proyecto;
   - observabilidad;
   - permisos y puertas.
6. Crear ADR para cada decisión que limite opciones futuras.
7. Definir un camino incremental desde `CURRENT` a `TARGET`.
8. Identificar qué se reutiliza como patrón de MiroFish y qué se reimplementa de forma independiente.
9. Marcar dependencias como `CONFIRMED`, `CANDIDATE` o `UNKNOWN`.
10. Solicitar aprobación para decisiones de alto impacto.

## Salidas

- `.ai/ARCHITECTURE.md`;
- `.ai/decisions/ADR-XXX.md`;
- actualización de `RISK_REGISTER.md`;
- recomendación de MVP y límites explícitos.

## Prohibiciones

- No escribir implementación.
- No elegir tecnología por moda.
- No diseñar una plataforma distribuida si un proceso local satisface el MVP.
- No presentar un componente futuro como existente.
- No adoptar una dependencia externa sin analizar licencia, operación y salida.

## Criterio de salida

La arquitectura debe permitir que `@planner` genere tareas pequeñas y que un revisor pueda rastrear cada componente a un requisito o restricción.
