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




def draw_line(a,b,c):
    for x in range(0,nb_raws):
        y=int(a*x+b)
        if (x>0) and (y>0) and (x < nb_raws) and (y < nb_lines):
            color=img[x,y] + c
            if(color>255):
                color=255
            img[x,y]=color

            color=out_array[x,y]-(255-c)/2
            if(color<0):
                color=0
            out_array[x,y]=color
    print(f" {c}")


def getMoy(a,b):
    tab=[]

    for x in range(0,nb_raws):
        y=a*x+b
        if (x>0) and (y>0) and (x < nb_raws) and (y < nb_lines):
            color=img[int(x), int(y)]
            tab.append(color)
        else:
            color=0
    n=len(tab)
    if(n):
        color = int(sum(tab) / n)
    else:
        color=0
    return color

def line(x2,y2):
    min=255
    sa=0
    sb=0

    for test in range(0, test_iteration):
        bin=random.randrange(0, 2)
        if(bin):
            x1=0
            y1=random.randrange(0, nb_raws)
        else:
            x1=random.randrange(0, nb_lines)
            y1=0
        if(x2!=x1):
            a = (y2-y1)/(x2-x1)
            b = y1 - (a * x1)
            color=getMoy(a,b)
            if(color<min):
                min=color
                sa=a
                sb=b

    if(color):
        draw_line(sa,sb,min)

if __name__ == '__main__':
    test_iteration=200
    display_every = 10
    img = cv2.imread("Lenna.png",cv2.IMREAD_GRAYSCALE)
    out_array=img.copy()

    nb_lines,nb_raws  = img.shape
    out_array.fill(255)
    i=0
    for i in range(0,3500):
        print(i,end="")

        darkest_line,darkest_row,c=getDarkestPixel(img,nb_lines,nb_raws)
        y=random.randrange(0, nb_lines)
        x=random.randrange(0, nb_raws)
        line(y,x)
        cv2.imshow('image', out_array)
        cv2.waitKey(1)

    cv2.waitKey()


