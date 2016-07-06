from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import math
import main

imported_dict = main.clients_name()
img = Image.new("RGB", (700, 700), "black")
draw = ImageDraw.Draw(img)
x = 1
y = 1
y_sizes = []
for key, val in imported_dict.items():


    font = ImageFont.truetype("fonts/riesling.ttf", round(math.pow(val[0],0.2))*30)
    text_options = {'fill': val[1], 'font': font}               #szín
    text_content = key                            #szöveg
    text_size = draw.textsize(text_content, font=font)

    if text_size[0] > 700 - x:
        y += max(y_sizes)
        x = 1
        y_sizes = []

    draw.text((x, y), text_content, **text_options)

    x += (text_size [0] + 10)
    y_sizes.append(text_size[1])

img.save('try.png')
img.show()
