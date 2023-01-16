import image

img = image.Image("Luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
#gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

#Recorre todas las filas y columnas de la imagen y obtieve los pixeles:
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        
        #Convierte los valores del los leds RGB a gris
        r = 0.299 * p.getRed() + 0.587 * p.getGreen() + 0.114 * p.getBlue()
        g = 0.299 * p.getRed() + 0.587 * p.getGreen() + 0.114 * p.getBlue()
        b = 0.299 * p.getRed() + 0.587 * p.getGreen() + 0.114 * p.getBlue()

        #Utiliza los nuevos pixeles para indicar el nuevo color de la imagen
        #         
        newpixel = image.Pixel(int(r),int(g),int(b))
        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()