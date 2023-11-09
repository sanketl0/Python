

def minimumElement(Arr):
    minValue = Arr[0]
    for i in Arr:
        if i <  minValue:
            minValue = i
    return minValue

def main():
    Arr = []

    print("Size of list : ")
    size = int(input())

    print("Enter a values : ")
    for i in range(0,size):
        value = int(input())
        Arr.append(value)

    print("Our list is : ",Arr)
    print("The minimum element of list is :",minimumElement(Arr))

if __name__ == '__main__':
    main()