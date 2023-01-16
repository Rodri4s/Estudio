def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("½División por cero!")
    else:
        print("El resultado es", result)
    finally:
        print("ejecutando la cláusula finally")

def main():
    x = 5
    y = 2
    divide(x,y)

if __name__ == "__main__":
    main()

#TypeError
#IndexError
#KeyError
#ZeroDivisionError
#OverflowError
#MemoryError