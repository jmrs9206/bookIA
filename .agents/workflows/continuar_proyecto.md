---
description: Reanudar un proyecto desde sus artefactos persistentes y estado Git
---

Cuando el usuario escriba `/continuar_proyecto <project_id>`:

1. Actuar en modo lectura como `@director`.
2. Localizar el registro y repositorio del proyecto.
3. Verificar branch, commit, estado Git y paquete `.ai/`.
4. Activar `construir_contexto.md` con `@context`.
5. Comparar estado documentado y estado real.
6. Marcar conflictos, archivos obsoletos y runs incompletos.
7. Resumir:
   - último hito verificado;
   - tareas abiertas;
   - decisiones pendientes;
   - riesgos;
   - siguiente acción permitida.
8. No modificar código ni asumir que la última conversación terminó correctamente.
9. Esperar una orden de planificación, ejecución o auditoría.
