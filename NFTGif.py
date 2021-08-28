import random

from PIL import Image, ImageFont, ImageDraw

#initialize variables and the random number generator
random.seed(version=2)
RGB_ColorR = 0
RGB_ColorG = 0
RGB_ColorB = 0
Num_Shape_X = 0
x = 0
y = 0
z = 0
Secret_Text_List = ["I wonder what I need to do now?", "chocolate", "I need to get stronger", "we were to young back then, we didn't know", "A", "I wish things were different", "Hi waht's up", "california", "blue", "black", "red", "Anime", "we", "He", "she", "it's in the past now", "Broken bonds", "The red string of fate keeps bringing us together", "maybe", "where", "Let's pray"]
Rand_Word = 0
#create a function that gets random integers for colors evverytime its called
def random_num_gen():
    global RGB_ColorR
    global RGB_ColorG
    global RGB_ColorB
    global Num_Shape_X
    global x
    global y
    global z
    global Rand_Word

    RGB_ColorR = random.randint(0,255)
    RGB_ColorG = random.randint(0,255)
    RGB_ColorB = random.randint(0,255)
    Num_Shape_X = random.randint(1, 25)
    Rand_Word = random.randint(0, len(Secret_Text_List)-1)
    x = random.randint(11, 2000)
    y = random.randint(11, 2000)
    z = random.randint(11, 2000)


#call random_num_gen() to assign random RGB number
random_num_gen()

#Generate a new image with a black background color
image = Image.new('RGB', (1800,1800))

#create a drawable image to draw on top of the image
draw = ImageDraw.Draw(image, 'RGBA')

#fnt = ImageFont.load_default(size=25)
fnt = ImageFont.truetype("System/Library/Fonts/Arial Unicode.ttf", size=25, layout_engine=ImageFont.LAYOUT_RAQM)

#function for converting string to ninary
def String_To_Bin(w = ''):
    return [bin(ord(x))[2:].zfill(8) for x in w]

#function for drawing random circles with random colors
def draw_words():
    global draw
    global x
    global y
    global z
    global Num_Shape_X
    global Rand_Word
    global Secret_Text_List
    global fnt
    for i in range(Num_Shape_X):
        random_num_gen()
        Word = Secret_Text_List[Rand_Word]
        Bin_Word = str(String_To_Bin(Word))
        print(Word)
        print(Bin_Word)
        draw.text((x,y), Word, font=fnt, direction="ttb", fill=(RGB_ColorR, RGB_ColorG, RGB_ColorB))
        #x = x+10
        #y = y-10
        #draw.text((x,y), Bin_Word, font=fnt, direction="ttb", fill=(RGB_ColorR, RGB_ColorG, RGB_ColorB))





#draw the first image by calling the draw_circle function and save it
draw_words()
image.save('Matrix.png')
image.show()

draw = ImageDraw.Draw(image, 'RGBA')
draw_words()
image.save('Matrix2.png')
image.show()

draw = ImageDraw.Draw(image, 'RGBA')
draw_words()
image.save('Matrix3.png')
image.show()

draw = ImageDraw.Draw(image, 'RGBA')
draw_words()
image.save('Matrix4.png')
image.show()


#alpha-blend the images together
#result = Image.blend(image, image2, alpha=.5)
#result.save('result.jpg')

#display the images
#result.show()
