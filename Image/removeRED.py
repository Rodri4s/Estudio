import image

img = image.Image("Luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

#Recorre las filas y columnas de la imagen para obtenes los valores de los pixeles
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        newpixel = image.Pixel(0, p.getGreen(), p.getBlue()) #Convierte los pixeles de rojo a cero
        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()