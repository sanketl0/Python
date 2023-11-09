

def maximumElement(arr):
    maxValue = arr[0]
    for i in arr:
        if i >  maxValue:
            maxValue = i
    return maxValue

def main():
    Arr = []

    print("Size of list : ")
    size = int(input())

    print("Enter a values : ")
    for i in range(size):
        value = int(input())
        Arr.append(value)

    print("Our list is : ",Arr)
    print("The maximum element of list is :",maximumElement(Arr))

if __name__ == '__main__':
    main()