#!/usr/bin/env python3
import os
import sys
import re
import subprocess

# Datos de los Libros
BOOKS_DATA = {
    "libro_1_el_bosque_magico": {
        "num": 1,
        "subtitulo": "El Bosque Mágico",
        "sinopsis": """¡Acompaña a Nico, Luna y su travieso perrito Copito en un viaje mágico al corazón de un bosque encantado!

En este libro híbrido premium de cuento ilustrado y actividades, descubrirás una entrañable historia de amistad y generosidad. Cada página de lectura a color viene acompañada de una hermosa página ilustrada en gran tamaño para leer, y páginas interactivas en blanco y negro para colorear y pintar.

¡Fomenta la creatividad, la concentración y la lectura temprana con divertidas sopas de letras, busca y cuenta, conecta los puntos y juegos de diferencias al final del libro!

Ideal para pequeños lectores y artistas de 4 a 8 años.""",
        "bg_color": "#d6ebdc",
        "border_color": "#8ea696",
        "text_color": "#2c3e35",
        "accent_color": "#234d36"
    },
    "libro_2_viaje_al_espacio": {
        "num": 2,
        "subtitulo": "Viaje al Espacio",
        "sinopsis": """¡Despega hacia las estrellas con Nico, Luna y su perrito Copito en una aventura espacial inolvidable!

Construye un cohete de cartón, viaja más allá de las nubes y descubre planetas sonrientes hechos de helado de fresa. En este volumen premium de 60 páginas, Nico y Luna harán nuevos amigos intergalécticos como el Robot Tuerca y el adorable alienígena Bip-Bip.

Cada escena del viaje combina una página de cuento con hermosas ilustraciones infantiles a color alternadas con láminas en blanco y negro listas para colorear.

¡Fomenta el aprendizaje, la lectura temprana y la creatividad con divertidas sopas de letras, busca y cuenta, conecta los puntos y juegos de diferencias al final del libro!

Ideal para niños de 4 a 8 años.""",
        "bg_color": "#0d1b2a",
        "border_color": "#415a77",
        "text_color": "#e0e1dd",
        "accent_color": "#e0a96d"
    },
    "libro_3_los_dinosaurios_perdidos": {
        "num": 3,
        "subtitulo": "Los Dinosaurios Perdidos",
        "sinopsis": """¡Viaja en el tiempo con Nico, Luna y su valiente perrito Copito a un asombroso valle prehistórico!

Cruza un portal mágico y conoce a entrañables amigos gigantes como el pequeño tiranosaurio Dino y el bondadoso Brontosaurio de cuello largo. En este volumen premium de 60 páginas, Nico y Luna le ayudarán a buscar sus juguetes perdidos a través de cascadas tibias y cuevas de cristales luminosos.

Cada escena del viaje combina una página de lectura ágil en la izquierda con hermosas ilustraciones infantiles a color alternadas con láminas en blanco y negro listas para colorear a la derecha.

¡Fomenta la creatividad, la lectura temprana y la concentración con divertidas sopas de letras, busca y cuenta, conecta los puntos, conecta las sombras y juegos de diferencias al final del libro!

Ideal para niños de 4 a 8 años.""",
        "bg_color": "#1e3f20", # Verde selva jurásica profundo
        "border_color": "#345e37",
        "text_color": "#eaf2eb",
        "accent_color": "#ffb703" # Naranja sol prehistórico
    }
}

