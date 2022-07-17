from cmath import pi
from statistics import median
from turtle import shape
from PIL import Image
import math
import numpy as np


#size will be 64x64 but in characters 128 x 64
width_per_character = 6
height_per_character = 12
characters = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,'. ")
characters.reverse()
with Image.open("/Users/kerstinportmacsilber/Downloads/Konfirmations wichtige Bilder/IMG_20200920_143546.jpg") as im:
    image_width, image_height = im.size
    
    
    pixel_per_square = 16
    pixels_per_square = (pixel_per_square ** 2) *2

    result = np.full((int(image_width/pixel_per_square),int(image_height/(2*pixel_per_square))), "", str)
    for XCharacter in range(int(image_width/pixel_per_square)):
        for YCharacter in range(int(image_height/(2*pixel_per_square))):
            sum_of_color = [0,0,0]
            for column in range(pixel_per_square):
                for row in range(pixel_per_square *2):
                    pixel = im.getpixel((column + pixel_per_square * XCharacter, row + pixel_per_square * 2 * YCharacter))
                    sum_of_color[0] += pixel[0]
                    sum_of_color[1] += pixel[1]
                    sum_of_color[2] += pixel[2]
            sum_of_color[0] /= pixels_per_square
            sum_of_color[1] /= pixels_per_square
            sum_of_color[2] /= pixels_per_square
            median_color = int(sum(sum_of_color)/3)
            
            result[XCharacter,YCharacter] = characters[int((median_color/255)**1.5 * (len(characters)-1))]
        print(int(100 * XCharacter/int(image_width/pixel_per_square)), "%")

    for i in range(int(image_width/pixel_per_square)):
        print("".join(result[0:,i]))



    
    
    
