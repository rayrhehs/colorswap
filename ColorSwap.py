from PIL import Image
# import numpy as np 
import random

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    width, height = image.size
    
    # image size is within bounds 
    if i > width or j > height:
      return None

    pixel = image.getpixel((i, j))
    return pixel

# in order to view results of the function, you must save them in a variable 

image1 = open_image('mdg.png')
# image1.show()

# image details like it's size and format 
print(image1.size)
print(image1.format)
print(image1.mode)

# random generator 
def random_generator(image):
  # get dimensions via .size 
  width, height = image.size 

  # create a new image and make pixel map 
  new_mdg = create_image(width, height)
  pixels = new_mdg.load()

  # pixel list containing pixel IDs
  pixelList = []
  npixelList = []

  # loop 
  for w in range(width):
    for h in range(height): 

      # get pixel information 
      pixel = get_pixel(image, w, h)

      # stores pixel RGB values 
      pixelID = [pixel[0], pixel[1], pixel[2]]

      # if the pixel ID isn't in the list, add it,
      if pixelID not in pixelList: 
        pixelList.append(pixelID)
        # piggy backing off of this 'if statement'
        # every time unique color found = add to list, make seperate list for new color palette 
        npixelList.append([random.randint(0,255), random.randint(0,255), random.randint(0,255)])

      pPos = pixelList.index(pixelID)
      npColor = npixelList[pPos]
      
      # break pixel information into rgb [0 = red, 1 = green, 2 = blue]
      red = npColor[0]
      green = npColor[1]
      blue = npColor[2]

      # rebuilds image using rgb for pixel at position [w, h]
      pixels[w, h] = (int(red), int(green), int(blue))
  
  # print(pixelList)
  # print(npixelList)
  return new_mdg

image2 = random_generator(image1)
image2.show()


# # red generator 
# def red_generator(image):
#   # get dimensions via .size 
#   width, height = image.size 

#   # create a new image and make pixel map 
#   new_mdg = create_image(width, height)
#   pixels = new_mdg.load()

#   # pixel list containing pixel IDs
#   pixelList = []
#   npixelList = []

#   # loop 
#   for w in range(width):
#     for h in range(height): 

#       # get pixel information 
#       pixel = get_pixel(image, w, h)

#       # stores pixel RGB values 
#       pixelID = [pixel[0], pixel[1], pixel[2]]

#       # if the pixel ID isn't in the list, add it,
#       if pixelID not in pixelList: 
#         pixelList.append(pixelID)
#         # piggy backing off of this 'if statement'
#         # every time unique color found = add to list, make seperate list for new color palette 
#         npixelList.append([random.randint(0,255), 0, 0])

#       pPos = pixelList.index(pixelID)
#       npColor = npixelList[pPos]
      
#       # break pixel information into rgb [0 = red, 1 = green, 2 = blue]
#       red = npColor[0]
#       green = npColor[1]
#       blue = npColor[2]

#       # rebuilds image using rgb for pixel at position [w, h]
#       pixels[w, h] = (int(red), int(green), int(blue))
  
#   # print(pixelList)
#   # print(npixelList)
#   return new_mdg

# image3 = red_generator(image1)
# image3.show()


