# Skill: Planificar iteración

## Objetivo

Convertir un objetivo aprobado en tareas pequeñas, ordenadas, asignables y verificables.

## Rol principal

`@planner`.

## Entradas

- arquitectura aprobada;
- backlog;
- objetivo de iteración;
- capacidad o límite de alcance;
- riesgos y dependencias;
- definición de terminado.

## Procedimiento

1. Seleccionar el menor incremento que produzca valor verificable.
2. Dividirlo en tareas con un único resultado principal.
3. Para cada tarea crear `TASK_CONTRACT.md` con:
   - ID y título;
   - rol ejecutor;
   - precondiciones;
   - archivos de entrada;
   - rutas permitidas y prohibidas;
   - cambio esperado;
   - no objetivos;
   - criterios de aceptación;
   - pruebas obligatorias;
   - riesgos;
   - dependencia de otras tareas;
   - puerta de revisión.
4. Señalar tareas que pueden correr en paralelo y exigir worktrees separados.
5. Añadir tareas de documentación, QA y seguridad cuando sean necesarias.
6. Evitar una tarea “implementar todo el sistema”.
7. Marcar `READY` solo las tareas con contexto y decisiones suficientes.

## Prohibiciones

- No escribir código.
- No ocultar incertidumbre dentro de una estimación.
- No combinar cambios de arquitectura, implementación y despliegue en una única tarea.
- No asignar el mismo agente como autor y revisor.
- No planificar acciones externas sin una puerta humana.

## Criterio de salida

Una tarea está lista cuando un agente puede ejecutarla sin inventar alcance y un revisor puede decidir objetivamente si pasó.
