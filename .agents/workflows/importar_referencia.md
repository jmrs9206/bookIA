---
description: Analizar una referencia externa y registrar patrones con procedencia y licencia
---

Cuando el usuario escriba `/importar_referencia <URL_o_ruta> [project_id]`:

1. Actuar como `@director` y confirmar el proyecto receptor.
2. Activar `investigar_referencia.md` con `@research`.
3. Exigir URL/ruta, commit o versión y licencia.
4. Guardar el resultado en `.ai/references/<slug>/REFERENCE_ANALYSIS.md`.
5. Activar una revisión breve con `@architect` para clasificar cada patrón como `ADOPT`, `ADAPT`, `EXPERIMENT` o `REJECT`.
6. No modificar código del proyecto.
7. No copiar código de la referencia.
8. Finalizar en `NEEDS_APPROVAL` si la recomendación implica una decisión de arquitectura o dependencia.
