#crossgen.py
####Imports####

from PIL import Image
import random
import os

####Flavor Text####

print("RANDOM CROSS GENERATOR by Slashscreen.")
print("Initializing...")

####Functions####

def verify_loop(string): #Makes sure string is number
    while True:
        inp = input(string)
        try:
            return int(inp)
        except:
            print("Please input a number.")

def path_verify(): #Makes sure path exists
    while True:
        path = input("What path to save under? (Don't include filename) ==> ")
        if os.path.isdir(path):
            filename = input("What filename? Do not include extention. ==> ")
            return path+"/"+filename+".png"
        else:
            print("Path does not exist. Please input a valid path, without the filename.")

def val_ver(): #Makes sure value either 2 or 3
    while True:
        inp = verify_loop("How many colors? (2 or 3) ==> ")
        if 1 < inp < 4: #if between 2 and 3
            return inp
        else:
            print("Please input a number between 2 and 3.")

def randomval(maxi): #Make random number
    #in own function because i need to call seed each time
    random.seed()
    return random.randrange(maxi)

####Variables####

base = Image.open("3colorcross.png") #loads that greyscale image
basepx = base.load() #Get pixel data
width, height = base.size #gets width and height. not necessary but more readable
cross = Image.new("RGB",base.size) #creates new flag as blank canvas
crosspx = cross.load() #gets pixel gata

cnum = val_ver() #how many colors should it have?

c1 = (randomval(255),randomval(255),randomval(255))  #bg color
c2 = (randomval(255),randomval(255),randomval(255)) #inner cross
if cnum == 3: #only called if 3 colors 
    c3 = (randomval(255),randomval(255),randomval(255)) #inner cross border

print("Generating...")

####Generate new flag####

for x in range(width):
    for y in range(height):
        px = basepx[x,y]
        if px == 255 or (cnum == 2 and px == 136): #bg color. Overrites grey bit if mode is 2
            crosspx[x,y] = c1
        elif px == 0: #inner cross
            crosspx[x,y] = c2
        elif cnum == 3 and px == 136: #inner border - only activates if color is 3
            crosspx[x,y] = c3
        else: #there's a few extra pixels around the border of the grey bit that need to be bg color or border color
            if cnum == 2: #if 2 color, as background
                crosspx[x,y] = c1
            else: #If 3 color, as border
                crosspx[x,y] = c3

####Saving####

cross.show()
cross.save(path_verify())

