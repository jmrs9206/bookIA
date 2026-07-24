# GUÍA DE PUBLICACIÓN PASO A PASO EN AMAZON KDP

Esta guía contiene las instrucciones exactas para subir y publicar con éxito los libros de la colección **Las Aventuras de Nico y Luna** utilizando el paquete consolidado en `kdp_package`.

---

## 🛠️ PASO 1: REGISTRO Y CONFIGURACIÓN FISCAL

1. **Crear tu Cuenta**: Ve a [Amazon KDP](https://kdp.amazon.com) e inicia sesión con tu cuenta de Amazon existente o crea una nueva.
2. **Configurar tu Cuenta**: Haz clic en **"Mi cuenta"** en la parte superior derecha y rellena la información obligatoria:
   - **Información del autor/editor**: Nombre completo, dirección y teléfono.
   - **Datos Bancarios**: Añade tu cuenta bancaria (IBAN de España) para recibir el pago de regalías mensualmente.
   - **Información Fiscal (Entrevista Fiscal)**: Indica que eres residente en **España** y proporciona tu **NIF/NIE**. Rellena el formulario fiscal W-8BEN integrado en la web para evitar que EE. UU. te aplique retenciones fiscales (gracias al tratado de doble imposición).

---

## 📂 PASO 2: ORGANIZACIÓN DE ARCHIVOS PARA SUBIDA

En tu directorio local `kdp_package/`, cada libro está organizado en carpetas que contienen:
* 📄 **`interior_sangria.pdf`**: El archivo del interior del libro físico.
* 🎨 **`portada_tapa_blanda.pdf`**: La cubierta extendida que incluye la contraportada, el lomo y la portada frontal.
* 📱 **`ebook_kindle.epub`**: El manuscrito digital fluido para la versión Kindle.
* 📝 **`kdp_metadata.md`**: Un archivo de ayuda con el título, subtítulo, 7 palabras clave de búsqueda backend y la descripción en formato HTML comercial listo para copiar y pegar.

---

## 🚀 PASO 3: PUBLICAR EL LIBRO EN TAPA BLANDA (FÍSICO)

En la pestaña **"Estantería"** de KDP, haz clic en **"+ Crear"** y elige **"Crear libro de tapa blanda"**. Completa las siguientes tres secciones:

### A. Detalles del Libro (Metadatos)
1. **Idioma**: Selecciona *Español*.
2. **Título**: Escribe el título exacto de la portada (ej: `Las Aventuras de Nico y Luna: El Bosque Mágico`).
3. **Subtítulo**: Copia el subtítulo del archivo de ayuda (ej: *Libro de cuento ilustrado para colorear con actividades para niños de 4 a 8 años...*).
4. **Autor**: Escribe como autor principal a: `Julio Martín Rodríguez Sánchez`.
5. **Descripción**: Copia la descripción con formato HTML del archivo de metadatos y pégala en la caja de texto. Amazon interpretará las negritas y las viñetas automáticamente.
6. **Palabras clave**: Introduce las 7 palabras clave optimizadas en las 7 cajas de texto traseras.
7. **Categorías**: Elige categorías infantiles que describan actividades y pasatiempos infantiles.

### B. Contenido del Libro
1. **ISBN**: Selecciona **"Asignar un ISBN gratuito de KDP"**.
2. **Opciones de impresión**:
   - **Tipo de tinta y papel**: *Interior con color estándar y papel blanco*.
   - **Tamaño de impresión**: **8.5 x 11 pulgadas** (21.59 x 27.94 cm).
   - **Ajustes de sangría**: **Con sangría (PDF obligatorio)**.
   - **Acabado de portada**: Elige *Brillo* o *Mate* (el brillo es el más recomendado para niños).
3. **Subir Manuscrito**: Sube `interior_sangria.pdf`.
4. **Subir Portada**: Elige *"Subir una portada que ya tiene (solo PDF)"* y sube `portada_tapa_blanda.pdf`.
5. **Declaración de IA**: En el apartado de contenido de Inteligencia Artificial, declara que has utilizado herramientas de IA para las *imágenes/ilustraciones* del interior y portada de forma honesta.
6. **Previsualizador**: Abre el previsualizador y comprueba que todo esté dentro de los márgenes de seguridad. Si todo se ve correcto, haz clic en **"Aprobar"**.

### C. Derechos y Precios
1. **Territorios**: Selecciona *Todos los territorios*.
2. **Tienda principal**: Elige `Amazon.es`.
3. **Fijar Precio**: Introduce un precio recomendado (por ejemplo, entre **8,99 € y 12,99 €**). Amazon calculará el costo de impresión y te mostrará el beneficio neto de tu regalía del **60%** por cada venta.
4. **Publicar**: Haz clic en **"Publicar tu libro de tapa blanda"**.

---

## 📱 PASO 4: PUBLICAR LA VERSIÓN KINDLE (EBOOK)

Una vez completado el paso anterior, KDP te ofrecerá la opción de enlazar la versión Kindle:
1. El sistema importará todos los detalles (título, autor y descripción).
2. En la sección de Contenido, sube `ebook_kindle.epub` como manuscrito.
3. Sube la ilustración de portada frontal del libro como imagen de portada del eBook.
4. En la sección de precios, elige el plan de regalías del **70%** y establece un precio (por ejemplo, entre **2,99 € y 4,99 €**).
5. Haz clic en **"Publicar tu eBook Kindle"**.
