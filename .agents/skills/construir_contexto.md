# Skill: Construir contexto de proyecto o tarea

## Objetivo

Preparar un contexto pequeño, vigente y verificable para que el siguiente agente no dependa de una conversación anterior.

## Rol principal

`@context`.

## Entradas

- `project_id`;
- repositorio y commit actuales;
- artefactos aprobados de `.ai/`;
- tarea o etapa objetivo;
- rol receptor.

## Procedimiento

1. Verificar que el proyecto, repositorio y branch/worktree coinciden.
2. Leer únicamente los artefactos aprobados y el estado real relevante.
3. Crear o actualizar el mapa del repositorio con rutas que existan.
4. Resumir:
   - propósito;
   - alcance activo;
   - arquitectura actual y objetivo;
   - restricciones;
   - decisiones vigentes;
   - interfaces relevantes;
   - criterios de aceptación;
   - riesgos;
   - desconocidos.
5. Etiquetar cada elemento como `FACT`, `INFERENCE`, `PROPOSAL` o `UNKNOWN`.
6. Eliminar datos obsoletos o marcarlos `STALE`; no borrarlos sin rastro.
7. Definir el conjunto mínimo de archivos que el siguiente rol debe leer.
8. Registrar versión de contexto y fecha de verificación.

## Salidas

- `.ai/PROJECT_CONTEXT.md` actualizado;
- bloque `Task Context` dentro de `TASK_CONTRACT.md` cuando aplique;
- lista de fuentes y archivos leídos;
- handoff al rol receptor.

## Prohibiciones

- No comprimir hasta perder restricciones críticas.
- No incluir secretos ni datos de otros proyectos.
- No resolver conflictos de decisión por cuenta propia.
- No usar memoria conversacional como única fuente.
- No incluir archivos inexistentes.

## Criterio de salida

El contexto es suficiente cuando un agente nuevo puede explicar la tarea, sus límites, sus fuentes y su criterio de terminado sin necesitar la conversación original.
