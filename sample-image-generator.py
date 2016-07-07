from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import math
import main
from random import randint

imported_dict = main.clients_name()
img = Image.new("RGB", (700, 700), "black")
draw = ImageDraw.Draw(img)
counter = 0


for key, val in imported_dict.items():
    x = randint(1, 699)
    y = randint(1, 699)
    font = ImageFont.truetype("fonts/HighlandGothicFLF.ttf", round(math.pow(val[0], 0.2)) * 30)
    text_options = {'fill': val[1], 'font': font}  # szín
    text_content = key  # szöveg
    text_size = draw.textsize(text_content, font=font)
    print ("waccap")


    while counter < 10:

        draw.text((x, y), text_content, **text_options)


    if text_size[0] > 700 - x:
        y += max(y_sizes)
        x = 1
        y_sizes = []

    draw.text((x, y), text_content, **text_options)

    x += (text_size [0] + 10)
    y_sizes.append(text_size[1])

img.save('try.png')
img.show()
