# Skill: Revisar cambios

## Objetivo

Realizar una revisión independiente del cambio contra contrato, arquitectura, seguridad y evidencia.

## Rol principal

`@reviewer`, con apoyo de `@security` o `@qa` cuando aplique.

## Entradas

- `TASK_CONTRACT.md`;
- diff o commit local;
- `EVIDENCE_LOG.md`;
- arquitectura y convenciones relevantes;
- identidad del autor.

## Procedimiento

1. Confirmar que el revisor no es el autor.
2. Verificar que el diff corresponde al alcance.
3. Comprobar coherencia funcional, manejo de errores y casos límite.
4. Revisar contratos públicos, migraciones y compatibilidad.
5. Buscar secretos, permisos excesivos, entradas no validadas y dependencias riesgosas.
6. Validar que las pruebas alegadas fueron ejecutadas y que su alcance es suficiente.
7. Ejecutar checks adicionales cuando sean seguros.
8. Clasificar hallazgos:
   - `BLOCKER`;
   - `MAJOR`;
   - `MINOR`;
   - `NOTE`.
9. Emitir una única decisión:
   - `APPROVE_FOR_QA`;
   - `REQUEST_CHANGES`;
   - `BLOCKED`.

## Prohibiciones

- No aprobar por estilo o confianza en el autor.
- No editar silenciosamente el código y aprobarlo.
- No introducir requisitos nuevos como defectos.
- No ignorar tests no ejecutados.
- No autorizar merge o despliegue.

## Salida

Informe con hallazgos, archivo/línea o evidencia, impacto, acción requerida y estado final.
