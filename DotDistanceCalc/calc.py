import math
from PIL import ImageDraw, Image



print("Welcome to the Dot distance Calculator")

while True:
    print("enter the point 1")

    #for first points in the axis
    while True:
        try:
            x1 = int(input("Enter X1: "))
            y1 = int(input("Enter Y1: "))
            break
        except:
            print("please enter numbers only")
            continue

    while True:
        try:
            x2 = int(input("Enter X2: "))
            y2 = int(input("Enter Y2: "))
            break
        except:
            print("Please enter numbers only")
            continue

    #calculations

    #distance between two points
    dis_btw = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    calc_dis = round(dis_btw,2)

    #midterm

    mid = ((x1+x2)/2, (y1+y2)/2)

    #angle in degrees

    ang_dig = math.degrees(math.atan2(y2-y1, x2-x1))

    calc_angTan = round(ang_dig,2)


    #results

    print(f"The midpoint of the points is: {mid}")

    print(f"The distance between the two points is: {calc_dis}")

    print(f"The angle of the point from the center (0,0) is: {calc_angTan}")



    with Image.open("DotDistanceCalc/graph.png") as pic:
        draw = ImageDraw.Draw(pic)

        draw.line(((x1,y1),(x2,y2)),fill='green', width=5)
        draw.text((x1,y1),f"{(x1,y1)}",fill='white',size=80)
        draw.text((x2,y2),f"{(x2,y2)}",fill='white',size=80)
        draw.line((mid,mid),fill='red',width=100)
        draw.text((mid), f"{mid}",fill='red',size=80)


        pic.show()
    
    ask = input("Do you want to calc again?(Y/N): ").strip().upper()

    if ask == "Y":
        continue
    elif ask == "N":
        break
    else:
        continue
