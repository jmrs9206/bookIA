---
description: Auditar un proyecto en modo lectura y detectar diferencias entre documentos, código y evidencia
---

Cuando el usuario escriba `/auditar_proyecto <project_id>`:

1. Activar modo de solo lectura.
2. Cargar contexto con `@context`.
3. Revisar con `@reviewer`, `@qa` y `@security` sin editar archivos de implementación.
4. Comparar:
   - charter y alcance;
   - requisitos y AC;
   - arquitectura documentada e implementada;
   - dependencias y licencias;
   - pruebas declaradas y evidencia;
   - secretos y permisos;
   - estado Git y documentación.
5. Clasificar hallazgos por severidad y procedencia.
6. Guardar un informe de auditoría.
7. No corregir automáticamente; convertir correcciones en propuestas de tareas.
