# Skill: Inicializar proyecto

## Objetivo

Crear el paquete de control de un nuevo proyecto sin escribir todavía su implementación.

## Rol principal

`@product`, coordinado por `@director`.

## Entradas obligatorias

- idea o problema a resolver;
- propietario humano;
- ubicación prevista del repositorio o indicación de proyecto nuevo;
- referencias conocidas, si existen.

## Procedimiento

1. Asignar un `project_id` estable y legible.
2. Comprobar si ya existe un proyecto con ese identificador.
3. Inspeccionar el repositorio cuando exista; no asumir que está vacío.
4. Crear la carpeta `.ai/` y copiar las plantillas mínimas.
5. Redactar `PROJECT_CHARTER.md` con:
   - propósito;
   - usuarios;
   - alcance inicial;
   - no objetivos;
   - restricciones conocidas;
   - métricas de éxito;
   - riesgos y desconocidos.
6. Redactar `PROJECT_CONSTITUTION.md` con rutas, roles, acciones prohibidas y puertas humanas.
7. Redactar una primera versión de `PROJECT_CONTEXT.md` usando solo hechos verificados.
8. Marcar requisitos o decisiones no proporcionados como `UNKNOWN` o `PROPOSED`.
9. Guardar un `HANDOFF.md` para el siguiente rol.
10. Detener el flujo en `NEEDS_APPROVAL`.

## Salidas

- `.ai/PROJECT_CHARTER.md`;
- `.ai/PROJECT_CONSTITUTION.md`;
- `.ai/PROJECT_CONTEXT.md`;
- `.ai/REQUIREMENTS.md` en borrador;
- `.ai/ACCEPTANCE_CRITERIA.md` en borrador;
- `.ai/HANDOFF.md`.

## Prohibiciones

- No generar código de producto.
- No seleccionar stack definitivo sin análisis y aprobación.
- No inventar usuarios, presupuesto, SLA, integraciones o datos.
- No sobrescribir un paquete `.ai/` existente sin crear respaldo y comparar versiones.
- No registrar secretos.

## Criterio de salida

El skill termina en `NEEDS_APPROVAL`. Solo puede pasar a contexto y arquitectura cuando el charter y la constitución estén aprobados explícitamente.
