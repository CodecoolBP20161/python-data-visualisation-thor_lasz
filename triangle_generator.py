from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import math
from datamanager import DataManager
from random import randint

datamanager = DataManager()
imported_dict = datamanager.clients_name()
img = Image.new("RGB", (1000, 1000), "black")
draw = ImageDraw.Draw(img)
x = 380
y = 100
y_sizes = []
counter = 20
counter2 = 20
iterator = 0
# for i in range(int(len(imported_dict)/2)):
for key, val in imported_dict.items():


    font = ImageFont.truetype("fonts/HighlandGothicFLF.ttf", round(math.pow(val[0],0.2))*15)
    text_options = {'fill': val[1], 'font': font}               #szín
    text_content = key                            #szöveg
    text_size = draw.textsize(text_content, font=font)

    if iterator < len(imported_dict)/2:
        if text_size[0] > 500 -x:
            y += max(y_sizes)
            x = 500 - 8*counter
            y_sizes = []

        draw.text((x, y), text_content, **text_options)

        x += (text_size [0] + 10)
        y_sizes.append(text_size[1])
        x2 = img.getbbox()[2]
        y2 = img.getbbox()[3]
        print (x2, y2)
        counter += 1
    else:
        if text_size[0] > 500 + 8*counter2 -x2:
            y2 += max(y_sizes)
            x2 = 500
            y2_sizes = []

        draw.text((x2, y2), text_content, **text_options)

        x2 += (text_size[0] + 10)
        y_sizes.append(text_size[1])
        counter2 += 1
    iterator += 1
#img = img.rotate(24)
img.save('try.png')
img.show()
