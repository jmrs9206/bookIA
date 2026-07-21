# Skill: Actualizar memoria persistente

## Objetivo

Guardar solo conocimiento verificado que permita continuar un proyecto sin contaminar otros contextos.

## Rol principal

`@memory`.

## Entradas

- decisiones aprobadas;
- evidencia de tareas cerradas;
- cambios de arquitectura;
- riesgos y problemas abiertos;
- namespace del proyecto.

## Procedimiento

1. Seleccionar únicamente hechos o decisiones con fuente.
2. Clasificar cada elemento por ámbito: global, organización, proyecto, iteración o tarea.
3. Rechazar secretos, datos personales y contenido no necesario.
4. Registrar:
   - afirmación;
   - tipo;
   - fuente;
   - fecha;
   - confianza;
   - caducidad o condición de revalidación;
   - owner.
5. Detectar conflictos con memoria existente.
6. No sobrescribir una decisión previa; registrar supersesión.
7. Promover a memoria global solo patrones genéricos revisados.

## Prohibiciones

- No guardar conversaciones completas.
- No guardar una propuesta como decisión.
- No compartir memoria de proyecto sin importación explícita.
- No mantener hechos sin fecha o fuente.

## Criterio de salida

Un agente nuevo puede recuperar decisiones y hechos relevantes, verificar su origen y saber qué elementos deben revalidarse.
