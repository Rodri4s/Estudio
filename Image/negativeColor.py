import image

img = image.Image("Luther.jpg")
wnd = image.ImageWin(img.getWidth(),img.getHeight())
img.draw(wnd)
img.setDelay(1,15) #Genera la imagen tipo animacion

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col,row)

        newR = 255 - p.getRed()
        newG = 255 - p.getGreen()
        newB = 255 -p.getBlue()

        newPixel = image.Pixel(newR,newG,newB)
        img.setPixel(col,row,newPixel)

img.draw(wnd)
wnd.exitOnClick()