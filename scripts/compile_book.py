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

/* Página especial para portadillas artísticas de capítulo a sangre completa (full bleed) */
@page page_portada_capitulo {
    size: 8.5in 11in;
    margin: 0;
    @bottom-center {
        content: none;
    }
}

body {
    font-family: 'Nunito', sans-serif;
    font-size: 14pt;
    line-height: 1.6;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
}

.page-break {
    page-break-after: always;
    box-sizing: border-box;
    position: relative;
    height: 9.4in; /* Altura útil con márgenes */
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

/* Portada Interior */
.portada-interior {
    text-align: center;
    padding-top: 1.2in;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 9.4in;
    box-sizing: border-box;
}

.portada-interior-title-area {
    margin-top: 0.5in;
}

.portada-interior h1 {
    font-family: 'Fredoka', sans-serif;
    font-size: 34pt;
    font-weight: 600;
    margin-bottom: 12pt;
    text-transform: uppercase;
    color: #111111;
    line-height: 1.2;
}

.portada-interior h2 {
    font-family: 'Fredoka', sans-serif;
    font-size: 22pt;
    font-weight: normal;
    color: #4a4a4a;
    margin-bottom: 0.8in;
}

.portada-interior .meta {
    font-size: 13pt;
    color: #555555;
    line-height: 1.8;
    margin-bottom: 1.5in;
}

/* Derechos de Autor */
.derechos {
    font-size: 11pt;
    color: #333333;
    padding-top: 0.4in;
    line-height: 1.6;
}

.derechos h3, .derechos p {
    margin-bottom: 15px;
}

/* Portadilla de Capítulo Artística (A sangre completa) */
.portada-capitulo {
    page: page_portada_capitulo;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 11.0in; /* Ocupa todo el papel físico */
    width: 8.5in;
    position: relative;
    page-break-after: always;
    box-sizing: border-box;
}

.portada-capitulo-overlay {
    position: absolute;
    bottom: 1.5in; /* Elevado para seguridad de corte */
    left: 1.0in;
    right: 1.0in;
    background-color: rgba(255, 255, 255, 0.92); /* Fondo semitransparente premium */
    padding: 24pt 32pt;
    border-radius: 16px;
    text-align: center;
    border: 2px solid #1a1a1a;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12); /* Sombra suave y profesional */
}

.portada-capitulo-overlay h1 {
    font-family: 'Fredoka', sans-serif;
    font-size: 24pt;
    font-weight: 600;
    color: #111111;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 1px;
    line-height: 1.3;
}

/* Página de Lectura Estándar */
.lectura-container {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-sizing: border-box;
    padding: 0.2in 0.4in;
}

.page-title {
    font-family: 'Fredoka', sans-serif;
    font-size: 16pt;
    font-weight: 600;
    color: #222222;
    margin-bottom: 15pt;
    text-align: center;
    text-transform: uppercase;
    border-bottom: 2px dashed #cccccc;
    padding-bottom: 8px;
    letter-spacing: 1px;
}

.lectura-texto {
    font-size: 15pt;
    line-height: 1.6;
    text-align: justify;
    color: #1a1a1a;
    width: 100%;
}

.lectura-texto p {
    margin: 0 0 14pt 0;
}

.lectura-texto p:last-child {
    margin-bottom: 0;
}

.lectura-destacado {
    background-color: #fcfcfc;
    border-left: 4px solid #1a1a1a;
    padding: 12pt 16pt;
    margin: 15pt 0;
    font-size: 14pt;
    font-style: italic;
    border-radius: 4px;
    line-height: 1.5;
    box-shadow: inset 2px 2px 5px rgba(0,0,0,0.02);
}

/* Páginas de Ilustraciones y Actividades */
.image-container {
    text-align: center;
    margin-top: 15px;
    width: 100%;
}

.image-container img {
    display: block;
    margin: 0 auto;
    max-width: 95%;
    max-height: 5.4in; /* Ajustado para dar espacio al título y pie */
    object-fit: contain;
    border: 2px solid #1a1a1a;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 6px 15px rgba(0,0,0,0.08);
}

.image-caption {
    margin-top: 8pt;
    font-family: 'Fredoka', sans-serif;
    font-size: 11pt;
    color: #555555;
    text-align: center;
}

/* Páginas de Actividades */
.actividad-texto {
    font-size: 13pt;
    margin-bottom: 15px;
    line-height: 1.5;
}

.actividad-lista {
    padding-left: 20px;
    margin: 12px 0;
}

.actividad-lista li {
    margin-bottom: 10px;
    font-size: 13pt;
    line-height: 1.4;
}

/* Ajustes especiales para que las imágenes tengan prioridad de página */
.page-image-only {
    padding: 0;
    justify-content: center;
}

.page-image-only .image-container {
    margin-top: 0;
}

.page-image-only img {
    max-height: 7.8in; /* Más grandes si no hay texto */
    max-width: 100%;
}

h1, h2, h3 {
    font-family: 'Fredoka', sans-serif;
    text-align: center;
    color: #111111;
    margin-top: 10px;
    margin-bottom: 10px;
}
h1 { font-size: 24pt; font-weight: 600; }
h2 { font-size: 18pt; font-weight: 600; }
h3 { font-size: 15pt; font-weight: 600; }

/* Estilos Premium de Actividades y Juegos */
.actividad-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: calc(100% - 40px);
    box-sizing: border-box;
    padding: 0.1in 0.2in;
    width: 100%;
}

