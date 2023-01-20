from functools import reduce

CheckEven = lambda no: no % 2 == 0
Doubles = lambda no: no *2
sum = lambda  A,B: A + B




def main():
    print("enter a number of elements you want to enter :")
    isize = int(input())

    Data_input = []
    print("enter a elements")
    for icnt in range(0,isize,1):
        value = int(input())
        Data_input.append(value)

    print("Data is :",Data_input)

    Data_Filter = list(filter(CheckEven,Data_input))
    print("Data after filter is :",Data_Filter)

    Data_map = list(map(Doubles,Data_Filter))
    print("Data after map:",Data_map)

    Data_reduce = reduce(sum,Data_map)
    print("Data after reduce is :",Data_reduce)

if __name__ == "__main__":
    main()