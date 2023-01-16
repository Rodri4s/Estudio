def average(numlist):

    total = 0
    for num in numlist:
        total = total + num
    return total / len(numlist)

def main():
    list = [1,2,3,4,5]
    prom = average(list)
    print(prom)

if __name__ == "__main__":
    main()