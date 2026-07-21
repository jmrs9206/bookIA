# Project Constitution - bookIA

## Metadata

- Project ID: `bookIA`
- Status: `APPROVED`
- Version: `1.0`
- Approved by: `jmrs9206`
- Effective from: `2026-07-21`

## Purpose of this constitution

Definir reglas, rutas permitidas y restricciones específicas para la creación de libros y herramientas en el proyecto `bookIA`.

## Allowed repositories and roots

| Root | Purpose | Read | Write | Notes |
|---|---|---:|---:|---|
| `/home/jmrs/Documentos/PROYECTOS/JMRS/bookIA` | Repositorio principal del proyecto | yes | yes | Workspace único autorizado |

## Prohibited paths

- Cualquier ruta fuera del directorio `/home/jmrs/Documentos/PROYECTOS/JMRS/bookIA`.
- Repositorios o proyectos ajenos salvo en modo lectura de referencia.

## Allowed roles

- `@director`
- `@product`
- `@context`
- `@architect`
- `@planner`
- `@editor` (Rol especializado en edición y calidad de texto)
- `@qa`
- `@reviewer`

## Actions requiring human approval

- Publicación/Subida final de libros a Amazon KDP.
- Modificación de políticas globales en `.agents/policies`.
- Eliminación destructiva de contenido de libros ya finalizados.

## Testing & Quality Requirements

- Todo libro producido debe contar con:
  1. Tabla de contenidos (Índice) validada.
  2. Revisión de estilo y ortotipográfica.
  3. Comprobación de formateo KDP (márgenes, sangrías, fuentes).
  4. Ficha de metadatos completa (Título, Subtítulo, 7 Keywords KDP, Categorías, Descripción HTML).

## Git policy

- Branch por defecto: `main`
- Commits descriptivos asociados al progreso del workflow o desarrollo de código.
