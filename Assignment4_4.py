import math
from functools import reduce
Data_input = []

IsEven = lambda no : no%2==0

square = lambda no : int(math.pow(no,2))

sum = lambda a,b : a+b

def AcceptList(size):
    for i in range(0,size,1):
        value = int(input("Enter value : "))
        Data_input.append(value)

    return Data_input

def main():

    size = int(input("Enter size of List : "))
    print("Our list is :",AcceptList(size))

    filter_Data= list(filter(IsEven,Data_input))
    print("After filter data is  : ",filter_Data)

    map_Data = list(map(square,filter_Data))
    print("After Map data is : ",map_Data)

    reduce_Data = reduce(sum,map_Data)
    print("Sum of Data is : ",reduce_Data)

if __name__ == '__main__':
    main()