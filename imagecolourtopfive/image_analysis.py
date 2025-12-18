from PIL import Image, ImageDraw
from collections import Counter


with Image.open("imagecolourtopfive/CoolGirl.jpeg") as girl:
    
    # girl.show()

    width, height = girl.size

    girls_pixl = []
    for hi in range(height):
        for wid in range(width):
            pixl = girl.getpixel((wid,hi))
            girls_pixl.append(pixl)
    


    simplified_values = []


    for x in girls_pixl:
        values = (int(x[0])//10)*10, (int(x[1])//10)*10, (int(x[2])//10)*10
        simplified_values.append(values)
        

    total_of_all = dict(Counter(simplified_values))

    # print(total_of_all)

    top_5 = sorted(total_of_all.items(), key=lambda item: item[1], reverse=True)[:5]
    # print(top_5)

    colours = []
    for values_rgb in top_5:
        colours.append(values_rgb[0])

    draw = ImageDraw.Draw(girl)

    rect_width = width * 0.4
    rect_height = 40
    margin = 20
    padding = 10

    for i, colour in enumerate(colours):

        x0 = margin
        y0 = margin + i * (rect_height + padding)

        x1 = x0 + rect_width
        y1 = y0 + rect_height

        if y0 > height:
            break

        draw.rectangle([x0, y0, x1, y1], fill=colour)

    girl.show()



    # print(colours)

    





    # print(simplified_values)

    ##too slow for my pc

    # for count_total_number in simplified_values:
    #     total_count = simplified_values.count(count_total_number)

    # print(total_count)





