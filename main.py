import cv2 as cv
from hsp import *
import numpy as np
import tkinter as tk
from tkinter import filedialog
import sys

textEnd = ""
inputImg = ""

def copy():
    global textEnd
    frame.clipboard_clear()
    frame.clipboard_append(textEnd)

def browsingInterface():
    filename = filedialog.askopenfilename(
    filetypes=(
        ("JPG", "*.jpg"),
        ("PNG", ("*.png", "*.PNG")),
        ("All Files", "*.*")
    ),initialdir="C:/"
)   
    global inputImg
    inputImg = filename
    selectedFile.config(text=f"Selected File : {inputImg}")


def convertToAscii():
    global inputImg
    global textEnd

    image = cv.imread(cv.samples.findFile(inputImg))
    blacklow = np.array([0,0,0])
    blackup = np.array([50,50,100])
    whitelow = np.array([0,0,100])
    whiteup = np.array([255,255,255])
    outline = cv.inRange(image,blacklow,blackup)
    background = cv.inRange(image,whitelow,whiteup)

    if image is None:
        print("[ERROR] : Can't read the image!")
    while image.shape[1] > 450:
        image = cv.resize(image, (image.shape[1]//2,image.shape[0]//2), interpolation = cv.INTER_AREA)

    outline = cv.inRange(image,blacklow,blackup)
    background = cv.inRange(image,whitelow,whiteup)

    inputImg = inputImg[:-3] + "txt"
    print(image.shape)
    text = ["" for _ in range(image.shape[0])]

    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            darkness = isLightOrDark(image[row,column])
            if (outline[row,column] == [255,255,255]).any():
                text[row] += "@@"
            elif(background[row,column] == [255,255,255]).any():
                text[row] += "  "
            elif darkness  == "mid":
                text[row] += "=="
            elif darkness  == "light":
                text[row] += "--"
            elif darkness == "dark":
                text[row] += "++"

    with open(inputImg, 'w') as f:
        for e in text:
            textEnd += f"{e}\n"
            f.write(e)
            f.write("\n")

    confirmation.config(text="Conversion complete!")

frame = tk.Tk()
frame.geometry("600x200")
frame.title("Converter Image to Ascii")
frame.resizable(False,False)

browse = tk.Button(frame,text="Browse",command=browsingInterface)
browse.grid(row=0,column=0)

selectedFile = tk.Label(frame, text="")
selectedFile.grid(row=0,column=1)

convert = tk.Button(frame,text="Convert",command=convertToAscii)
convert.grid(row=1,column=0)

confirmation = tk.Label(frame, text="",fg="green")
confirmation.grid(row=1,column=1)

copy = tk.Button(frame,text="Copy",command=copy)
copy.grid(row=2,column=1)


if __name__ == "__main__":
    frame.mainloop()