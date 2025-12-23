
from PIL import Image as img
import os
from pathlib import Path

print("Welcome to Image Processing")
while True:
    ask_path = input("Enter the path to your folder: ")
    while True:
        try:
            ask_height = int(input("enter the size of the image: "))
            ask_width = int(input("enter the width of the image: "))
            break
        except:
            print("only type numbers")
            continue

    new_size = (ask_width, ask_height)
    path_clean = Path(ask_path.strip())



    inp = []
    for x in os.listdir(ask_path):
        if x.endswith(".jpg") or x.endswith(".png"):
            inp.append(f"{path_clean}\{x}")


    for imag in inp:
        with img.open(imag) as pic:
            rezised_pic = pic.resize(new_size)

            save_folder = Path("processed")
            filename = Path(imag).stem

            save_path = save_folder / f"{filename}_reshaped.jpg"
            rezised_pic.save(save_path)
    a = input("continue?(Y/N)").lower()
    if a == "n":
        break
    else:
        continue