from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def obtener_color_relleno(icon_code):
    """Determina el color de relleno según el código del icono."""
    if icon_code.endswith('d'):
        return Color('orange')  # Día
    elif icon_code.endswith('n'):
        return Color('gray')  # Noche
    return Color('white')  # Default

def dibujar_figura(draw, icon_code):
    """Dibuja la figura correspondiente según el código del icono."""
    figuras = {
        '01': lambda: dibujar_cielo_despejado(draw),  # Cielo despejado
        '02': lambda: dibujar_pocas_nubes(draw),  # Pocas nubes
        '03': lambda: dibujar_nubes_dispersas(draw),  # Nubes dispersas
        '04': lambda: dibujar_nubes_densas(draw),  # Nubes densas
        '09': lambda: dibujar_llovizna(draw),  # Llovizna
        '10': lambda: dibujar_lluvia_ligera(draw),  # Lluvia ligera
        '11': lambda: dibujar_tormenta_electronica(draw),  # Tormenta eléctrica
        '13': lambda: dibujar_nieve(draw),  # Nieve
        '50': lambda: dibujar_niebla(draw),  # Niebla
    }
    
    codigo_base = icon_code[:2]
    if codigo_base in figuras:
        figuras[codigo_base]()
    else:
        draw.text(100, 150, "Icono desconocido")

# Cada una de las funciones que dibujan el clima
def dibujar_cielo_despejado(draw):
    """Dibuja un cielo despejado con un sol estilizado."""
    draw.fill_color = Color('yellow')  # Sol amarillo
    draw.circle((200, 150), (100, 150))  # Sol

def dibujar_pocas_nubes(draw):
    """Dibuja un cielo con algunas nubes dispersas."""
    draw.fill_color = Color('white')  # Nubes blancas
    draw.ellipse((150, 100), (120, 70))  # Nube 1
    draw.ellipse((250, 130), (100, 60))  # Nube 2

def dibujar_nubes_dispersas(draw):
    """Dibuja nubes dispersas por el cielo."""
    draw.fill_color = Color('white')  # Nubes blancas
    draw.ellipse((150, 100), (120, 80))  # Nube 1
    draw.ellipse((250, 130), (110, 70))  # Nube 2
    draw.ellipse((200, 200), (130, 90))  # Nube 3

def dibujar_nubes_densas(draw):
    """Dibuja muchas nubes densas cubriendo el cielo."""
    draw.fill_color = Color('gray')  # Nubes grises
    draw.ellipse((100, 100), (150, 90))  # Nube grande 1
    draw.ellipse((250, 120), (150, 100))  # Nube grande 2
    draw.ellipse((200, 200), (140, 90))  # Nube grande 3

def dibujar_llovizna(draw):
    """Dibuja gotas de lluvia suaves."""
    draw.fill_color = Color('lightblue')
    for i in range(50, 350, 50):
        draw.line((i, 150), (i, 180))  # Líneas de lluvia ligera

def dibujar_lluvia_ligera(draw):
    """Dibuja gotas de lluvia más intensas."""
    draw.fill_color = Color('blue')
    for i in range(50, 350, 30):
        draw.line((i, 150), (i, 180))  # Líneas de lluvia más largas

def dibujar_tormenta_electronica(draw):
    """Dibuja rayos en una tormenta."""
    draw.fill_color = Color('black')
    draw.polygon([(100, 150), (200, 50), (300, 150)])  # Nube
    draw.stroke_width = 4
    draw.stroke_color = Color('yellow')
    draw.line((200, 50), (220, 100))  # Rayo
    draw.line((220, 100), (250, 50))  # Rayo

def dibujar_nieve(draw):
    """Dibuja copos de nieve cayendo."""
    draw.fill_color = Color('white')
    for x in range(50, 400, 50):
        draw.circle((x, 50), 5)  # Copos de nieve

def dibujar_niebla(draw):
    """Dibuja una niebla ligera."""
    draw.fill_color = Color('gray')
    draw.opacity = 0.5  # Efecto de niebla (translúcido)
    draw.bezier([(50, 150), (150, 50), (250, 250), (350, 150)])

def dibuja_icono(icon_code, texto="Reporte del clima"):
   
    fill_color = obtener_color_relleno(icon_code)
    
    with Image(width=400, height=300, background=Color('lightblue')) as image:
        # Configuración del dibujo
        with Drawing() as draw:
            draw.stroke_color = Color('black')
            draw.stroke_width = 2
            draw.fill_color = fill_color
            
            
            dibujar_figura(draw, icon_code)
            
            
            draw.font = 'fonts/Debrosee-ALPnL.ttf'
            draw.font_size = 42
            draw.fill_color = Color('white')
            draw.text(35, 290,texto)  # Texto dinámico, puedes pasar otro valor aquí
            
            # Aplicar el dibujo sobre la imagen
            draw(image)
        
        # Configuración final de la imagen
        image.format = 'png'
        return image.make_blob()

