import os

from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    os.getcwd()
    image_source.save(os.getcwd()+"\\out\\" + name.replace('\n',' ') +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":
    f=open('names.txt',"r")
    names = f.readlines()
    make_certificates('SaRan')
    # for name in names:
    #     print(name)
    #     make_certificates(name.strip())

    print(len(names), "certificates done.")

