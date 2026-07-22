#!/usr/bin/env python3

'''
Will Bergen 2019
 - Make some kind of vaguely dynamic background for some text -> png
 - Code is based on pillow examples, and where marked other web sources
'''

from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageColor
import random

import scipy
import numpy as np

# Some fonts:
dejavu_sans_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


# Some params:
text = "Friedrich Hayek"
height = 800
width = 1200
canvas = (width, height)
center = (width//2, height//2)
font_size = 120
font = ImageFont.truetype(dejavu_sans_bold, font_size) # use a truetype font


# Colors sets derived from https://www.materialpalette.com/colors
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

light_blues = [
"#e1f5fe",
"#b3e5fc",
"#81d4fa",
"#4fc3f7",
"#29b6f6",
"#03a9f4",
"#039be5",
"#0288d1",
"#0277bd",
"#01579b",
"#80d8ff",
"#00b0ff",
"#0091ea",
"#40c4ff"
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

reds = [
"#ffebee",
"#ffcdd2",
"#ef9a9a",
"#e57373",
"#ef5350",
"#f44336",
"#e53935",
"#d32f2f",
"#c62828",
"#b71c1c",
"#ff8a80",
"#ff5252",
"#ff1744",
"#d50000"
]

pinks = [
"#fce4ec",
"#f8bbd0",
"#f48fb1",
"#f06292",
"#ec407a",
"#e91e63",
"#d81b60",
"#c2185b",
"#ad1457",
"#880e4f",
"#ff80ab",
"#ff4081",
"#f50057",
"#c51162"
]

purples = [
"#f3e5f5",
"#e1bee7",
"#ce93d8",
"#ba68c8",
"#ab47bc",
"#9c27b0",
"#8e24aa",
"#7b1fa2",
"#6a1b9a",
"#4a148c",
"#ea80fc",
"#e040fb",
"#d500f9",
"#aa00ff"
]

deep_purples = [
"#ede7f6",
"#d1c4e9",
"#b39ddb",
"#9575cd",
"#7e57c2",
"#673ab7",
"#5e35b1",
"#512da8",
"#4527a0",
"#311b92",
"#b388ff",
"#7c4dff",
"#651fff",
"#6200ea"
]

blues = [
"#e3f2fd",
"#bbdefb",
"#90caf9",
"#64b5f6",
"#42a5f5",
"#2196f3",
"#1e88e5",
"#1976d2",
"#1565c0",
"#0d47a1",
"#82b1ff",
"#448aff",
"#2979ff",
"#2962ff"
]

cyans = [
"#e0f7fa",
"#b2ebf2",
"#80deea",
"#4dd0e1",
"#26c6da",
"#00bcd4",
"#00acc1",
"#0097a7",
"#00838f",
"#006064",
"#84ffff",
"#18ffff",
"#00e5ff",
"#00b8d4"
]

teals = [
"#e0f2f1",
"#b2dfdb",
"#80cbc4",
"#4db6ac",
"#26a69a",
"#009688",
"#00897b",
"#00796b",
"#00695c",
"#004d40",
"#a7ffeb",
"#64ffda",
"#1de9b6",
"#00bfa5"
]

greens = [
"#e8f5e9",
"#c8e6c9",
"#a5d6a7",
"#81c784",
"#66bb6a",
"#4caf50",
"#43a047",
"#388e3c",
"#2e7d32",
"#1b5e20",
"#b9f6ca",
"#69f0ae",
"#00e676",
"#00c853"
]

limes = [
"#f9fbe7",
"#f0f4c3",
"#e6ee9c",
"#dce775",
"#d4e157",
"#cddc39",
"#c0ca33",
"#afb42b",
"#9e9d24",
"#827717",
"#f4ff81",
"#eeff41",
"#c6ff00",
"#aeea00"
]

yellows = [
"#fffde7",
"#fff9c4",
"#fff59d",
"#fff176",
"#ffee58",
"#ffeb3b",
"#fdd835",
"#fbc02d",
"#f9a825",
"#f57f17",
"#ffff8d",
"#ffff00",
"#ffea00",
"#ffd600"
]

oranges = [
"#fff3e0",
"#ffe0b2",
"#ffcc80",
"#ffb74d",
"#ffa726",
"#ff9800",
"#fb8c00",
"#f57c00",
"#ef6c00",
"#e65100",
"#ffd180",
"#ffab40",
"#ff9100",
"#ff6d00"
]

deep_oranges = [
"#fbe9e7",
"#ffccbc",
"#ffab91",
"#ff8a65",
"#ff7043",
"#ff5722",
"#f4511e",
"#e64a19",
"#d84315",
"#bf360c",
"#ff9e80",
"#ff6e40",
"#ff3d00",
"#dd2c00"
]

browns = [
"#efebe9",
"#d7ccc8",
"#bcaaa4",
"#a1887f",
"#8d6e63",
"#795548",
"#6d4c41",
"#5d4037",
"#4e342e",
"#3e2723"
]

greys = [
"#fafafa",
"#f5f5f5",
"#eeeeee",
"#e0e0e0",
"#bdbdbd",
"#9e9e9e",
"#757575",
"#616161",
"#424242",
"#212121"
]

blue_greys = [
"#eceff1",
"#cfd8dc",
"#b0bec5",
"#90a4ae",
"#78909c",
"#607d8b",
"#546e7a",
"#455a64",
"#37474f",
"#263238"
]

palettes = [indigos, light_greens, light_blues, ambers, reds, pinks, purples, deep_purples,
blues, cyans, teals, greens, limes, yellows, oranges, deep_oranges, browns, greys, blue_greys]

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

t_bbox = draw.textbbox((0, 0), text, font=font)
t_w, t_h = t_bbox[2] - t_bbox[0], t_bbox[3] - t_bbox[1]
font_center = ((width-t_w)//2, (height - t_h)//2)

# Get the pixels:
pixels = image.load()
# print(pixels[100,100]) # successfully gets that pixel in (r,g,b,a) quad



# Sigs:
# rectangle([upper_left_corner, lower_right_corner], color)
# pieslice([upper_left_corner, lower_right_corner], start_angle,
# 	end_angle, color)

sqaure_scale = 100
mini_scale = 20

palette1 = random.choice(palettes)
palette2 = random.choice(palettes)

directions = [1,2,3,4]

# Draw some squares with deco littler squares...
for i in range(0,width//2,sqaure_scale):
	for j in range(0,height,sqaure_scale):
		c1 = random.choice(palette1[:4])
		c2 = random.choice(palette2[1:])
		draw.rectangle([(i, j), (i+sqaure_scale, j+sqaure_scale)], c1)
		for k in range(1,sqaure_scale, sqaure_scale//10):
			# x0_y0 = (i+sqaure_scale-k, j+sqaure_scale-k)
			# x1_y1 = ((i+sqaure_scale-k-mini_scale, j))
			d = random.choice(directions)
			print(d)
			c2 = random.choice(palette2[:4])
			# good one:
			# draw.rectangle([(i+sqaure_scale-k, j+sqaure_scale-k), (i+sqaure_scale-k-mini_scale, j)], c2) # [\]
			if d == 1:
				safe_rectangle([(i+sqaure_scale-k, j+sqaure_scale-k), (i+sqaure_scale+k-mini_scale, j)], c2) # [\]
			elif d == 2:
				safe_rectangle([(i+sqaure_scale-k, j+sqaure_scale-k), (i+sqaure_scale-k-mini_scale, j)], c2) # [\]
			elif d == 3:
				safe_rectangle([(i+sqaure_scale+k, j+sqaure_scale+k), (i+sqaure_scale+k-mini_scale, j)], c2) # [\]
			elif d == 4:
				safe_rectangle([(i+sqaure_scale+k, j+sqaure_scale-k), (i+sqaure_scale-k-mini_scale, j)], c2) # [\]
# Mirror the above:
for i in range(0, width//2):
	for j in range(0,height):
		pixels[i+width//2,j] = pixels[width//2-i,j]


# Draw the underneath Circle:
# num_circles = 50
# coef = 100
# h_coef = 90 # move them down a bit
# for i in range(num_circles, 1,-1):
# 	c1 = random.choice(palette1)
	# draw.pieslice([0+width/i+coef, 0+height/i+coef + h_coef, width-width/i-coef, height-height/i-coef], 0, 180, c1)




# This prevents the text drawing...
# image = image.filter(ImageFilter.BoxBlur(11))

# Stroke the text by drawing it offeset in all directions:
shadowcolor = "black"
stroke_size = 4
draw.text((font_center[0]-stroke_size, font_center[1]-stroke_size), text, font=font, fill=shadowcolor)
draw.text((font_center[0]+stroke_size, font_center[1]-stroke_size), text, font=font, fill=shadowcolor)
draw.text((font_center[0]-stroke_size, font_center[1]+stroke_size), text, font=font, fill=shadowcolor)
draw.text((font_center[0]+stroke_size, font_center[1]+stroke_size), text, font=font, fill=shadowcolor)

draw.text(font_center, text, font=font)

# Resize to antialias:
image = image.resize((width//2, height//2), Image.Resampling.LANCZOS)

# Save the image:
image.save("try.png")
