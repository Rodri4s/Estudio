def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max

def main():
    List = [1,2,4,6,8,13]
    maxVal = max(List)
    print(maxVal)

if __name__ == "__main__":
    main()