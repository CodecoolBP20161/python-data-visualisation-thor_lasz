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
coordinates = []
is_empty = True
for key, val in imported_dict.items():
    font = ImageFont.truetype("fonts/HighlandGothicFLF.ttf", round(math.pow(val[0], 0.2)) * 30)
    text_options = {'fill': val[1], 'font': font}  # szín
    text_content = key  # szöveg
    text_size = draw.textsize(text_content, font=font)
    while True:
        x = randint(1, 699)
        y = randint(1, 699)

        for tuples in coordinates:
            print (tuples, ' ?=', x, y, x + text_size[0], y + text_size[1])
            if (x > tuples[0] and x < tuples[2]) and (y > tuples[1] and y < tuples[3]) or (x + text_size[0] > tuples[0] and x + text_size[0]< tuples[2]) and (y + text_size[1]> tuples[1] and y + text_size[1]< tuples[3]):
                is_empty = False
                break
            else:
                is_empty = True

        if is_empty:

            break




        print (is_empty, '\n\n')
        print (" ")
    draw.text((x, y), text_content, **text_options)
    coordinates.append((x, y, x + text_size[0], y+text_size[1]))
    print (is_empty)
    #y_sizes.append(text_size[1])

img.save('try.png')
img.show()