.actividad-svg {
    display: block;
    margin: 10px auto;
    max-width: 100%;
    max-height: 4.8in;
    background-color: #ffffff;
    border-radius: 12px;
}

.actividad-instrucciones {
    font-size: 12.5pt;
    line-height: 1.5;
    color: #333333;
    text-align: center;
    margin-bottom: 12px;
    width: 100%;
}

.actividad-lista-diferencias {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    list-style: none;
    padding: 0;
    margin: 15px 0 0 0;
    width: 100%;
}

.actividad-lista-diferencias li {
    font-size: 10.5pt;
    background-color: #f7f7f7;
    border: 1px dashed #bbbbbb;
    border-radius: 20px;
    padding: 6px 14px;
    color: #333333;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Lienzo de dibujo libre */
.canvas-dibujo-decorativo {
    width: 100%;
    height: 4.2in;
    border: 3px double #333333;
    border-radius: 16px;
    background-color: #ffffff;
    margin: 10px 0;
    position: relative;
    box-sizing: border-box;
}

.canvas-decoracion-esquina {
    position: absolute;
    font-size: 20pt;
    color: #cccccc;
    user-select: none;
}

.canvas-decoracion-tl { top: 8px; left: 12px; }
.canvas-decoracion-tr { top: 8px; right: 12px; }
.canvas-decoracion-bl { bottom: 8px; left: 12px; }
.canvas-decoracion-br { bottom: 8px; right: 12px; }

.campos-dibujo-libre {
    width: 100%;
    margin-top: 15px;
}

.campo-escritura {
    font-size: 12pt;
    margin-bottom: 12px;
    color: #222222;
    text-align: left;
    display: flex;
    align-items: center;
}

.campo-escritura strong {
    margin-right: 10px;
    white-space: nowrap;
}

.campo-escritura span {
    border-bottom: 1.5px dashed #777777;
    flex-grow: 1;
    height: 20px;
    display: inline-block;
}

/* Probador de colores */
.probador-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    width: 100%;
    margin-top: 10px;
    gap: 15px;
    box-sizing: border-box;
}

.probador-caja {
    width: 47%;
    border: 2px dashed #999999;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    background-color: #fafafa;
    box-sizing: border-box;
}

.probador-caja h4 {
    margin: 0 0 5px 0;
    font-family: 'Fredoka', sans-serif;
    font-size: 12pt;
    color: #111111;
}

.probador-zonas {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 10px;
}

.probador-zona-color {
    width: 40px;
    height: 40px;
    border: 2px dashed #bbbbbb;
    border-radius: 50%;
    background-color: #ffffff;
}

