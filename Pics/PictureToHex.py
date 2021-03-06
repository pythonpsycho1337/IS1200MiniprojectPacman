#Written by Thomas Peterson
#This script is used to convert images to hexvalues which later is stored in Data.c (This file is not sent to the mips processor)
import PIL
import sys
from PIL import Image

def imageToHex(im):
    #param im = File path to the target image (String)
    rgb_im = im.convert('RGB')
    width, height = im.size
    w = 0
    while (w < width):
        h = 0
        mySum = 0
        while(h < height):
            r, g, b = rgb_im.getpixel((w, h))
            if (r+g+b > 500):
                mySum += 2**h
            h+=1
        if (w + 1 == width):
            sys.stdout.write(hex(mySum))
        else:
            sys.stdout.write(hex(mySum)+",")
        w += 1

if __name__=="__main__":
    while(True):
        try:
            imageToHex(PIL.Image.open(raw_input("Filename:")))
            print ""
        except:
            print("[*] File not found")
