# Definición de terminado y evidencia

## Principio

Una tarea no está terminada porque el agente haya dejado de escribir. Está terminada cuando los criterios de aceptación están satisfechos y existe evidencia revisable.

## Requisitos mínimos para `DONE`

1. El alcance coincide con un `TASK_CONTRACT.md` aprobado.
2. Todos los criterios de aceptación de la tarea tienen estado y evidencia.
3. Se registraron los archivos leídos, creados, modificados y eliminados.
4. El diff no incluye cambios ajenos o accidentales.
5. Las comprobaciones obligatorias se ejecutaron o se declararon bloqueadas.
6. Los comandos incluyen código de salida y resultado resumido.
7. No existen defectos críticos abiertos.
8. La documentación afectada está actualizada.
9. Un rol distinto revisó el cambio.
10. Las operaciones externas pendientes permanecen en `NEEDS_APPROVAL`.

## Matriz de evidencia

| Tipo de cambio | Evidencia mínima |
|---|---|
| Documentación | diff, enlaces internos válidos, revisión de coherencia |
| Código | diff, lint o type-check aplicable, pruebas relevantes |
| API | contrato, pruebas de request/response, manejo de errores |
| Datos | esquema, migración reversible, prueba con datos no sensibles |
| Seguridad | amenaza o control revisado, pruebas o análisis aplicable |
| DevOps | configuración, comando reproducible, logs, rollback |
| Arquitectura | alternativas, trade-offs, ADR y aprobación |

## Resultados permitidos de una validación

- `PASS`: comprobación ejecutada y satisfactoria.
- `FAIL`: ejecutada y fallida.
- `BLOCKED`: no pudo ejecutarse por una causa concreta.
- `NOT_APPLICABLE`: no corresponde, con justificación.
- `NOT_RUN`: omitida; impide `DONE` si era obligatoria.

## Prohibiciones

- No sustituir pruebas por una lectura superficial.
- No reducir criterios para hacer que una tarea “pase”.
- No ocultar warnings relevantes.
- No marcar `NOT_APPLICABLE` sin justificación.
- No usar la aprobación del autor como revisión independiente.
- No afirmar cobertura o rendimiento sin medición.

## Reporte de finalización

```text
Task: ...
Role: ...
Status: DONE | NEEDS_REVIEW | NEEDS_REWORK | BLOCKED | NEEDS_APPROVAL
Acceptance criteria:
- AC-001: PASS — evidencia ...
Changed files:
- ...
Commands:
- comando — exit code — resultado
Review:
- reviewer — fecha — resultado
Open risks:
- ...
Next authorized action:
- ...
```

## Definición de terminado del proyecto

Un proyecto solo puede declararse entregado cuando:

- el charter y el alcance están aprobados;
- los requisitos prioritarios tienen evidencia;
- la arquitectura implementada coincide con la documentada o las diferencias están registradas;
- la instalación y ejecución son reproducibles;
- existen pruebas y documentación de operación;
- los riesgos aceptados están explícitos;
- el usuario aprueba la entrega;
- no se confunde “MVP” con “producción”.
