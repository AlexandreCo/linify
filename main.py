# This is a sample Python script.
from PIL import Image, ImageDraw
import numpy as np
import cv2
import random

def getDarkestPixel(outArray,nb_lines,nb_rows):
    min=255
    darkest_line=0
    darkest_row=0
    for line in range(nb_lines):
        for row in range(nb_rows):
            if(outArray[line, row]<min):
                min=outArray[line, row]
                darkest_line=line
                darkest_row=row

    return darkest_line,darkest_row,min

if __name__ == '__main__':

    img = cv2.imread("Lenna.png",cv2.IMREAD_GRAYSCALE)
    out_array=img.copy()

    nb_lines,nb_raws  = img.shape
    out_array.fill(255)
    while True:
        darkest_line,darkest_row,c=getDarkestPixel(img,nb_lines,nb_raws)
        y=random.randrange(0, nb_lines)
        x=random.randrange(0, nb_raws)
        print(darkest_line,darkest_row,c)
        cv2.line(out_array,(x,y),(darkest_line,darkest_row),
                 int(c))
        img[darkest_line,darkest_row]=255
        #cv2.imshow('image', out_array)
        cv2.imshow('image', img)
        cv2.waitKey(1)


