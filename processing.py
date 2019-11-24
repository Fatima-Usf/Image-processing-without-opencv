from PIL import Image
import OS
#convert the iage to scall grayscale 
pil_im = Image.open('1-min.jpg').convert('L')
pil_im.show()
