# Aislamiento de proyectos y sesiones

## Objetivo

Permitir que un único Gemini CLI y una única instalación de Antigravity trabajen con múltiples proyectos sin contaminación de contexto ni colisiones de archivos.

## Identidad mínima de ejecución

Toda ejecución debe estar asociada a:

```text
project_id
repository_root
branch_or_worktree
run_id
active_role
active_task_id
context_version
memory_namespace
allowed_paths
```

Si falta `project_id` o `repository_root`, la ejecución no puede modificar archivos.

## Qué puede compartirse

- binario de Gemini CLI;
- autenticación del usuario;
- adaptador del orquestador;
- políticas globales;
- biblioteca de patrones aprobados;
- plantillas y skills versionadas.

## Qué no puede compartirse implícitamente

- sesión conversacional activa;
- historial de tareas;
- memoria del proyecto;
- secretos;
- variables de entorno;
- worktree;
- rama;
- artefactos temporales;
- criterios de aceptación;
- decisiones de arquitectura;
- datos de pruebas.

## Regla de sesión

Cada `run_id` utiliza una sesión independiente. Reanudar una sesión solo es válido para el mismo proyecto, la misma rama o worktree y una tarea compatible.

No se reutiliza una conversación de Proyecto A para Proyecto B aunque el modelo, el usuario y la tecnología sean los mismos.

## Regla de filesystem

- El agente puede escribir únicamente en `allowed_paths`.
- Las rutas deben resolverse y comprobarse antes de escribir.
- Los enlaces simbólicos que salgan del workspace se consideran no autorizados.
- Los archivos temporales se guardan bajo el directorio del run.
- Los artefactos compartidos se copian mediante un proceso de importación explícito.

## Paralelismo

Para tareas paralelas:

- un worktree o clon aislado por tarea de escritura;
- una rama por tarea;
- una sesión por tarea;
- un log y un `EVIDENCE_LOG.md` por tarea;
- coordinación de archivos compartidos antes de integrar;
- revisión de conflictos por un rol de integración.

## Memoria por capas

1. **Global**: políticas y patrones genéricos.
2. **Organización**: convenciones del orquestador.
3. **Proyecto**: hechos y decisiones del proyecto.
4. **Iteración**: objetivos y riesgos de la iteración.
5. **Tarea**: contexto mínimo para ejecutar una unidad de trabajo.

Las capas inferiores pueden heredar reglas superiores, pero no escribir en ellas automáticamente.

## Importación entre proyectos

Un aprendizaje de Proyecto A solo puede promoverse a la biblioteca global cuando:

- es genérico;
- no contiene secretos ni propiedad específica;
- tiene evidencia;
- se revisó su licencia y procedencia;
- fue aprobado por el Memory Steward o el usuario.

## Cierre de sesión

Al cerrar un run, producir un handoff con:

- estado;
- commit o diff;
- archivos cambiados;
- pruebas;
- decisiones;
- desconocidos;
- siguiente acción permitida.

La sesión puede descartarse después porque el estado operativo queda persistido en artefactos.
