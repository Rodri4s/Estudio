def min(lst):
    min = lst[0]
    for e in lst:
        if e < min:
            min = e
    return min

def main():
    List = [1,2,4,6,8,13]
    minVal = min(List)
    print(minVal)

if __name__ == "__main__":
    main()