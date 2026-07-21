---
description: Crear el paquete de control de un nuevo proyecto sin comenzar a programar
---

Cuando el usuario escriba `/nuevo_proyecto <idea>`, ejecutar esta secuencia:

1. Actuar como `@director` y generar un `project_id` provisional.
2. Activar `inicializar_proyecto.md` con `@product`.
3. Si existe repositorio, activar `construir_contexto.md` con `@context`.
4. Registrar referencias mencionadas, pero no analizarlas todavía salvo que sean necesarias para el charter.
5. Presentar un resumen con:
   - propósito;
   - alcance;
   - no objetivos;
   - restricciones;
   - desconocidos;
   - criterios de éxito;
   - archivos creados.
6. Cambiar el estado a `NEEDS_APPROVAL`.
7. Detener la secuencia. No diseñar arquitectura ni generar código hasta que el usuario apruebe el charter y la constitución.

Si el identificador ya existe, no sobrescribir. Ejecutar `/continuar_proyecto <project_id>` o proponer un ID distinto.
