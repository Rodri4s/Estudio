import image

def imagen(Xrange,Yrange,color):
    img = image.Image("Luther.jpg")
    win = image.ImageWin(img.getWidth(), img.getHeight())
    img.draw(win)
    #gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    #Recorre todas las filas y columnas de la imagen y obtieve los pixeles:
    centerX = img.getWidth()/2
    centerY = img.getHeight()/2
    for row in range(int(centerY - Yrange/2), int(centerY + Yrange/2)):
        for col in range(int(centerX - Xrange/2), int(centerX + Xrange/2)):            
            p = img.getPixel(col, row)
        
            if color == "red":
                r = p.getRed()
                g = 0
                b = 0
            elif color == "green":
                r = 0
                g = p.getGreen()
                b = 0
            elif color == "blue":
                r = 0
                g = 0
                b = p.getBlue()
            else:
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

def main():
    Xrange = int(input("Indica el ancho del cuadrado: "))
    Yrange = int(input("Indica el alto del cuadrado: "))
    color = input("Indique el color que desee mantener: ")
    imagen(Xrange, Yrange, color)



if __name__ == "__main__":
    main()