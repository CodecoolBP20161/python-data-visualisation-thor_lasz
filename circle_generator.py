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
x = 450
y = 25
y_sizes = []
counter = 2
mask = []
if len(imported_dict) %2 == 1:
    mask = [0]

for i in range(int((len(imported_dict)/2))):
    mask.append(i+20)
for i in range(int((len(imported_dict)/2))):
    mask.append(mask[-1]-1)

print (mask)
counter = 0
print (len(mask))
print (len(imported_dict))
for key, val in imported_dict.items():


    font = ImageFont.truetype("fonts/HighlandGothicFLF.ttf", round(math.pow(val[0],0.2))*25)
    text_options = {'fill': val[1], 'font': font}               #szín
    text_content = key                            #szöveg
    text_size = draw.textsize(text_content, font=font)

    if text_size[0] > 500 + 8*mask[counter]- x:
        y += max(y_sizes)
        x = 500 - 8*mask[counter]
        y_sizes = []

    draw.text((x, y), text_content, **text_options)

    x += (text_size [0] + 10)
    y_sizes.append(text_size[1])
    counter += 1
img = img.rotate(24)
img.save('try.png')
img.show()
