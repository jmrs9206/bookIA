#!/usr/bin/env python3
import os
import sys
import re
import subprocess

# Configuración de estilos CSS para Weasyprint (Libro Físico KDP 8.5" x 11")
CSS_TEMPLATE = """@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Nunito:wght@400;700&display=swap');

@page {
    size: 8.5in 11in;
    margin: 0.8in;
    @bottom-center {
        content: counter(page);
        font-family: 'Fredoka', sans-serif;
        font-size: 11pt;
        color: #555555;
    }
}

@page :first {
    @bottom-center {
        content: none;
    }
}

@page :nth(2) {
    @bottom-center {
        content: none;
    }
}

body {
    font-family: 'Nunito', sans-serif;
    font-size: 14pt;
    line-height: 1.5;
    color: #111111;
    margin: 0;
    padding: 0;
}

.page-break {
    page-break-after: always;
    box-sizing: border-box;
    position: relative;
    height: 9.2in; /* Altura útil ajustada */
    overflow: hidden;
}

/* Portada Interior */
.portada-interior {
    text-align: center;
    padding-top: 1in;
}

.portada-interior h1 {
    font-family: 'Fredoka', sans-serif;
    font-size: 32pt;
    margin-bottom: 10pt;
    text-transform: uppercase;
    color: #222222;
    line-height: 1.2;
}

.portada-interior h2 {
    font-family: 'Fredoka', sans-serif;
    font-size: 22pt;
    font-weight: normal;
    color: #555555;
    margin-bottom: 1.5in;
}

.portada-interior .meta {
    font-size: 12pt;
    color: #666666;
    line-height: 1.8;
}

/* Derechos de Autor */
.derechos {
    font-size: 10pt;
    color: #444444;
    padding-top: 0.5in;
    line-height: 1.5;
}

.derechos h3, .derechos p {
    margin-bottom: 15px;
}

/* Portadilla de Capítulo Artística */
.portada-capitulo {
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 9.2in;
    width: 100%;
    position: relative;
    page-break-after: always;
    box-sizing: border-box;
}

.portada-capitulo-overlay {
    position: absolute;
    bottom: 1.0in;
    left: 5%;
    right: 5%;
    background-color: rgba(255, 255, 255, 0.85); /* Fondo semitransparente suave */
    padding: 15pt 25pt;
    border-radius: 8px;
    text-align: center;
    border: 3px solid #222222;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}

.portada-capitulo-overlay h1 {
    font-family: 'Fredoka', sans-serif;
    font-size: 22pt;
    color: #111111;
    margin: 0;
    text-transform: uppercase;
    line-height: 1.3;
}

/* Página de Lectura Estándar */
.lectura-container {
    padding: 0.2in 0;
}

.page-title {
    font-family: 'Fredoka', sans-serif;
    font-size: 16pt;
    color: #333333;
    margin-bottom: 15pt;
    text-align: center;
    text-transform: uppercase;
    border-bottom: 2px dashed #cccccc;
    padding-bottom: 5px;
}

.lectura-texto {
    font-size: 14pt;
    margin-bottom: 15pt;
    text-align: justify;
    padding: 0 10px;
}

.lectura-texto p {
    margin: 0 0 10px 0;
}

.lectura-destacado {
    background-color: #f9f9f9;
    border-left: 5px solid #222222;
    padding: 10pt;
    margin: 10pt 0;
    font-size: 15pt;
    font-style: italic;
    font-weight: bold;
    border-radius: 4px;
}

/* Páginas de Ilustraciones y Actividades */
.image-container {
    text-align: center;
    margin-top: 10px;
}

.image-container img {
    display: block;
    margin: 0 auto;
    max-width: 90%;
    max-height: 5.2in; /* Altura contenida para que quepa con texto */
    object-fit: contain;
    border: 2px solid #000000;
    border-radius: 8px;
    padding: 5px;
    background-color: #ffffff;
}

.image-caption {
    margin-top: 5pt;
    font-family: 'Fredoka', sans-serif;
    font-size: 11pt;
    color: #555555;
}

/* Páginas de Actividades */
.actividad-texto {
    font-size: 13pt;
    margin-bottom: 15px;
}

.actividad-lista {
    padding-left: 20px;
    margin: 10px 0;
}

.actividad-lista li {
    margin-bottom: 8px;
    font-size: 13pt;
}

/* Ajustes especiales para que las imágenes tengan prioridad de página */
.page-image-only {
    padding: 0;
}

.page-image-only .image-container {
    margin-top: 0.5in;
}

.page-image-only img {
    max-height: 7.5in; /* Más grandes si no hay texto */
}

h1, h2, h3 {
    font-family: 'Fredoka', sans-serif;
    text-align: center;
    color: #222222;
    margin-top: 10px;
    margin-bottom: 10px;
}
h1 { font-size: 24pt; }
h2 { font-size: 18pt; }
h3 { font-size: 14pt; }
"""

