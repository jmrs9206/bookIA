# Especificación Detallada del Workflow de Creación de Libros KDP (bookIA)

## Visión General del Proceso

El workflow de `bookIA` transforma una noción de nicho en un producto editorial completo listo para publicar en Amazon KDP mediante 10 fases consecutivas respaldadas por agentes de IA y controles de calidad.

```mermaid
flowchart TD
    F1[1. Selección de Nicho e Investigación] --> F2[2. Investigación de Palabras Clave KDP]
    F2 --> F3[3. Diseño de la Tabla de Contenidos / Índice]
    F3 --> F4[4. Generación Modular del Borrador con IA]
    F4 --> F5[5. Revisión y Ampliación de Contenido]
    F5 --> F6[6. Corrección Ortográfica y de Estilo]
    F6 --> F7[7. Diseño de Portada y Asset Gráficos]
    F7 --> F8[8. Maquetación KDP (PDF / EPUB)]
    F8 --> F9[9. Kit de Metadatos y Publicación en KDP]
    F9 --> F10[10. Estrategia de Lanzamiento, Promoción y Reseñas]
```

---

## Detalle por Fase

### Fase 1: Selección del Nicho
- **Rol asignado**: `@product` / `@research`
- **Entradas**: Preferencia del autor, catálogo objetivo (Práctico, Actividades, Ficción).
- **Acciones**:
  - Evaluación de demanda vs competencia en Amazon.
  - Definición del público objetivo (buyer persona).
- **Entregable**: `nicho_selected.md` con justificación de viabilidad.

### Fase 2: Investigación de Palabras Clave
- **Rol asignado**: `@research`
- **Acciones**:
  - Identificación de 7 frases/keywords principales para backend de KDP.
  - Selección de categorías BISAC / KDP relevantes.
  - Análisis de títulos y subtítulos de los top 5 competidores.
- **Entregable**: `keywords_and_categories.md`.

### Fase 3: Estructura del Libro (Índice / TOC)
- **Rol asignado**: `@architect` / `@editor`
- **Acciones**:
  - Creación del índice detallado: Introducción, 8-15 Capítulos (con 3-5 subsecciones cada uno), Conclusión.
  - Definición de elementos especiales (ejercicios, resumen de capítulo, tablas explicativas).
- **Entregable**: `book_outline.md`.

### Fase 4: Generación Modular del Borrador
- **Rol asignado**: `@writer` / `@planner`
- **Acciones**:
  - Redacción capítulo a capítulo para evitar pérdida de contexto o respuestas genéricas.
  - Aplicación de prompts avanzados con instrucciones de tono, densidad informativa y ejemplos reales.
- **Entregable**: `draft_raw/chapter_XX.md`.

### Fase 5: Revisión y Ampliación de Contenido
- **Rol asignado**: `@editor`
- **Acciones**:
  - Eliminación de muletillas o frases repetitivas típicas de modelos de lenguaje.
  - Incorporación de casos de estudio, guías paso a paso y datos complementarios.
- **Entregable**: `draft_reviewed/chapter_XX.md`.

### Fase 6: Corrección de Estilo y Ortotipografía
- **Rol asignado**: `@reviewer` / `@qa`
- **Acciones**:
  - Verificación gramatical, consistencia de tiempos verbales y formato de listas.
  - Unificación de manuscrito completo en `manuscript_final.md`.

### Fase 7: Diseño de Portada y Assets Gráficos
- **Rol asignado**: `@designer` / `@product`
- **Acciones**:
  - Cálculo de dimensiones del lomo según número final de páginas y tipo de papel (blanco/crema).
  - Generación de concepto de portada (front cover, spine, back cover) y generación de imagen / prompt.

### Fase 8: Maquetación y Formato KDP
- **Rol asignado**: `@devops` / `@formatter`
- **Acciones**:
  - Compilación mediante herramientas de maquetación (Pandoc, Typst, HTML/CSS print) a PDF (para libro impreso) y EPUB (para Kindle).
  - Verificación de sangrías, márgenes de encuadernación y paginación.

### Fase 9: Kit de Publicación KDP
- **Rol asignado**: `@product`
- **Acciones**:
  - Redacción de descripción de Amazon en HTML permitido (`<b>`, `<i>`, `<ul>`, `<li>`, `<h3>`).
  - Preparación de ficha técnica completa de publicación.
- **Entregable**: `kdp_launch_kit.md`.

### Fase 10: Promoción y Reseñas
- **Rol asignado**: `@product` / `@marketing`
- **Acciones**:
  - Estrategia de lanzamiento KDP Select (Free Promo / Countdown Deal).
  - Definición de secuencias de email o copys para redes sociales.

---

## Estructura Estándar de Archivos por Libro

Cuando se inicie un libro dentro de `bookIA`, la estructura de carpetas en `books/<niche>/<slug_libro>/` será:

```
books/<niche>/<slug_libro>/
├── 01_research/
│   ├── niche_analysis.md
│   └── keywords.md
├── 02_outline/
│   └── outline.md
├── 03_draft/
│   ├── ch01.md
│   ├── ch02.md
│   └── ...
├── 04_manuscript/
│   └── manuscript_complete.md
├── 05_kdp_assets/
│   ├── kdp_metadata.md
│   ├── cover_prompt.md
│   ├── interior_print.pdf
│   └── interior_ebook.epub
```
