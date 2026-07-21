---
description: Mostrar el estado verificable de un proyecto sin modificarlo
---

Cuando el usuario escriba `/estado_proyecto <project_id>`:

1. Operar en modo lectura.
2. Verificar repositorio, branch/commit y versión de contexto.
3. Informar únicamente:
   - estado del proyecto;
   - iteración activa;
   - tareas por estado;
   - última evidencia válida;
   - decisiones pendientes;
   - bloqueos;
   - riesgos principales;
   - próxima acción autorizada.
4. Etiquetar cualquier discrepancia como `CONFLICT` o `STALE`.
5. No afirmar progreso basado solo en mensajes anteriores.
