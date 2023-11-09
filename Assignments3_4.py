
Arr = []
def AcceptValue(size):
    print("Enter Numbers : ")

    for i in range(0,size):
        value = int(input())
        Arr.append(value)
    return Arr

def CheckFrequecy(ele,arr):
    count = 0
    for i in arr:
        if(i==ele):
            count=count+1
    return count



def main():

    print("Enter size of list : ")
    size = int(input())
    print("Our list is ",AcceptValue(size))

    print("Element to Search : ")
    Element = int(input())

    print("Frequency  is : ",CheckFrequecy(Element,Arr))


if __name__ == '__main__':
    main()