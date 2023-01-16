import image

#Manda a llamar imagen
img = image.Image("Luther.jpg")
wnd = image.ImageWin(img.getWidth(), img.getHeight())

#Dibuja la imagen con las medidas de la ventana
img.draw(wnd)

#Recorre las filas y columnas de la imagen para detectar sus pixeles
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.get_pixel(col,row)
        #Se define la nueva potencia de cada color
        newPixel = image.Pixel(p.getRed(), 0, p.getBlue())
        img.setPixel(col, row, newPixel)

#Se hace el nuevo dibujo de la imagen
img.draw(wnd)
wnd.exitOnClick()
