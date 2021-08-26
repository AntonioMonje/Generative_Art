import random

from PIL import Image, ImageDraw

#initialize variables and the random number generator
random.seed(version=2)
RGB_ColorR = 0
RGB_ColorG = 0
RGB_ColorB = 0
Num_Shape_Circle = 0
Num_Shape_x = 0
Num_Shape_y = 0
Num_Shape_z = 0
r = 0
x = 0
y = 0
pic_name = 'cool'
pic_name2 = 'cool2'

#create a function that gets random integers for colors evverytime its called
def random_num_gen():
    global RGB_ColorR
    global RGB_ColorG
    global RGB_ColorB
    global Num_Shape_x
    global Num_Shape_y
    global Num_Shape_z
    global r
    global x
    global y


    RGB_ColorR = random.randint(0,255)
    RGB_ColorG = random.randint(0,255)
    RGB_ColorB = random.randint(0,255)
    Num_Shape_x = random.randint(1, 400)
    Num_Shape_y = random.randint(1, 200)
    Num_Shape_z = random.randint(1, 200)
    r = random.randint(10, 500)
    x = random.randint(11, 2000)
    y = random.randint(11, 2000)


#call random_num_gen() to assign random RGB number
random_num_gen()

#Generate a new image with a random background color
image = Image.new('RGB', (1800,1800), (RGB_ColorR, RGB_ColorG, RGB_ColorB))

#create a drawable image to draw on top of the image
draw = ImageDraw.Draw(image, 'RGBA')

#function for drawing random circles with random colors
def draw_circle():
    global draw
    global x
    global y
    global r
    global Num_Shape_x

    for i in range(Num_Shape_x):
        random_num_gen()
        draw.ellipse((x-r, y-r, x+r, y+r),outline=(RGB_ColorR, RGB_ColorG, RGB_ColorB))
        x = x*random.randint(1,10)
        y = y*random.randint(1,10)
        r = r*random.randint(1,10)
        draw.ellipse((x-r, y-r, x+r, y+r),outline=(RGB_ColorR, RGB_ColorG, RGB_ColorB))



#call random_num_gen() to assign random RGB number
random_num_gen()


#Generate a new image with a random background color
image2 = Image.new('RGB', (1800,1800), (RGB_ColorR, RGB_ColorG, RGB_ColorB))

#create a drawable image to draw on top of the image
draw2 = ImageDraw.Draw(image2, 'RGBA')

#function for drawing random polygons with random colors
def draw_poly():
    global draw2
    global x
    global y
    global r
    global Num_Shape_y

    for i in range(Num_Shape_y):
        random_num_gen()
        draw2.polygon(((x+r,y+r),(x+y,y-x),(x+y,y-x-50)), fill=(RGB_ColorR, RGB_ColorG, RGB_ColorB))

#draw the first image by calling the draw_circle function and save it
draw_circle()
image.save('cool.jpg')

#draw the first image by calling the draw_poly function and save it
draw_poly()
image2.save('cool2.jpg')

#alpha-blend the images together
result = Image.blend(image, image2, alpha=.5)


#display the images
image.show()
image2.show()
result.show()