def parse_markdown_to_html(md_content, base_dir):
    # Separar el documento por páginas
    pages = re.split(r'##\s+\[PÁGINA\s+(\d+):\s*(.*?)\]', md_content)
    
    html_out = []
    html_out.append("<!DOCTYPE html><html><head><meta charset='utf-8'>")
    html_out.append(f"<style>{CSS_TEMPLATE}</style>")
    html_out.append("</head><body>")
    
    # Procesar pares de (número_pagina, título_pagina, contenido_pagina)
    idx = 1
    while idx < len(pages):
        page_num = pages[idx].strip()
        page_title = pages[idx+1].strip()
        page_content = pages[idx+2].strip()
        idx += 3
        
        # Limpiar delimitadores horizontales del markdown
        page_content = re.sub(r'^---\s*$', '', page_content, flags=re.MULTILINE)
        
        # Clase CSS de la página
        page_class = "page-break"
        
        # Analizar tipo de página y formatear
        if "PORTADA INTERIOR" in page_title:
            title_match = re.search(r'^#\s+(.*?)$', page_content, re.MULTILINE)
            subtitle_match = re.search(r'^##\s+(.*?)$', page_content, re.MULTILINE)
            
            title = title_match.group(1) if title_match else "Las Aventuras de Nico y Luna"
            subtitle = subtitle_match.group(1) if subtitle_match else ""
            
            # Limpiar contenido extra para metadatos
            meta_content = page_content
            if title_match: meta_content = meta_content.replace(title_match.group(0), "")
            if subtitle_match: meta_content = meta_content.replace(subtitle_match.group(0), "")
            meta_content = meta_content.replace("#", "")
            # Reemplazar ** text ** por negrita
            meta_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', meta_content)
            meta_content = meta_content.replace("\n", "<br>")
            
            html_out.append(f"""
            <div class="{page_class} portada-interior">
                <h1>{title}</h1>
                <h2>{subtitle}</h2>
                <div class="meta">{meta_content}</div>
            </div>
            """)
            
        elif "DERECHOS" in page_title or "AUTOR" in page_title:
            formatted_content = page_content
            formatted_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', formatted_content)
            formatted_content = formatted_content.replace("\n\n", "</p><p>").replace("\n", "<br>")
            html_out.append(f"""
            <div class="{page_class} derechos">
                <div class="page-title">{page_title}</div>
                <p>{formatted_content}</p>
            </div>
            """)
            
        elif "PORTADILLA CAPÍTULO" in page_title or "PORTADILLA DE CAPÍTULO" in page_title:
            # Buscar si contiene una imagen de fondo
            img_match = re.search(r'!\[(.*?)\]\((.*?)\)', page_content)
            img_path = ""
            resolved_img_path = ""
            if img_match:
                img_path = img_match.group(2)
                # Resolver la ruta de la imagen
                resolved_img_path = os.path.normpath(os.path.join(base_dir, "final", img_path))
                if not os.path.exists(resolved_img_path):
                    resolved_img_path = os.path.normpath(os.path.join(base_dir, img_path.replace("../", "")))
            
            # Limpiar el título quitando las marcas
            clean_title = page_title.replace("PORTADILLA CAPÍTULO - ", "").replace("PORTADILLA DE CAPÍTULO - ", "").replace("PORTADILLA CAPÍTULO:", "").replace("PORTADILLA DE CAPÍTULO:", "").strip()
            
            # Generar el HTML de la portadilla de capítulo con imagen de fondo
            if img_path:
                html_out.append(f"""
                <div class="{page_class} portada-capitulo" style="background-image: url('{resolved_img_path}');">
                    <div class="portada-capitulo-overlay">
                        <h1>{clean_title}</h1>
                    </div>
                </div>
                """)
            else:
                html_out.append(f"""
                <div class="{page_class} portada-capitulo">
                    <div class="portada-capitulo-overlay">
                        <h1>{clean_title}</h1>
                    </div>
                </div>
                """)
            
        else:
            # Páginas normales
            # Verificar si contiene una imagen
            img_match = re.search(r'!\[(.*?)\]\((.*?)\)', page_content)
            
            if img_match:
                img_caption = img_match.group(1)
                img_path = img_match.group(2)
                
                # Intentar resolver la ruta absoluta de la imagen para Weasyprint
                resolved_img_path = os.path.normpath(os.path.join(base_dir, "final", img_path))
                if not os.path.exists(resolved_img_path):
                    resolved_img_path = os.path.normpath(os.path.join(base_dir, img_path.replace("../", "")))
                
                # Quitar la imagen del texto de lectura para maquetarla de forma especial
                clean_content = page_content.replace(img_match.group(0), "")
                
                # Formatear el texto de lectura
                clean_content = format_body_text(clean_content)
                
                # Si tiene poco texto y una imagen grande, le damos la clase para imagen
                if len(clean_content.strip()) < 100:
                    html_out.append(f"""
                    <div class="{page_class} page-image-only">
                        <div class="image-container">
                            <img src="{resolved_img_path}" alt="{img_caption}">
                            <div class="image-caption">{img_caption}</div>
                        </div>
                    </div>
                    """)
                else:
                    html_out.append(f"""
                    <div class="{page_class}">
                        <div class="page-title">{page_title}</div>
                        <div class="lectura-texto">{clean_content}</div>
                        <div class="image-container">
                            <img src="{resolved_img_path}" alt="{img_caption}">
                            <div class="image-caption">{img_caption}</div>
                        </div>
                    </div>
                    """)
            else:
                # Página sin imagen (solo texto o juegos)
                clean_content = format_body_text(page_content)
                
                html_out.append(f"""
                <div class="{page_class}">
                    <div class="page-title">{page_title}</div>
                    <div class="lectura-container">
                        <div class="lectura-texto">{clean_content}</div>
                    </div>
                </div>
                """)
                
    html_out.append("</body></html>")
    return "\n".join(html_out)

