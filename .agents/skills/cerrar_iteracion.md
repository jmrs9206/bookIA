# Skill: Cerrar iteración

## Objetivo

Consolidar el resultado de una iteración, impedir cierres ficticios y preparar la decisión humana de integración.

## Roles

`@director`, `@reviewer`, `@qa`, `@docs` y `@memory`.

## Procedimiento

1. Recopilar tareas y estados.
2. Verificar que ninguna tarea requerida quede en `IN_PROGRESS` o sin evidencia.
3. Resumir cambios por requisito, no por cantidad de archivos.
4. Consolidar pruebas, defectos, riesgos y deuda.
5. Comparar arquitectura implementada con arquitectura aprobada.
6. Actualizar documentación y memoria.
7. Generar `ITERATION_REPORT.md`.
8. Determinar:
   - `NEEDS_REWORK` si hay fallos;
   - `BLOCKED` si falta evidencia;
   - `NEEDS_APPROVAL` si el incremento está listo para integrar.
9. Mostrar exactamente qué acción externa se propone: merge, push, release o ninguna.
10. Esperar aprobación humana para cualquier integración externa.

## Prohibiciones

- No hacer merge o push como parte automática del cierre.
- No ocultar tareas fallidas.
- No convertir riesgos aceptados implícitamente.
- No declarar el proyecto terminado si solo cerró una iteración.
