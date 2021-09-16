import qrcode

inputText = input("Tell a qrcode information:\n> ")

img = qrcode.make(inputText)
type(img)  
img.save("some_file.png")