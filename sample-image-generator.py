from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import math
import main

imported_dict = main.clients_name()
img = Image.new("RGB", (520, 520), "black")
draw = ImageDraw.Draw(img)
index = 1
for key, val in imported_dict.items():

    print (val)
    font = ImageFont.truetype("fonts/riesling.ttf", round(math.pow(val[0],0.2))*30)
    text_options = {'fill': val[1], 'font': font}               #szín
    text_content = key                            #szöveg
    text_size = draw.textsize(text_content, font=font)
    print (text_size)
    draw.text((206, index), text_content, **text_options)
    index += (text_size[1])
    img = img.rotate(17.5, expand=1)
img.save('try.png')
img.show()