.probador-zona-rectangular {
    width: 90%;
    height: 50px;
    border: 2px dashed #bbbbbb;
    border-radius: 8px;
    background-color: #ffffff;
    margin: 8px auto 0 auto;
}
"""

def parse_markdown_to_html(md_content, base_dir):
    # Separar el documento por páginas
    pages = re.split(r'##\s+\[PÁGINA\s+(\d+):\s*(.*?)\]', md_content)
    
    html_out = []
    html_out.append("<!DOCTYPE html><html><head><meta charset='utf-8'>")
    html_out.append(f"<style>{CSS_TEMPLATE}</style>")
    html_out.append("</head><body>")
    
    # Determinar si el libro es de temática espacial o de bosque
    es_espacio = "viaje_al_espacio" in base_dir.lower() or "espacio" in base_dir.lower()
    
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
                <div class="portada-interior-title-area">
                    <h1>{title}</h1>
                    <h2>{subtitle}</h2>
                </div>
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
            
            # Generar el HTML de la portadilla de capítulo con imagen de fondo (con la clase portada-capitulo que tiene page: page_portada_capitulo;)
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
            
        elif "ACTIVIDAD 1" in page_title or "EL LABERINTO" in page_title:
            # Generar Laberinto SVG interactivo vectorial real
            entrada_emoji = "🚀" if es_espacio else "🦔"
            salida_emoji = "🪐" if es_espacio else "🏡"
            pared_color = "#1d3557" if es_espacio else "#2a9d8f"
            fondo_color = "#f4f9f9" if es_espacio else "#f4f9f4"
            
            svg_laberinto = f"""
            <svg class="actividad-svg" width="310" height="310" viewBox="0 0 340 340">
                <rect x="10" y="10" width="320" height="320" rx="15" fill="{fondo_color}" stroke="{pared_color}" stroke-width="2" />
                <!-- Iconos Entrada y Salida -->
                <text x="35" y="45" font-size="22" text-anchor="middle">{entrada_emoji}</text>
                <text x="305" y="315" font-size="22" text-anchor="middle">{salida_emoji}</text>
                <!-- Paredes Exteriores -->
                <path d="M 50,20 L 320,20 L 320,290 M 20,320 L 20,50 M 20,320 L 290,320" stroke="{pared_color}" stroke-width="4" stroke-linecap="round" fill="none" />
                <!-- Paredes Interiores -->
                <path d="M 50,50 L 80,50 M 110,50 L 170,50 M 20,80 L 50,80 M 80,80 L 110,80 M 140,80 L 200,80 M 230,80 L 260,80 M 290,80 L 320,80
                         M 50,110 L 110,110 M 140,110 L 170,110 M 200,110 L 260,110 M 290,110 L 320,110
                         M 80,140 L 140,140 M 170,140 L 230,140 M 260,140 L 290,140
                         M 20,170 L 50,170 M 80,170 L 110,170 M 140,170 L 200,170 M 230,170 L 290,170
                         M 50,200 L 80,200 M 110,200 L 140,200 M 170,200 L 230,200 M 260,200 L 320,200
                         M 20,230 L 80,230 M 110,230 L 170,230 M 200,230 L 260,230 M 290,230 L 320,230
                         M 50,260 L 110,260 M 140,260 L 200,260 M 230,260 L 290,260
                         M 20,290 L 50,290 M 80,290 L 140,290 M 170,290 L 230,290 M 260,290 L 320,290" 
                       stroke="{pared_color}" stroke-width="3" stroke-linecap="round" fill="none" />
                <path d="M 50,20 L 50,50 M 50,80 L 50,140 M 50,170 L 50,230 M 50,260 L 50,290
                         M 80,50 L 80,110 M 80,140 L 80,200 M 80,230 L 80,260 M 80,290 L 80,320
                         M 110,20 L 110,80 M 110,110 L 110,170 M 110,200 L 110,290
                         M 140,50 L 140,110 M 140,140 L 140,230 M 140,260 L 140,320
                         M 170,80 L 170,140 M 170,170 L 170,200 M 170,230 L 170,290
                         M 200,20 L 200,80 M 200,110 L 200,170 M 200,200 L 200,260 M 200,290 L 200,320
                         M 230,50 L 230,110 M 230,140 L 230,230 M 230,260 L 230,320
                         M 260,20 L 260,50 M 260,80 L 260,170 M 260,200 L 260,290
                         M 290,50 L 290,140 M 290,170 L 290,260 M 290,290 L 290,320" 
                       stroke="{pared_color}" stroke-width="3" stroke-linecap="round" fill="none" />
            </svg>
            """
            
            # Limpiar contenido del markdown
            instruccion = re.sub(r'###\s+.*', '', page_content).strip()
            instruccion = re.sub(r'\*\*.*?\*\*', '', instruccion).strip()
            instruccion_html = format_body_text(instruccion)
            
            titulo_h3 = "🧩 ¡Guía al Cohete de Nico y Luna!" if es_espacio else "🧩 ¡Ayuda a Nico y Luna!"
            
            html_out.append(f"""
            <div class="{page_class}">
                <div class="page-title">{page_title}</div>
                <div class="actividad-container">
                    <h3>{titulo_h3}</h3>
                    <div class="actividad-instrucciones">{instruccion_html}</div>
                    {svg_laberinto}
                </div>
            </div>
            """)
            
        elif "ACTIVIDAD 2" in page_title or "DIFERENCIAS" in page_title:
            # Generar Diferencias SVG vectorial limpio
            if es_espacio:
                svg_diferencias = """
                <svg class="actividad-svg" width="480" height="200" viewBox="0 0 600 240">
                    <!-- Escena A -->
                    <g transform="translate(10, 10)">
                        <rect x="0" y="0" width="270" height="210" rx="10" fill="#ffffff" stroke="#222222" stroke-width="2.5" />
                        <text x="135" y="25" font-family="'Fredoka', sans-serif" font-size="11" text-anchor="middle" font-weight="bold" fill="#444444">DIBUJO A</text>
                        <!-- Cohete -->
                        <path d="M 135,50 L 155,90 L 155,150 L 115,150 L 115,90 Z" fill="none" stroke="#222222" stroke-width="3" />
                        <circle cx="135" cy="110" r="12" fill="none" stroke="#222222" stroke-width="2.5" />
                        <path d="M 115,130 L 95,160 L 115,160 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <path d="M 155,130 L 175,160 L 155,160 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <path d="M 125,150 L 135,170 L 145,150" fill="none" stroke="#222222" stroke-width="2" />
                        <!-- Antena -->
                        <line x1="135" y1="50" x2="135" y2="35" stroke="#222222" stroke-width="2.5" />
                        <circle cx="135" cy="35" r="4" fill="#222222" />
                        <!-- Planeta -->
                        <circle cx="50" cy="75" r="18" fill="none" stroke="#222222" stroke-width="2.5" />
                        <ellipse cx="50" cy="75" rx="25" ry="5" fill="none" stroke="#222222" stroke-width="2" transform="rotate(-15, 50, 75)" />
                        <!-- Estrellas -->
                        <path d="M 220,55 L 222,60 L 227,60 L 223,64 L 224,69 L 220,66 L 216,69 L 217,64 L 213,60 L 218,60 Z" fill="none" stroke="#222222" stroke-width="2" />
                        <path d="M 235,115 L 236,118 L 240,118 L 237,121 L 238,125 L 235,123 L 232,125 L 233,121 L 230,118 L 234,118 Z" fill="none" stroke="#222222" stroke-width="1.5" />
                        <!-- 3 Burbujas de propulsión -->
                        <circle cx="120" cy="190" r="5" fill="none" stroke="#222222" stroke-width="2" />
                        <circle cx="135" cy="195" r="4" fill="none" stroke="#222222" stroke-width="2" />
                        <circle cx="150" cy="190" r="6" fill="none" stroke="#222222" stroke-width="2" />
                    </g>
                    <!-- Escena B (5 diferencias) -->
                    <g transform="translate(320, 10)">
                        <rect x="0" y="0" width="270" height="210" rx="10" fill="#ffffff" stroke="#222222" stroke-width="2.5" />
                        <text x="135" y="25" font-family="'Fredoka', sans-serif" font-size="11" text-anchor="middle" font-weight="bold" fill="#444444">DIBUJO B</text>
                        <!-- Cohete -->
                        <path d="M 135,50 L 155,90 L 155,150 L 115,150 L 115,90 Z" fill="none" stroke="#222222" stroke-width="3" />
                        <!-- DIFERENCIA 4: Falta la ventana redonda central -->
                        <!-- Aletas -->
                        <path d="M 115,130 L 95,160 L 115,160 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <path d="M 155,130 L 175,160 L 155,160 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <path d="M 125,150 L 135,170 L 145,150" fill="none" stroke="#222222" stroke-width="2" />
                        <!-- DIFERENCIA 1: Falta la antena del casco/cohete -->
                        <!-- Planeta -->
                        <circle cx="50" cy="75" r="18" fill="none" stroke="#222222" stroke-width="2.5" />
                        <!-- DIFERENCIA 5: Falta el anillo del planeta -->
                        <!-- Estrellas -->
                        <!-- DIFERENCIA 2: Falta la estrella superior der -->
                        <path d="M 235,115 L 236,118 L 240,118 L 237,121 L 238,125 L 235,123 L 232,125 L 233,121 L 230,118 L 234,118 Z" fill="none" stroke="#222222" stroke-width="1.5" />
                        <!-- DIFERENCIA 3: Falta una burbuja del motor (solo 2) -->
                        <circle cx="120" cy="190" r="5" fill="none" stroke="#222222" stroke-width="2" />
                        <circle cx="150" cy="190" r="6" fill="none" stroke="#222222" stroke-width="2" />
                    </g>
                </svg>
                """
                diferencias_list = """
                <ul class="actividad-lista-diferencias">
                    <li>[  ] 1. Antena en la punta</li>
                    <li>[  ] 2. Estrella de arriba</li>
                    <li>[  ] 3. Burbuja del motor</li>
                    <li>[  ] 4. Ventana del cohete</li>
                    <li>[  ] 5. Anillo del planeta</li>
                </ul>
                """
            else:
                svg_diferencias = """
                <svg class="actividad-svg" width="480" height="200" viewBox="0 0 600 240">
                    <!-- Escena A -->
                    <g transform="translate(10, 10)">
                        <rect x="0" y="0" width="270" height="210" rx="10" fill="#ffffff" stroke="#222222" stroke-width="2.5" />
                        <text x="135" y="25" font-family="'Fredoka', sans-serif" font-size="11" text-anchor="middle" font-weight="bold" fill="#444444">DIBUJO A</text>
                        <!-- Pino -->
                        <rect x="52" y="140" width="12" height="30" fill="none" stroke="#222222" stroke-width="2" />
                        <polygon points="58,65 25,105 91,105" fill="none" stroke="#222222" stroke-width="2.5" />
                        <polygon points="58,95 20,135 96,135" fill="none" stroke="#222222" stroke-width="2.5" />
                        <polygon points="58,125 15,155 101,155" fill="none" stroke="#222222" stroke-width="2.5" />
                        <!-- Seta Grande -->
                        <path d="M 175,130 Q 175,175 190,175 Q 205,175 205,130 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <path d="M 150,130 C 150,90 230,90 230,130 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <!-- Lunares seta (4 lunares) -->
                        <circle cx="170" cy="110" r="4" fill="#222222" />
                        <circle cx="190" cy="105" r="4.5" fill="#222222" />
                        <circle cx="210" cy="115" r="4" fill="#222222" />
                        <circle cx="190" cy="122" r="3.5" fill="#222222" />
                        <!-- Sol sonriente -->
                        <circle cx="230" cy="45" r="15" fill="none" stroke="#222222" stroke-width="2" />
                        <!-- Rayos (6 rayos) -->
                        <line x1="230" y1="26" x2="230" y2="18" stroke="#222222" stroke-width="2" />
                        <line x1="230" y1="64" x2="230" y2="72" stroke="#222222" stroke-width="2" />
                        <line x1="211" y1="45" x2="203" y2="45" stroke="#222222" stroke-width="2" />
                        <line x1="249" y1="45" x2="257" y2="45" stroke="#222222" stroke-width="2" />
                        <line x1="216" y1="31" x2="210" y2="25" stroke="#222222" stroke-width="2" />
                        <line x1="244" y1="59" x2="250" y2="65" stroke="#222222" stroke-width="2" />
                        <!-- Flor -->
                        <path d="M 115,150 Q 110,165 115,185" fill="none" stroke="#222222" stroke-width="2" />
                        <circle cx="115" cy="142" r="5" fill="none" stroke="#222222" stroke-width="2" />
                        <!-- Pétalos (5 pétalos) -->
                        <circle cx="115" cy="132" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <circle cx="125" cy="139" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <circle cx="121" cy="151" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <circle cx="109" cy="151" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <circle cx="105" cy="139" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <!-- Piedra pequeña al pie -->
                        <path d="M 23,175 Q 33,167 43,175 Q 33,183 23,175 Z" fill="none" stroke="#222222" stroke-width="2" />
                    </g>
                    <!-- Escena B (5 diferencias) -->
                    <g transform="translate(320, 10)">
                        <rect x="0" y="0" width="270" height="210" rx="10" fill="#ffffff" stroke="#222222" stroke-width="2.5" />
                        <text x="135" y="25" font-family="'Fredoka', sans-serif" font-size="11" text-anchor="middle" font-weight="bold" fill="#444444">DIBUJO B</text>
                        <!-- Pino -->
                        <rect x="52" y="140" width="12" height="30" fill="none" stroke="#222222" stroke-width="2" />
                        <polygon points="58,65 25,105 91,105" fill="none" stroke="#222222" stroke-width="2.5" />
                        <polygon points="58,95 20,135 96,135" fill="none" stroke="#222222" stroke-width="2.5" />
                        <polygon points="58,125 15,155 101,155" fill="none" stroke="#222222" stroke-width="2.5" />
                        <!-- Seta Grande -->
                        <path d="M 175,130 Q 175,175 190,175 Q 205,175 205,130 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <path d="M 150,130 C 150,90 230,90 230,130 Z" fill="none" stroke="#222222" stroke-width="2.5" />
                        <!-- DIFERENCIA 4: A la seta le faltan los lunares -->
                        <!-- Sol sonriente -->
                        <circle cx="230" cy="45" r="15" fill="none" stroke="#222222" stroke-width="2" />
                        <!-- DIFERENCIA 2: Al sol le faltan los rayos -->
                        <!-- Flor -->
                        <path d="M 115,150 Q 110,165 115,185" fill="none" stroke="#222222" stroke-width="2" />
                        <circle cx="115" cy="142" r="5" fill="none" stroke="#222222" stroke-width="2" />
                        <!-- DIFERENCIA 3: A la flor le falta un pétalo (solo 4) -->
                        <circle cx="115" cy="132" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <circle cx="125" cy="139" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <circle cx="121" cy="151" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <circle cx="109" cy="151" r="5" fill="none" stroke="#222222" stroke-width="1.5" />
                        <!-- DIFERENCIA 5: Falta la piedra pequeña al pie del pino -->
                    </g>
                </svg>
                """
                diferencias_list = """
                <ul class="actividad-lista-diferencias">
                    <li>[  ] 1. Rayos del sol sonriente</li>
                    <li>[  ] 2. Lunares de la seta grande</li>
                    <li>[  ] 3. Pétalo de la flor silvestre</li>
                    <li>[  ] 4. Piedra junto al pie del pino</li>
                    <li>[  ] 5. Altura del tronco del pino</li>
                </ul>
                """
            
            html_out.append(f"""
            <div class="{page_class}">
                <div class="page-title">{page_title}</div>
                <div class="actividad-container">
                    <h3>🔍 ¡Encuentra las 5 diferencias!</h3>
                    <div class="actividad-instrucciones">Compara los dos dibujos y marca las 5 diferencias que encuentres en el dibujo B. ¡Luego coloréalos!</div>
                    {svg_diferencias}
                    {diferencias_list}
                </div>
            </div>
            """)
            
        elif "ACTIVIDAD 3" in page_title or "CONECTA LOS PUNTOS" in page_title or "CONECTA PUNTOS" in page_title:
            # Conecta los puntos SVG vectorial
            if es_espacio:
                svg_conecta = """
                <svg class="actividad-svg" width="300" height="300" viewBox="0 0 300 300">
                    <!-- Dibujo base pre-existente -->
                    <circle cx="150" cy="130" r="16" fill="none" stroke="#222222" stroke-width="2.5" />
                    <circle cx="150" cy="130" r="22" fill="none" stroke="#222222" stroke-width="1.5" />
                    <path d="M 125,170 L 95,210 L 125,225" fill="none" stroke="#222222" stroke-width="2.5" stroke-linecap="round" />
                    <path d="M 175,170 L 205,210 L 175,225" fill="none" stroke="#222222" stroke-width="2.5" stroke-linecap="round" />
                    <path d="M 135,230 L 142,260 L 150,240 L 158,260 L 165,230" fill="none" stroke="#222222" stroke-width="2" stroke-linejoin="round" />
                    <!-- Elementos fondo -->
                    <circle cx="50" cy="60" r="12" fill="none" stroke="#dddddd" stroke-width="1.5" />
                    <ellipse cx="50" cy="60" rx="18" ry="4" fill="none" stroke="#dddddd" stroke-width="1.2" transform="rotate(-10, 50, 60)" />
                    <!-- Puntos -->
                    <g>
                        <circle cx="150" cy="40" r="4" fill="#000000" /><text x="150" y="32" font-size="10" text-anchor="middle" font-weight="bold">1</text>
                        <circle cx="162" cy="60" r="4" fill="#000000" /><text x="172" y="62" font-size="10" text-anchor="start" font-weight="bold">2</text>
                        <circle cx="170" cy="80" r="4" fill="#000000" /><text x="180" y="82" font-size="10" text-anchor="start" font-weight="bold">3</text>
                        <circle cx="175" cy="100" r="4" fill="#000000" /><text x="185" y="102" font-size="10" text-anchor="start" font-weight="bold">4</text>
                        <circle cx="175" cy="120" r="4" fill="#000000" /><text x="185" y="122" font-size="10" text-anchor="start" font-weight="bold">5</text>
                        <circle cx="175" cy="140" r="4" fill="#000000" /><text x="185" y="142" font-size="10" text-anchor="start" font-weight="bold">6</text>
                        <circle cx="175" cy="160" r="4" fill="#000000" /><text x="185" y="162" font-size="10" text-anchor="start" font-weight="bold">7</text>
                        <circle cx="175" cy="180" r="4" fill="#000000" /><text x="185" y="182" font-size="10" text-anchor="start" font-weight="bold">8</text>
                        <circle cx="175" cy="200" r="4" fill="#000000" /><text x="185" y="202" font-size="10" text-anchor="start" font-weight="bold">9</text>
                        <circle cx="175" cy="230" r="4" fill="#000000" /><text x="185" y="234" font-size="10" text-anchor="start" font-weight="bold">10</text>
                        <circle cx="160" cy="230" r="4" fill="#000000" /><text x="160" y="222" font-size="10" text-anchor="middle" font-weight="bold">11</text>
                        <circle cx="150" cy="230" r="4" fill="#000000" /><text x="150" y="222" font-size="10" text-anchor="middle" font-weight="bold">12</text>
                        <circle cx="140" cy="230" r="4" fill="#000000" /><text x="140" y="222" font-size="10" text-anchor="middle" font-weight="bold">13</text>
                        <circle cx="125" cy="230" r="4" fill="#000000" /><text x="115" y="234" font-size="10" text-anchor="end" font-weight="bold">14</text>
                        <circle cx="125" cy="200" r="4" fill="#000000" /><text x="115" y="202" font-size="10" text-anchor="end" font-weight="bold">15</text>
                        <circle cx="125" cy="180" r="4" fill="#000000" /><text x="115" y="182" font-size="10" text-anchor="end" font-weight="bold">16</text>
                        <circle cx="125" cy="160" r="4" fill="#000000" /><text x="115" y="162" font-size="10" text-anchor="end" font-weight="bold">17</text>
                        <circle cx="125" cy="140" r="4" fill="#000000" /><text x="115" y="142" font-size="10" text-anchor="end" font-weight="bold">18</text>
                        <circle cx="125" cy="100" r="4" fill="#000000" /><text x="115" y="102" font-size="10" text-anchor="end" font-weight="bold">19</text>
                        <circle cx="138" cy="60" r="4" fill="#000000" /><text x="128" y="62" font-size="10" text-anchor="end" font-weight="bold">20</text>
                    </g>
                </svg>
                """
            else:
                svg_conecta = """
                <svg class="actividad-svg" width="300" height="300" viewBox="0 0 300 300">
                    <!-- Dibujo base pre-existente -->
                    <circle cx="130" cy="120" r="18" fill="none" stroke="#222222" stroke-width="2" />
                    <circle cx="130" cy="120" r="6" fill="#222222" />
                    <circle cx="170" cy="120" r="18" fill="none" stroke="#222222" stroke-width="2" />
                    <circle cx="170" cy="120" r="6" fill="#222222" />
                    <polygon points="150,132 144,142 156,142" fill="#222222" />
                    <path d="M 125,160 Q 150,175 175,160" fill="none" stroke="#222222" stroke-width="1.5" />
                    <path d="M 130,175 Q 150,190 170,175" fill="none" stroke="#222222" stroke-width="1.5" />
                    <path d="M 60,240 L 240,240 Q 250,230 230,225" fill="none" stroke="#222222" stroke-width="3" stroke-linecap="round" />
                    <line x1="135" y1="210" x2="130" y2="240" stroke="#222222" stroke-width="2.5" />
                    <line x1="135" y1="210" x2="138" y2="240" stroke="#222222" stroke-width="2.5" />
                    <line x1="165" y1="210" x2="162" y2="240" stroke="#222222" stroke-width="2.5" />
                    <line x1="165" y1="210" x2="170" y2="240" stroke="#222222" stroke-width="2.5" />
                    <!-- Puntos -->
                    <g>
                        <circle cx="150" cy="60" r="4" fill="#000000" /><text x="150" y="52" font-size="10" text-anchor="middle" font-weight="bold">1</text>
                        <circle cx="170" cy="65" r="4" fill="#000000" /><text x="178" y="63" font-size="10" text-anchor="start" font-weight="bold">2</text>
                        <circle cx="180" cy="85" r="4" fill="#000000" /><text x="188" y="85" font-size="10" text-anchor="start" font-weight="bold">3</text>
                        <circle cx="185" cy="105" r="4" fill="#000000" /><text x="193" y="105" font-size="10" text-anchor="start" font-weight="bold">4</text>
                        <circle cx="200" cy="120" r="4" fill="#000000" /><text x="208" y="120" font-size="10" text-anchor="start" font-weight="bold">5</text>
                        <circle cx="215" cy="140" r="4" fill="#000000" /><text x="223" y="140" font-size="10" text-anchor="start" font-weight="bold">6</text>
                        <circle cx="218" cy="160" r="4" fill="#000000" /><text x="226" y="160" font-size="10" text-anchor="start" font-weight="bold">7</text>
                        <circle cx="210" cy="180" r="4" fill="#000000" /><text x="218" y="180" font-size="10" text-anchor="start" font-weight="bold">8</text>
                        <circle cx="195" cy="195" r="4" fill="#000000" /><text x="203" y="195" font-size="10" text-anchor="start" font-weight="bold">9</text>
                        <circle cx="180" cy="210" r="4" fill="#000000" /><text x="188" y="210" font-size="10" text-anchor="start" font-weight="bold">10</text>
                        <circle cx="165" cy="215" r="4" fill="#000000" /><text x="165" y="227" font-size="10" text-anchor="middle" font-weight="bold">11</text>
                        <circle cx="135" cy="215" r="4" fill="#000000" /><text x="135" y="227" font-size="10" text-anchor="middle" font-weight="bold">12</text>
                        <circle cx="120" cy="210" r="4" fill="#000000" /><text x="112" y="210" font-size="10" text-anchor="end" font-weight="bold">13</text>
                        <circle cx="105" cy="195" r="4" fill="#000000" /><text x="97" y="195" font-size="10" text-anchor="end" font-weight="bold">14</text>
                        <circle cx="90" cy="180" r="4" fill="#000000" /><text x="82" y="180" font-size="10" text-anchor="end" font-weight="bold">15</text>
                        <circle cx="82" cy="160" r="4" fill="#000000" /><text x="74" y="160" font-size="10" text-anchor="end" font-weight="bold">16</text>
                        <circle cx="85" cy="140" r="4" fill="#000000" /><text x="77" y="140" font-size="10" text-anchor="end" font-weight="bold">17</text>
                        <circle cx="100" cy="120" r="4" fill="#000000" /><text x="92" y="120" font-size="10" text-anchor="end" font-weight="bold">18</text>
                        <circle cx="115" cy="85" r="4" fill="#000000" /><text x="107" y="85" font-size="10" text-anchor="end" font-weight="bold">19</text>
                        <circle cx="130" cy="65" r="4" fill="#000000" /><text x="122" y="63" font-size="10" text-anchor="end" font-weight="bold">20</text>
                    </g>
                </svg>
                """
            
            html_out.append(f"""
            <div class="{page_class}">
                <div class="page-title">{page_title}</div>
                <div class="actividad-container">
                    <h3>✏️ ¡Une los puntos del 1 al 20!</h3>
                    <div class="actividad-instrucciones">Completa el dibujo trazando una línea entre los números del 1 al 20 en orden. ¡Luego dale color!</div>
                    {svg_conecta}
                </div>
            </div>
            """)
            
        elif "ACTIVIDAD 4" in page_title or "DIBUJO Y CREATIVIDAD" in page_title or "DIBUJO" in page_title:
            # Lienzo decorado para dibujo libre
            deco_tl = "⭐" if es_espacio else "🌸"
            deco_tr = "🪐" if es_espacio else "🌿"
            deco_bl = "🚀" if es_espacio else "🍄"
            deco_br = "✨" if es_espacio else "🐞"
            
            label_p1 = "Nombre de tu planeta o alien:" if es_espacio else "Nombre de tu criatura:"
            label_p2 = "¿Qué le gusta comer / poderes?:" if es_espacio else "¿Qué poder mágico tiene?:"
            
            html_out.append(f"""
            <div class="{page_class}">
                <div class="page-title">{page_title}</div>
                <div class="actividad-container">
                    <h3>🎨 ¡Diseña tu propia Creación!</h3>
                    <div class="actividad-instrucciones">Dibuja y dale color a tu propia criatura o planeta del espacio en este marco decorado. ¡Sé creativo!</div>
                    
                    <div class="canvas-dibujo-decorativo">
                        <span class="canvas-decoracion-esquina canvas-decoracion-tl">{deco_tl}</span>
                        <span class="canvas-decoracion-esquina canvas-decoracion-tr">{deco_tr}</span>
                        <span class="canvas-decoracion-esquina canvas-decoracion-bl">{deco_bl}</span>
                        <span class="canvas-decoracion-esquina canvas-decoracion-br">{deco_br}</span>
                    </div>
                    
                    <div class="campos-dibujo-libre">
                        <div class="campo-escritura"><strong>{label_p1}</strong> <span></span></div>
                        <div class="campo-escritura"><strong>{label_p2}</strong> <span></span></div>
                    </div>
                </div>
            </div>
            """)
            
        elif "PROBADOR DE COLORES" in page_title or "PROBADOR DE LÁPICES" in page_title or "PROBADOR DE ROTULADORES" in page_title:
            # Probadores
            titulo_probador = "🖍️ Probador de Lápices de Colores" if "LÁPICES" in page_title else "🎨 Probador de Rotuladores"
            desc_probador = ("Prueba el trazo, la presión y los tonos de tus lápices o ceras de colores."
                             if "LÁPICES" in page_title else
                             "Prueba la intensidad de tus rotuladores y asegúrate de que no traspase el papel.")
            
            html_out.append(f"""
            <div class="{page_class}">
                <div class="page-title">{page_title}</div>
                <div class="actividad-container">
                    <h3>{titulo_probador}</h3>
                    <div class="actividad-instrucciones">{desc_probador}</div>
                    
                    <div class="probador-container">
                        <div class="probador-caja">
                            <h4>Color Suave</h4>
                            <p style="font-size: 8.5pt; color: #666666; margin: 4px 0;">Pinta con trazos muy suaves.</p>
                            <div class="probador-zonas">
                                <div class="probador-zona-color"></div>
                                <div class="probador-zona-color"></div>
                            </div>
                        </div>
                        
                        <div class="probador-caja">
                            <h4>Color Fuerte</h4>
                            <p style="font-size: 8.5pt; color: #666666; margin: 4px 0;">Pinta con trazos más fuertes.</p>
                            <div class="probador-zonas">
                                <div class="probador-zona-color"></div>
                                <div class="probador-zona-color"></div>
                            </div>
                        </div>
                        
                        <div class="probador-caja" style="width: 96%; height: 1.6in;">
                            <h4>Mezcla y Degradados</h4>
                            <p style="font-size: 8.5pt; color: #666666; margin: 4px 0;">Prueba a degradar un color o a mezclar dos colores diferentes en esta zona.</p>
                            <div class="probador-zona-rectangular"></div>
                        </div>
                    </div>
                </div>
            </div>
            """)
            
        else:
            # Páginas normales (Lectura con y sin imágenes)
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
                        <div class="lectura-texto" style="padding: 0 0.4in; margin-bottom: 10px;">{clean_content}</div>
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
