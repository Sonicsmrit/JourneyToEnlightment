import numpy as np
from PIL import Image as img
from PIL import ImageDraw
from pathlib import Path
import os

def gray():
    with img.open(f"colorfilter/colorfullGirl.jpeg") as girl: ##colorfilter/colorfulGirl.jpeg for testing only

        rgb_val = np.array(girl)
        
        gray_scale = 0.299*rgb_val[:,:,0] + 0.587*rgb_val[:,:,1] + 0.114*rgb_val[:,:,2]
        gray_scale = gray_scale.astype(np.uint8)
        
        
        gray_image = img.fromarray(gray_scale, "L")
        
        gray_image.show()

        ask = input("Do you want to save the image(Y/N): ").strip().upper()
        if ask == "Y":
            asl_name = input("enter name of the file: ")
            gray_image.save(f"{asl_name}.jpeg")
            return
        elif ask == "N":
            return
        else:
            return


def sepia():
    with img.open(f"colorfilter/colorfullGirl.jpeg") as girl:
        rgb_val = np.array(girl)

        Red = rgb_val[:,:,0] * 0.393 + rgb_val[:,:,1] * 0.769 + rgb_val[:,:,2] * 0.189
        Blue = rgb_val[:,:,0] * 0.272 + rgb_val[:,:,1] * 0.534 + rgb_val[:,:,2] * 0.131
        Green = rgb_val[:,:,0] * 0.349 + rgb_val[:,:,1] * 0.686 + rgb_val[:,:,2] * 0.168

        Red = np.clip(Red, 0, 255)
        Blue = np.clip(Blue, 0, 255)
        Green = np.clip(Green, 0, 255)

        Red = (Red.astype(np.uint8))
        Blue = (Blue.astype(np.uint8))
        Green = (Green.astype(np.uint8))

        combined = np.dstack((Red, Green, Blue))
        sepia_bb = img.fromarray(combined, "RGB")
        sepia_bb.show()

        ask = input("Do you want to save the image(Y/N): ").strip().upper()
        if ask == "Y":
            asl_name = input("enter name of the file: ")
            sepia_bb.save(f"{asl_name}.jpeg")
            return
        elif ask == "N":
            return
        else:
            return

        

def bright(a):
    with img.open(f"colorfilter/colorfullGirl.jpeg") as girl:
        rgb_val = np.array(girl)
        # inc = (rgb_val[:,:,0] * a) + (rgb_val[:,:,1] * a) + (rgb_val[:,:,2] * a)
        inc = rgb_val * a
        inc = np.clip(inc,0 ,255).astype(np.uint8)
        
        bright_img = img.fromarray(inc, "RGB")

        bright_img.show()

        ask = input("Do you want to save the image(Y/N): ").strip().upper()
        if ask == "Y":
            asl_name = input("enter name of the file: ")
            bright_img.save(f"{asl_name}.jpeg")
            return
        elif ask == "N":
            return
        else:
            return


def contrash(perc):
    with img.open(f"colorfilter/colorfullGirl.jpeg") as girl:
        val_arr = np.array(girl)
        cont_inc = perc * (val_arr.astype(np.float32) - 128) + 128
        cont_inc = np.clip(cont_inc, 0, 255).astype(np.uint8)

        pic = img.fromarray(cont_inc, "RGB")
        pic.show()

        ask = input("Do you want to save the image(Y/N): ").strip().upper()
        if ask == "Y":
            asl_name = input("enter name of the file: ")
            pic.save(f"{asl_name}.jpeg")
            return
        elif ask == "N":
            return
        else:
            return








##starting
# getPathval = (input("Enter the complete file path of your image: "))
# clean_path = getPathval.strip()

while True:
    while True:
        try:
            ask_qa = int(input("Enter the filter you want to put on\n (1) for Gray Scale\n (2) for Sepia tone effect\n (3) for Brightness adjestment\n(4) for contrast enhancement:"))
            break
        except:
            print("enter the number only!")
            continue


    # with img.open(f"{clean_path}") as beauty:

    if ask_qa == 1:
        gray()

    elif ask_qa == 2:
        sepia()
    elif ask_qa ==3:
        while True:
            try:
                val = int(input("Enter the percentage brightness you want: "))
                
                
                break
            except:
                print("enter a percent value without the percent sign")
                continue
        percent = 1 + (val/100)
        bright(percent)
    elif ask_qa == 4:
        while True:
            try:
                val = int(input("Enter the percentage contrass you want: "))
                
                
                break
            except:
                print("enter a percent value without the percent sign")
                continue
        percent = 1 + (val/100)
        contrash(percent)
    
    question = input("Do you want to do it again?(Y/N) ").strip().upper()

    if question == "Y":
        continue
    elif question == "N":
        break
    else:
        continue



