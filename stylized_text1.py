#!/usr/bin/env python3

'''
Will Bergen 2019
 - Massively stylize a word such that it may be reasonably used as a 'art'
 - Code is based on pillow examples
'''

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

# Some fonts:
dejavu_sans_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


# Some params:
text = "Friedrich Hayek"
height = 300
width = 500
canvas = (width, height)
center = (width//2, height//2)
font_size = 45
font_width_offset = 13 * len(text)
font_center = (width//2 - font_width_offset, height//2 - font_size)

def set_color(x,y):
    green = (0,255,0,255)
    blue = (0,0,255,255)
    red = (255,0,0,255)
    if (x + y < 250):
        return blue
    elif (x + y > 250 and x + y < 500):
        return green
    else:
        return red


'''

(X,Y)(1,0)(2,0)(3,0)... ..(width-1,0)
(0,1)(1,1)(2,1)(3,1)...
(0,2)(1,2)(2,2)(3,2)...
..
..
..
(0,height-1)...         ..(width-1,height-1)
'''

# Make a new Image:
image = Image.new('RGBA', canvas)
draw = ImageDraw.Draw(image)

# Make the background a ... dark blury colored mess?
pixels = image.load()
print(pixels[100,100]) # successfully gets that pixel in (r,g,b,a) quad

for i in range(width):
    for j in range(height):
        #color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255))
        # pixels[i,j] ...
        pixels[i,j] = set_color(i,j)

image = image.filter(ImageFilter.BoxBlur(1))
# use a truetype font
font = ImageFont.truetype(dejavu_sans_bold, font_size)

draw.text(font_center, text, font=font)

# Display the Image for testing purposes:
image.save("try.png")
