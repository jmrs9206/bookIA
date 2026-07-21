# Skill: Ejecutar tarea de implementación

## Objetivo

Implementar exactamente una tarea aprobada dentro de un workspace aislado y producir evidencia completa.

## Roles permitidos

`@frontend`, `@backend`, `@integration`, `@devops` o `@docs`, según el contrato.

## Precondiciones

- tarea en estado `READY`;
- rol activo coincide con el asignado;
- repositorio, branch/worktree y run identificados;
- rutas autorizadas definidas;
- contexto cargado;
- no existe una puerta humana pendiente.

## Procedimiento

1. Leer el contrato y repetir internamente alcance, no objetivos y pruebas.
2. Inspeccionar archivos reales antes de editar.
3. Registrar estado Git inicial.
4. Elegir el cambio mínimo que satisface el contrato.
5. Implementar solo en rutas autorizadas.
6. No añadir dependencias salvo que el contrato lo contemple; de hacerlo, justificar y revisar licencia.
7. Ejecutar comprobaciones tempranas y corregir errores dentro del alcance.
8. Revisar el diff para detectar cambios accidentales, secretos o archivos generados.
9. Actualizar documentación y evidencia.
10. Crear `HANDOFF.md` para revisión independiente.

## Salidas

- diff limitado;
- pruebas o checks con resultados reales;
- `EVIDENCE_LOG.md` actualizado;
- lista de decisiones o desviaciones;
- estado `NEEDS_REVIEW`, `BLOCKED` o `NEEDS_APPROVAL`.

## Prohibiciones

- No ampliar el alcance para “mejorar” otras áreas.
- No editar archivos prohibidos.
- No inventar APIs, respuestas o datos.
- No silenciar fallos para obtener verde.
- No hacer push, merge, release o deploy.
- No marcar `DONE`; la revisión corresponde a otro rol.

## Protocolo de bloqueo

Cuando el contrato sea imposible o contradictorio:

```text
BLOCKED
Motivo: ...
Evidencia: ...
Impacto: ...
Opciones seguras: ...
Decisión requerida: ...
```
