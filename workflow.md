# Flujo de Trabajo (Workflow) para Creación de Libros KDP con IA

> **Marco de Orquestación `bookIA`**  
> Basado en las políticas y arquitectura de orquestación de agentes IA.  
> Documento detallado de especificación: [.ai/WORKFLOW_SPEC.md](file:///home/jmrs/Documentos/PROYECTOS/JMRS/bookIA/.ai/WORKFLOW_SPEC.md)

---

## 🎯 Objetivo

Establecer un sistema estructurado, repetible y asistido por IA para investigar, escribir, maquetar y publicar libros de alto valor en Amazon KDP, cumpliendo al 100% las directrices editoriales y de contenido de Amazon.

---

## 📚 Categorías y Nichos del Catálogo

| Categoría | Nichos Principales | Enfoque de Contenido |
|---|---|---|
| **1. Prácticos / No Ficción** | IA para principiantes, ChatGPT profesional, Finanzas personales, Productividad | Guías paso a paso, tablas, ejemplos aplicados y resúmenes ejecutivos |
| **2. Actividades / Low Content** | Sopas de letras, Sudoku, Ejercicios de caligrafía, Colorear | Generación asistida por scripts/herramientas vectoriales |
| **3. Ficción** | Thriller, Romance, Fantasía, Ciencia Ficción | Arcos narrativos completos, desarrollo de personajes y diálogos naturales |

---

## 🔄 El Workflow en 10 Pasos

1. **Investigación de Nicho**: Validación de demanda y viabilidad en Amazon KDP.
2. **Palabras Clave & Categorías**: Definición de las 7 palabras clave de backend y 2 categorías BISAC.
3. **Índice y Estructura**: Creación de la tabla de contenidos por capítulos y subsecciones.
4. **Redacción por Capítulos**: Generación asistida con prompts estructurados.
5. **Revisión y Enriquecimiento**: Eliminación de muletillas de IA y adición de casos/ejercicios.
6. **Corrección Ortotipográfica**: Unificación de estilo y ortografía.
7. **Diseño de Portada**: Definición del concepto visual y plantilla para lomo/cubierta KDP.
8. **Maquetación Impresa y Digital**: Compilación en PDF (paperback) y EPUB (Kindle).
9. **Ficha y Metadatos KDP**: Título, subtítulo y descripción enriquecida con HTML.
10. **Lanzamiento y Reseñas**: Estrategia promocional KDP Select y captura de valor.

---

## 📂 Estructura del Repositorio de Libros

Los nuevos libros se alojarán bajo la ruta estandarizada:

```
books/
└── <nicho>/
    └── <slug_del_libro>/
        ├── 01_research/      # Investigaciones y palabras clave
        ├── 02_outline/       # Tabla de contenidos
        ├── 03_draft/         # Borradores por capítulos
        ├── 04_manuscript/    # Manuscrito final unificado
        └── 05_kdp_assets/    # Metadatos HTML, PDF impreso, EPUB y Portada
```

---

## 🛠️ Prompts Base

### Prompt para Estructurar Índice (Fase 3)
```text
Actúa como un arquitecto de libros profesional especializado en [Nicho/Tema]. 
Crea un índice exhaustivo de [Nº] capítulos para un libro titulado "[Título]".
Para cada capítulo, incluye de 3 a 5 subsecciones detalladas, los objetivos de aprendizaje y los ejercicios o tablas prácticas que incluirá.
```

### Prompt para Redacción de Capítulo (Fase 4)
```text
Actúa como un autor experto en [Tema]. Escribe el Capítulo [Nº]: "[Título Capítulo]".
Sigue exactamente la siguiente estructura: [Subsecciones].
Estilo: Claro, profesional, directo y sin clichés ni muletillas típicas de IA.
Incluye al menos un ejemplo práctico, una tabla comparativa si procede y 3 ejercicios clave al final.
```

---

## 📋 Lista de Control de Calidad (Definition of Done)

- [ ] Índice validado y sin vacíos temáticos.
- [ ] Borrador completo revisado sin errores ortotipo.
- [ ] PDF maquetado con márgenes KDP de acuerdo al número de páginas.
- [ ] Archivo EPUB validado sin errores de etiquetas.
- [ ] Kit de metadatos (7 Keywords + Descripción HTML) listo para copiar/pegar en KDP.
