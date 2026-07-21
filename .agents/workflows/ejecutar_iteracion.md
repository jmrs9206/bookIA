---
description: Ejecutar una iteración aprobada con aislamiento, revisión y evidencia
---

Cuando el usuario escriba `/ejecutar_iteracion <project_id> [iteration_id]`:

1. Actuar como `@director`.
2. Reconstruir el estado desde disco; no confiar en la conversación.
3. Verificar charter, arquitectura, backlog, tareas `READY` y ausencia de puertas pendientes.
4. Activar `construir_contexto.md` para la iteración.
5. Para cada tarea seleccionada:
   - crear o confirmar branch/worktree y `run_id` aislados;
   - asignar un solo rol ejecutor;
   - activar `ejecutar_tarea.md`;
   - activar `revisar_cambios.md` con un rol distinto;
   - si hay cambios solicitados, crear una tarea de rework y repetir;
   - activar `validar_proyecto.md` con `@qa`.
6. No integrar una tarea que no tenga revisión y evidencia.
7. Al terminar, activar `cerrar_iteracion.md`.
8. Finalizar en `NEEDS_APPROVAL` para merge/push/release, o `NEEDS_REWORK`/`BLOCKED` cuando corresponda.
9. Nunca ejecutar automáticamente la acción externa pendiente.
