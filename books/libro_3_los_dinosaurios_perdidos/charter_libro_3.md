# Project Charter - Libro 3: Los Dinosaurios Perdidos

## Metadata
- **Project ID**: `libro_3_los_dinosaurios_perdidos`
- **Colección**: Las Aventuras de Nico y Luna — Libro 3
- **Autor**: Julio Martín Rodríguez Sánchez
- **Copyright**: © 2026 Julio Martín Rodríguez Sánchez
- **Status**: `NEEDS_APPROVAL`
- **Fecha**: 2026-07-22

---

## 1. Propósito y Sinopsis
**Propósito**: Crear el tercer volumen de la colección infantil ilustrada de aventuras y actividades de Nico y Luna, enfocado en el nicho de dinosaurios y prehistoria para niños de 4 a 8 años en Amazon KDP.

**Sinopsis**: Nico, Luna y Copito viajan en el tiempo a través de un portal mágico en el jardín y aparecen en un valle prehistórico lleno de helechos gigantes, volcanes que echan burbujas de vapor y dinosaurios amigables como el pequeño T-Rex "Dino" y un enorme Brontosaurio. Juntos deben ayudar a Dino a encontrar sus juguetes perdidos antes de regresar al presente.

---

## 2. Alcance (In Scope)
- **Estructura Física**: Libro impreso premium de exactamente **60 páginas físicas**.
- **Maquetación KDP**: PDF en tamaño físico de sangría de **8.625 x 11.25 pulgadas** con márgenes asimétricos KDP.
- **Narrativa**: 7 Capítulos (incluyendo Portadilla de Pertenencia, Portada Interior, Derechos y Nota Editorial, 4 capítulos de historia y 1 capítulo final de actividades).
- **Assets Gráficos**:
  - 1 Cubierta extendida KDP (Contraportada + Lomo + Portada, tamaño 17.385" x 11.25", temática selva jurásica).
  - 6 Portadillas artísticas de capítulo a color (sangre completa).
  - 5 Ilustraciones de historia a color (sangre completa).
  - 5 Láminas de colorear en blanco y negro (centradas limpiamente).
- **Actividades en SVG**:
  - Laberinto del Volcán (ayudar a Dino a llegar al nido).
  - 5 Diferencias en el nido de Triceratops.
  - Conecta los Puntos de un dinosaurio del 1 al 20.
  - Marco de dibujo libre para diseñar tu propio dinosaurio.
  - Probador de lápices y rotuladores y solucionario al final.

---

## 3. Fuera de Alcance (Out of Scope)
- Generación de audio-libros o adaptaciones digitales Kindle reflowable no maquetadas.
- Distribución o subida directa automática a Amazon KDP (la subida la realiza el usuario de manera manual).

---

## 4. Restricciones
- El manuscrito debe utilizar el mismo script de compilación [compile_book.py](file:///../../scripts/compile_book.py) para asegurar la consistencia y la entrega del PDF en formato de sangría KDP exacto.
- Licencias y atribución exclusivas a `Julio Martín Rodríguez Sánchez`.

---

## 5. Desconocidos / Bloqueos
- **Cuota de la API de Imágenes**: La API `gemini-3.1-flash-image` estará en reset a las 17:33:58. Actualmente son las 17:08 (faltan 25 minutos). Por tanto, la generación de las ilustraciones definitivas se encuentra en pausa temporal hasta el restablecimiento.

---

## 6. Criterios de Éxito
- Paginación física final de exactamente **60 páginas**.
- Cero advertencias de Weasyprint de calc() o desbordamientos.
- Aprobación visual 100% de la cubierta y del manuscrito interior sin marcos ni bordes blancos.

---

## 7. Plan de Acción Inicial
1. **Fase 1**: Aprobación del presente Charter por el usuario.
2. **Fase 2**: Investigación de palabras clave y estructuración del índice (outline) en `books/libro_3_los_dinosaurios_perdidos/outline/book_outline.md`.
3. **Fase 3**: Redacción del borrador en Markdown por capítulos.
4. **Fase 4**: Generación de las ilustraciones de relleno (placeholders) para compilar y validar la maquetación.
5. **Fase 5**: Reemplazo de ilustraciones definitivas al restablecerse la cuota de la API de imágenes.
6. **Fase 6**: Compilación final y reporte de Q&A.
