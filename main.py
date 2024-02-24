import cv2 as cv
from hsp import *
import numpy as np

inputImg = input("Please enter path of filename : ")
image = cv.imread(cv.samples.findFile(inputImg))

blacklow = np.array([0,0,0])
blackup = np.array([50,50,100])

whitelow = np.array([0,0,255])
whiteup = np.array([255,255,255])
outline = cv.inRange(image,blacklow,blackup)
backgroud = cv.inRange(image,whitelow,whiteup)

if image is None:
    print("[ERROR] : Can't read the image!")

inputImg = inputImg[:-3] + "txt"
print(image.shape)
text = ["" for _ in range(image.shape[0])]

for row in range(image.shape[0]):
    for column in range(image.shape[1]):
        if (outline[row,column] == [255,255,255]).any():
            text[row] += "#"
        elif(backgroud[row,column] == [255,255,255]).any():
            text[row] += " "
        elif(isLightOrDark(image[row,column]) == "light"):
            text[row] += "."
        elif(isLightOrDark(image[row,column]) == "dark"):
            text[row] += "~"
        
print(text)

with open(inputImg, 'w') as f:
    for e in text:
        f.write(e)
        f.write("\n")