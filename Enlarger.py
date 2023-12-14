from PIL import Image
import os

multiplier = int(input('How much do you want to multiply height and width of the image?(2x,3x,4x): '))
choosen_img = str(input('Write the image that you want to resize: '))

if multiplier < 4:
    im = Image.open(f'results\{choosen_img}.png')

    width, height = im.size

    new_width = width*multiplier
    new_height = height*multiplier

    directory = f"{choosen_img}"
    parent_dir = "results/"

    path = os.path.join(parent_dir, directory)
    if os.path.isdir(path) != True:
        os.mkdir(path)
    else:
        resized_image = im.resize((new_width,new_height))
        resized_image.save(f"{path}\{choosen_img}_{str(multiplier)}x.png")
else:
    print('That is too much!')