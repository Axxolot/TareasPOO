from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def dibuja():
    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.stroke_width = 2
        draw.fill_color = Color('white')
        draw.circle((50, 50), (25, 25))
        
        with Image(width=400, height=300, background=Color('lightblue')) as img:
            draw(img)  
            img.format = 'png'  
            png_bin = img.make_blob()
            return png_bin

