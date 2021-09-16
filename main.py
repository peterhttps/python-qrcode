import qrcode
from PIL import Image

inputText = input("Tell a qrcode information:\n> ")

img = qrcode.make(inputText)
type(img)  
img.save("some_file.png")
im = Image.open("some_file.png")
im.show()