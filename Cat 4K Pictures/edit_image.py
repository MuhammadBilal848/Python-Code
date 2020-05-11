from PIL import Image
#  PIL(pillow) is package name and Image is a module in it 

# To load an image from a file, use the open() function in the Image module:
img1 = Image.open("Cat.jpg","r") # image object get stored in img1 variable

# to display the picture on screen , we can use show() function from Image module
# img1.show()

# now how can we change the picture's extension to png,jpg,pdf and gif etc 
# for this we can use save method by changing the extension of any object or file name, 
# e.g here img1 has picture that has jpg ext, but we can change the extension to png and save that image
img1.save("Catty.png")

# now how to resize or change the size of image, for this we use thumbnail method
img1.thumbnail((250,250))
img1.save("catty.pdf")

# now to increase the sharpness,brighness,contrast and color or image we have to import ImageEnhance 
from PIL import ImageEnhance

# ________ Sharpness ________

img2 = Image.open("Cat 3.jpg","r")
# syntax - ImageEnhance.Sharpness(image)
enhace_pic = ImageEnhance.Sharpness(img2) # this is my sharpness object  
# now by using enahnce method i can enhance the picture
enhace_pic.enhance(2).save("cattoS.png")
# this takes 1 argument as factor 
# An enhancement factor of 0.0 gives a blurred image, a factor of 1.0 gives the original image, 
# and a factor of 2.0 gives a sharpened image.

# ________ Color ________

img2 = Image.open("Cat 4.jpg","r")
# syntax - ImageEnhance.Color(image)
enhace_pic = ImageEnhance.Color(img2) # this is my Color object  
# now by using enahnce method i can enhance the picture
enhace_pic.enhance(2).save("catto1C.png")
# this takes 1 argument as factor 
# An enhancement factor of 0.0 gives a black and white image. A factor of 1.0 gives the original image.

# ________ Brightness ________

img2 = Image.open("Cat 4.jpg","r")
# syntax - ImageEnhance.Brightness(image)
enhace_pic = ImageEnhance.Brightness(img2) # this is my sharpness object  
# now by using enahnce method i can enhance the picture
enhace_pic.enhance(5).save("catto2B.png")
# An enhancement factor of 0.0 gives a black image. A factor of 1.0 gives the original image.

# ________ Contrast ________

img2 = Image.open("Cat 4.jpg","r")
# syntax - ImageEnhance.Contrast(image)
enhace_pic = ImageEnhance.Contrast(img2) # this is my sharpness object  
# now by using enahnce method i can enhance the picture
enhace_pic.enhance(5).save("catto2Cont.png")
# An enhancement factor of 0.0 gives a solid grey image. A factor of 1.0 gives the original image.

# now to blur image or to apply filters on image we have to use ImageFilter module
from PIL import ImageFilter
img3 = Image.open("Cat 2.jpg","r")
img3.filter(ImageFilter.GaussianBlur(radius=1.1)).save("Catto 2.png") 
# gaussian blur takes one parameter as radius
# radius – Size of the box in one direction. Radius 0 does not blur, returns an identical
# image. Radius 1 takes 1 pixel in each direction, i.e. 9 pixels in total.

# we can use another method BoxBlur method to blur image
img3 = Image.open("Cat 2.jpg","r")
img3.filter(ImageFilter.BoxBlur(3)).save("Catto 3.png") 

# to increase sharpness of mask we 
img3 = Image.open("Cat 2.jpg","r")
img3.filter(ImageFilter.UnsharpMask(2.5,120,10)).save("Catto 4.png") 
# Parameters:	
# radius – Blur Radius
# percent – Unsharp strength, in percent
# threshold – Threshold controls the minimum brightness change that will be sharpened