CSS_TEMPLATE = """@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Nunito:wght@400;700&display=swap');

@page {{
    size: 17.385in 11.25in;
    margin: 0;
}}

body {{
    margin: 0;
    padding: 0;
    font-family: 'Nunito', sans-serif;
    background-color: #ffffff;
    -webkit-print-color-adjust: exact;
}}

.cover-wrapper {{
    display: flex;
    width: 17.385in;
    height: 11.25in;
    box-sizing: border-box;
    overflow: hidden;
}}

/* Contraportada (Back Cover) - Izquierda */
.back-cover {{
    width: 8.625in; /* 8.5in + 0.125in sangría izquierda */
    height: 11.25in;
    background-color: {bg_color};
    border-right: 1px dashed rgba(0,0,0,0.1);
    position: relative;
    box-sizing: border-box;
}}

/* Se elimina .back-content ya que usamos posicionamiento absoluto en sus hijos */

.back-container {{
    position: absolute;
    top: 0.8in;
    bottom: 0.8in;
    left: 0.925in; /* 0.8in + 0.125in de sangría izquierda */
    right: 0.8in; /* Margen seguro con el lomo */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
}}

.back-header {{
    border-bottom: 3px double {border_color};
    padding-bottom: 12px;
    text-align: center;
    margin-bottom: 15px;
}}

.back-header h2 {{
    font-family: 'Fredoka', sans-serif;
    font-size: 18pt;
    color: {accent_color};
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 1px;
}}

.sinopsis {{
    font-size: 11pt;
    line-height: 1.6;
    color: {text_color};
    text-align: justify;
    margin: 0;
    white-space: pre-line;
}}

.specs {{
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 15px;
    margin-bottom: 15px;
}}

.tag {{
    background-color: rgba(255,255,255,0.7);
    border: 1px solid {border_color};
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 9.5pt;
    font-weight: bold;
    color: {accent_color};
    text-transform: uppercase;
}}

.barcode-area {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid {border_color};
    padding-top: 15px;
    width: 100%;
}}

.barcode-box {{
    width: 2.0in;
    height: 1.2in;
    background-color: #ffffff;
    border: 1px dashed #999999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 8pt;
    color: #666666;
    font-weight: bold;
    box-sizing: border-box;
    padding: 5px;
    text-align: center;
}}

.isbn-label {{
    font-size: 9.5pt;
    color: {text_color};
    font-style: italic;
    text-align: left;
    max-width: 3.5in;
    line-height: 1.4;
}}

/* Lomo (Spine) - Centro */
.spine {{
    width: 0.135in;
    height: 11.25in;
    background-color: {bg_color};
    position: relative;
    box-sizing: border-box;
}}

.spine-text {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(90deg);
    transform-origin: center;
    white-space: nowrap;
    font-family: 'Fredoka', sans-serif;
    font-size: 7.5pt; /* Reducido ligeramente para seguridad de pliegue KDP */
    font-weight: 600;
    letter-spacing: 1px;
    color: {accent_color};
    text-transform: uppercase;
}}

/* Portada Frontal (Front Cover) - Derecha */
.front-cover {{
    width: 8.625in; /* 8.5in + 0.125in sangría derecha */
    height: 11.25in;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    position: relative;
    box-sizing: border-box;
}}

.front-content {{
    position: relative;
    width: 100%;
    height: 100%;
}}

.front-header-container {{
    position: absolute;
    top: 0.8in;
    left: 0.8in;
    right: 0.925in; /* Margen seguro con sangría derecha */
    text-align: center;
    box-sizing: border-box;
}}

.subtitle-container {{
    display: flex;
    justify-content: center;
    width: 100%;
    margin-top: 15px;
}}

.main-title {{
    font-family: 'Fredoka', sans-serif;
    font-size: 34pt;
    font-weight: 600;
    text-align: center;
    color: #ffffff;
    text-shadow: 2px 2px 0px #000000, -2px -2px 0px #000000, 2px -2px 0px #000000, -2px 2px 0px #000000, 0px 4px 10px rgba(0,0,0,0.5);
    margin: 0;
    line-height: 1.1;
    text-transform: uppercase;
}}

.subtitle-badge {{
    background-color: rgba(255, 255, 255, 0.9);
    border: 3px solid #222222;
    border-radius: 12px;
    padding: 10px 25px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    transform: rotate(-1deg);
    margin-top: 10px;
}}

.sub-title {{
    font-family: 'Fredoka', sans-serif;
    font-size: 20pt;
    color: #c71585; /* Rosa vibrante */
    margin: 0;
    text-align: center;
    text-transform: uppercase;
}}

.author-label {{
    position: absolute;
    bottom: 0.8in;
    left: 1.5in;
    right: 1.625in; /* Ajustado por sangría */
    font-family: 'Fredoka', sans-serif;
    font-size: 13pt;
    font-weight: 600;
    color: #ffffff;
    text-shadow: 1px 1px 0px #000000, -1px -1px 0px #000000, 1px -1px 0px #000000, -1px 1px 0px #000000;
    background-color: rgba(0, 0, 0, 0.65);
    padding: 6px 20px;
    border-radius: 20px;
    text-align: center;
}}
"""

