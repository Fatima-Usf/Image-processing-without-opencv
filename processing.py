"""from PIL import Image
#convert the iage to scall grayscale 
pil_im = Image.open('1-min.jpg').convert('L')
#pil_im.show()
# thumbnail: Réduit ou aggrandit l'image
#pil_im.thumbnail((128,128))
box = (80,80,400,400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
#pil_im.show()
region.show()"""

from PIL import Image
from pylab import *

im = array(Image.open('1-min.jpg').convert('L'))

"""
imshow(im)
x = [100,100,400,400]
y = [200,500,200,500]
plot(x,y,"r*")
plot(x[:2],y[:2])
plot(x[:2],y[:2])
#title(’Plotting: "1-min.jpg"’)
show()"""

im.show()
figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')
figure()
hist(im.flatten(),128)
show()