import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import shutil

import json
import os
import sys
import pprint
import argparse
from PIL import Image
from PIL import ImageTk
from PIL import ImageTk, Image  


pp = pprint.PrettyPrinter()





import random
list_img_dir = os.listdir("DO_NOT_TOUCH")
putin_image = random.choice(list_img_dir)

root = Tk()
root.title("Convert images to WebP")
root.geometry("400x250")
root.configure(bg='black')

def crawlDirectories(inputPath):
    global list_img_dir
    putin_image = random.choice(list_img_dir)
    img = Image.open("DO_NOT_TOUCH/" + putin_image)
    bg = ImageTk.PhotoImage(img)
    label.configure(image=bg)
    label.image = bg
    for dirpath, dirnames, files in os.walk(inputPath):
        pp.pprint(f'Found directory: {dirpath}')
        for file_name in files:
            file, ext = os.path.splitext(dirpath + os.sep + file_name)
            pp.pprint(ext)
            if ext in [".png", ".jpg", ".jpeg"]:
                convertImage(dirpath + os.sep + file_name)
    print(inputPath)


def convertImage(infile):
    file, ext = os.path.splitext(infile)
    pp.pprint(file)
    im = Image.open(infile).convert("RGB")
    im.save(file + ".webp", "WEBP", quality=70)
    os.remove(infile)

img =Image.open("DO_NOT_TOUCH/" + putin_image)
bg = ImageTk.PhotoImage(img)

# Add image
label = Label(root, image=bg)
label.place(x = 0,y = 0)

def callback(*args):
    print(e.get())


# drop Down boxes
# https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter


"""main_title_lebel = Label(text="Convert Images to WebP", bg="black", fg="white")
main_title_lebel.pack()
"""


"""PDF_name_lebel = Label(text="Add Folder Path to convert Images:  ", bg="black", fg="yellow")
PDF_name_lebel.pack()

PDFtitle = tk.Text(root,
                   height=1,
                   width=20,
                   )

PDFtitle.pack()"""

"""merge_button_lebel = Label(text="Convert NOW:  ", bg="black", fg="yellow")
merge_button_lebel.pack()"""

merge_button = tk.Button(root, text='PRESS TO CONVERT', command=lambda:crawlDirectories("images_to_convert"))
merge_button.pack()

root.mainloop()
