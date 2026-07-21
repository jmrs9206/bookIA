# Project Charter - bookIA

## Metadata

- Project ID: `bookIA`
- Project name: `bookIA - Generación y Publicación de Libros con IA para Amazon KDP`
- Owner: `jmrs9206`
- Repository: `https://github.com/jmrs9206/bookIA.git`
- Status: `APPROVED`
- Version: `1.0`
- Last verified: `2026-07-21`
- Approved by: `jmrs9206`

## Problem

El proceso manual de creación, maquetación y publicación de libros en Amazon KDP es lento y complejo. Se requiere una metodología y flujo estructurado asistido por IA para investigar nichos, estructurar contenidos de alto valor, redactar, maquetar y preparar assets listos para publicación cumpliendo rigurosamente con las políticas de Amazon KDP.

## Intended users

| User/persona | Need | Source | Status |
|---|---|---|---|
| Autor / Publisher | Automatizar y estructurar la producción de libros KDP de alta calidad | USER | CONFIRMED |
| Lector de Amazon KDP | Recibir contenido bien maquetado, útil y profesional sin patrones de relleno | DOCUMENT | CONFIRMED |

## Desired outcome

Un marco de trabajo y orquestación de IA capaz de guiar e implementar la creación completa de libros en diversos nichos (Libros Prácticos, Actividades, Ficción), produciendo borradores revisados, archivos maquetados (PDF/EPUB) y metadatos optimizados para KDP.

## In scope

- Investigación de nichos y palabras clave KDP.
- Generación de índices y estructuras detalladas por libro.
- Redacción asistida de capítulos con prompts optimizados y control de calidad.
- Edición, corrección ortotipográfica y adaptaciones estilísticas.
- Generación de metadatos (título, subtítulo, 7 palabras clave, categorías, descripción HTML).
- Creación y especificación del flujo de maquetación interior y portadas.

## Out of scope / non-goals

- Publicación directa mediante APIs no oficiales de Amazon (el subido final a KDP se realiza manualmente por el usuario).
- Generación masiva de contenido de baja calidad o spam.

## Success criteria

| ID | Criterion | Measurement | Target | Evidence owner |
|---|---|---|---|---|
| SC-001 | Cumplimiento KDP | Cero rechazos de formato o contenido por parte de Amazon KDP | 100% | @qa |
| SC-002 | Estructura completa | Workflow documentado y reproducible paso a paso | 100% | @product |
| SC-003 | Calidad editorial | Libro con índice completo, capítulos estructurados, ejercicios/ejemplos | 100% | @reviewer |

## Constraints

- Technology: Markdown, Pandoc/LaTeX (para maquetación PDF), Python/JavaScript scripts para herramientas auxiliares.
- Guidelines: Cumplimiento estricto con las directrices de contenido e IA de Amazon KDP.
- Storage: Repositorio local y Git remoto en `https://github.com/jmrs9206/bookIA.git`.

## Assumptions

| ID | Assumption | Impact if false | Verification plan | Status |
|---|---|---|---|---|
| AS-001 | Amazon KDP permite contenido generado por IA siempre que se declare y sea de alta calidad | Rechazo de cuenta KDP | Revisión continua de términos KDP | VERIFIED |
| AS-002 | El formato Markdown con Pandoc o herramientas similares permite maquetar en PDF/EPUB para KDP | Dificultad en maquetación | Pruebas de renderizado de muestra | VERIFIED |

## Risks

- Cambio en las políticas de Amazon KDP respecto a IA.
- Saturación de mercado en nichos no investigados.

## Approval gate

- [x] Problem approved
- [x] Scope approved
- [x] Non-goals approved
- [x] Success criteria approved
- [x] Constraints reviewed

Approval statement: `Aprobado por jmrs9206`