def main():
    if len(sys.argv) < 2:
        print("Uso: compile_cover.py <book_directory_path>")
        sys.exit(1)
        
    book_dir = os.path.abspath(sys.argv[1])
    if not os.path.isdir(book_dir):
        print(f"Error: {book_dir} no es un directorio válido.")
        sys.exit(1)
        
    book_key = os.path.basename(book_dir)
    if book_key not in BOOKS_DATA:
        print(f"Error: No se reconocen datos para el libro '{book_key}'")
        sys.exit(1)
        
    info = BOOKS_DATA[book_key]
    print(f"Compilando cubierta KDP para: {book_key} (Libro {info['num']})")
    
    # Buscar imagen de portada
    cover_dir = os.path.join(book_dir, "cover")
    cover_images = [f for f in os.listdir(cover_dir) if f.endswith(".jpg") and "cover" in f]
    
    if not cover_images:
        print(f"Error: No se encontró la ilustración de portada en {cover_dir}")
        sys.exit(1)
        
    cover_img_path = os.path.join(cover_dir, cover_images[0])
    print(f"Ilustración de portada encontrada: {cover_img_path}")
    
    # Renderizar plantilla CSS
    css_rendered = CSS_TEMPLATE.format(
        bg_color=info["bg_color"],
        border_color=info["border_color"],
        text_color=info["text_color"],
        accent_color=info["accent_color"]
    )
    
    # Tono de color alternativo del lomo/subtítulo para libro 2
    if info["num"] == 2:
        css_rendered = css_rendered.replace("color: #c71585;", "color: #ff8c00;") # Naranja en el libro 2
        
    # Cabecera condicional para portada (solo para Libro 3, que tiene portada limpia sin texto)
    if info["num"] == 3:
        portada_header = f"""
                <div class="front-header-container">
                    <div class="main-title">Las Aventuras de</div>
                    <div class="main-title" style="font-size: 38pt; font-weight: 600; margin-top: 5px;">Nico y Luna</div>
                    <div class="subtitle-container">
                        <div class="subtitle-badge">
                            <h2 class="sub-title">{info['subtitulo']}</h2>
                        </div>
                    </div>
                </div>
        """
    else:
        portada_header = ""
        
    # Generar HTML
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
    {css_rendered}
    </style>
</head>
<body>
    <div class="cover-wrapper">
        <!-- Contraportada -->
        <div class="back-cover">
            <div class="back-container">
                <div class="back-header">
                    <h2>Colección Nico y Luna</h2>
                </div>
                
                <p class="sinopsis">{info['sinopsis']}</p>
                
                <div class="specs">
                    <span class="tag">Lectura A Color</span>
                    <span class="tag">10 Láminas de Pintar</span>
                    <span class="tag">Juegos y Actividades</span>
                </div>
                
                <div class="barcode-area">
                    <div class="isbn-label">
                        Colección Nico y Luna<br>
                        Libro {info['num']} de la Colección<br>
                        Edición Especial Impresa
                    </div>
                    <div class="barcode-box">
                        CÓDIGO BARRAS KDP<br>
                        <span style="font-size: 6.5pt; font-weight: normal; color: #999999; margin-top: 4px; display: inline-block;">(Espacio reservado 2"x1.2")</span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Lomo -->
        <div class="spine">
            <div class="spine-text">
                LAS AVENTURAS DE NICO Y LUNA &mdash; LIBRO {info['num']} &mdash; JULIO MARTÍN RODRÍGUEZ SÁNCHEZ
            </div>
        </div>
        
        <!-- Portada -->
        <div class="front-cover" style="background-image: url('{cover_img_path}');">
            <div class="front-content">
                {portada_header}
                <div class="author-label">Julio Martín Rodríguez Sánchez</div>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    final_dir = os.path.join(book_dir, "final")
    temp_html_path = os.path.join(final_dir, "temp_cover.html")
    pdf_out_path = os.path.join(final_dir, f"las_aventuras_de_nico_y_luna_{book_key.replace('libro_', '')}_cover.pdf")
    
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Ejecutando Weasyprint para compilar la Cubierta completa a PDF...")
    try:
        subprocess.run(["weasyprint", temp_html_path, pdf_out_path], check=True)
        print(f"¡Cubierta PDF Generada Exitosamente!: {pdf_out_path}")
    except Exception as e:
        print(f"Error al ejecutar Weasyprint para la cubierta: {e}")
        
    # Limpiar archivo temporal
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

if __name__ == "__main__":
    main()