def format_body_text(text):
    # Normalizar retornos de carro
    text = text.replace('\r\n', '\n')
    
    # Formatear encabezados markdown antes de separar líneas
    text = re.sub(r'^#\s+(.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^##\s+(.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^###\s+(.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    lines = text.split('\n')
    new_lines = []
    in_blockquote = False
    bq_content = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('>'):
            in_blockquote = True
            # Extraer contenido de la cita
            clean_line = stripped[1:].strip()
            # Omitir etiquetas descriptivas redundantes
            clean_line_no_md = re.sub(r'\*+', '', clean_line).strip()
            if re.search(r'^(Texto de Lectura:|Instrucción de Coloreado:)$', clean_line_no_md, re.IGNORECASE):
                continue
            if clean_line:
                bq_content.append(clean_line)
        else:
            if in_blockquote:
                # Cerrar blockquote actual y añadirlo
                if bq_content:
                    content_str = " ".join(bq_content)
                    content_str = content_str.replace('—', '&mdash;')
                    content_str = re.sub(r'\*\*(.*?)\*\*', r'\1', content_str)
                    new_lines.append(f'<div class="lectura-destacado">{content_str}</div>')
                bq_content = []
                in_blockquote = False
            new_lines.append(line)
            
    # Si queda un blockquote abierto al final
    if in_blockquote and bq_content:
        content_str = " ".join(bq_content)
        content_str = content_str.replace('—', '&mdash;')
        content_str = re.sub(r'\*\*(.*?)\*\*', r'\1', content_str)
        new_lines.append(f'<div class="lectura-destacado">{content_str}</div>')
        
    text = "\n".join(new_lines)
    
    # Formatear caracteres especiales y markdown básico
    text = text.replace('—', '&mdash;')
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Formatear listas de juegos
    text = re.sub(r'-\s+\[\s*\]\s+(.*?)$', r'<li><input type="checkbox"> \1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'-\s+([^\n]+)', r'<li>\1</li>', text, flags=re.MULTILINE)
    
    # Agrupar las listas
    if '<li>' in text:
        text = re.sub(r'(<li>.*?</li>)+', r'<ul class="actividad-lista">\g<0></ul>', text, flags=re.DOTALL)
    
    # Formatear párrafos
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    formatted_paragraphs = []
    for p in paragraphs:
        if p.startswith('<div') or p.startswith('<ul') or p.startswith('<li>') or p.startswith('##') or p.startswith('<p>'):
            formatted_paragraphs.append(p)
        else:
            formatted_paragraphs.append(f"<p>{p}</p>")
            
    return "\n".join(formatted_paragraphs)

def main():
    if len(sys.argv) < 2:
        print("Uso: compile_book.py <book_directory_path>")
        sys.exit(1)
        
    book_dir = os.path.abspath(sys.argv[1])
    if not os.path.isdir(book_dir):
        print(f"Error: {book_dir} no es un directorio válido.")
        sys.exit(1)
        
    print(f"Compilando libro en: {book_dir}")
    
    # Buscar el manuscrito en la carpeta final
    final_dir = os.path.join(book_dir, "final")
    if not os.path.exists(final_dir):
        print(f"Error: No se encuentra la carpeta final en {book_dir}")
        sys.exit(1)
        
    md_files = [f for f in os.listdir(final_dir) if f.endswith(".md") and f != "informe_publicacion_kdp.md" and f != "qa_audit_report.md" and f != "revision_coherencia.md"]
    if not md_files:
        print(f"Error: No se encontró el manuscrito Markdown en {final_dir}")
        sys.exit(1)
        
    md_file_path = os.path.join(final_dir, md_files[0])
    print(f"Manuscrito encontrado: {md_file_path}")
    
    with open(md_file_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    # 1. COMPILAR PDF CON WEASYPRINT
    html_content = parse_markdown_to_html(md_content, book_dir)
    temp_html_path = os.path.join(final_dir, "temp_compile.html")
    
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    pdf_out_name = os.path.basename(md_file_path).replace(".md", ".pdf")
    pdf_out_path = os.path.join(final_dir, pdf_out_name)
    
    print("Ejecutando Weasyprint para compilar PDF...")
    try:
        subprocess.run(["weasyprint", temp_html_path, pdf_out_path], check=True)
        print(f"¡PDF Generado Exitosamente!: {pdf_out_path}")
    except Exception as e:
        print(f"Error al ejecutar Weasyprint: {e}")
        
    # Limpiar archivo temporal HTML
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
        
    # 2. COMPILAR EPUB CON PANDOC
    epub_out_name = os.path.basename(md_file_path).replace(".md", ".epub")
    epub_out_path = os.path.join(final_dir, epub_out_name)
    
    print("Ejecutando Pandoc para compilar EPUB...")
    try:
        subprocess.run([
            "pandoc", 
            os.path.basename(md_file_path), 
            "-o", os.path.basename(epub_out_path), 
            "--metadata", f"title={os.path.basename(book_dir).replace('_', ' ').title()}",
            "--toc"
        ], cwd=final_dir, check=True)
        print(f"¡EPUB Generado Exitosamente!: {epub_out_path}")
    except Exception as e:
        print(f"Error al ejecutar Pandoc: {e}")

if __name__ == "__main__":
    main()
