#!/usr/bin/env python3

'''
Will Bergen 2019
 - Massively stylize a word such that it may be reasonably used as a 'art'
 - Code is based on pillow examples
'''

from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageColor
import random

# Some fonts:
dejavu_sans_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


# Some params:
text = "Friedrich Hayek"
height = 1000
width = 1000
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

# Colors:
green = (0,255,0,255)
blue = (0,0,255,255)
red = (255,0,0,255)

color_set1 = ["#e4572e", "#17bebb", "#ffc914", "#2e282a", "#76b041"]
indigos =  [
"#e8eaf6",
"#9fa8da",
"#7986cb",
"#c5cae9",
"#5c6bc0",
"#3f51b5",
"#3949ab",
"#303f9f",
"#283593",
"#1a237e",
"#8c9eff",
"#536dfe",
"#3d5afe",
"#304ffe"]

light_greens = [
"#f1f8e9",
"#dcedc8",
"#c5e1a5",
"#aed581",
"#9ccc65",
"#8bc34a",
"#7cb342",
"#689f38",
"#558b2f",
"#33691e",
"#ccff90",
"#b2ff59",
"#76ff03",
"#64dd17"
]

ambers = [
"#fff8e1",
"#ffecb3",
"#ffe082",
"#ffd54f",
"#ffca28",
"#ffc107",
"#ffb300",
"#ffa000",
"#ff8f00",
"#ff6f00",
"#ffe57f",
"#ffd740",
"#ffc400",
"#ffab00"
]

# Make a new Image:
image = Image.new('RGBA', canvas)
draw = ImageDraw.Draw(image)

def safe_rectangle(xy, fill=None):
    # Newer Pillow requires x1>=x0/y1>=y0; the offsets below can invert that.
    (x0, y0), (x1, y1) = xy
    if x1 < x0:
        x0, x1 = x1, x0
    if y1 < y0:
        y0, y1 = y1, y0
    draw.rectangle([(x0, y0), (x1, y1)], fill)

# Make the background a ... dark blury colored mess?
pixels = image.load()
print(pixels[100,100]) # successfully gets that pixel in (r,g,b,a) quad

# From https://www.reddit.com/r/Python/comments/3xdrgg/i_made_a_few_wallpapers_with_python/
make_deco = 0


# Sigs:
# rectangle([upper_left_corner, lower_right_corner], color)
# pieslice([upper_left_corner, lower_right_corner], start_angle,
# 	end_angle, color)

sqaure_scale = 100
mini_scale = 20
d_iter = 0
directions = [1,2,3,4,3,2]

for i in range(0,width,sqaure_scale):
    for j in range(0,height,sqaure_scale):
        #color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255))
        # pixels[i,j] ...
        # pixels[i,j] = set_color(i,j)
        c1 = random.choice(light_greens[4:])
        c2 = random.choice(ambers[4:])
        draw.rectangle([(i, j), (i+sqaure_scale, j+sqaure_scale)], c1)
        for k in range(1,sqaure_scale, sqaure_scale//8):
	        safe_rectangle([(i+sqaure_scale-k, j+sqaure_scale-k), (i+sqaure_scale-k-mini_scale, j)], c2)
        if make_deco:
	        # orientation = random.choice([1,2,3,4,1,1,3,3])
	        orientation = directions[d_iter % len(directions)]
	        if orientation == 1:
	            draw.pieslice([(i-sqaure_scale-1,j), (i+sqaure_scale-1,j+sqaure_scale*2-1)], 270, 0, c2)
	        elif orientation == 2:
	            draw.pieslice([(i, j), (i+sqaure_scale*2-1, j+sqaure_scale*2-1)], 180, 270, c2)
	        elif orientation == 3:
	            draw.pieslice([(i,j-sqaure_scale-1), (i+sqaure_scale*2-1,j+sqaure_scale-1)], 90, 180, c2)
	        elif orientation == 4:
	            draw.pieslice([(i-sqaure_scale-1,j-sqaure_scale-1), (i+sqaure_scale-1,j+sqaure_scale-1)], 0, 90, c2)
        d_iter += 1

# image = image.filter(ImageFilter.BoxBlur(11))
# use a truetype font
font = ImageFont.truetype(dejavu_sans_bold, font_size)

draw.text(font_center, text, font=font)

# Display the Image for testing purposes:
image.save("try.png")
