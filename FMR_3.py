
CheckEven = lambda no: no % 2 == 0

Doubles = lambda no: no *2

sum = lambda  A,B: A + B


def FilterX(Helper_Function,Data):
    result = []
    for no in Data:
        if(Helper_Function(no)==True):
            result.append(no)
    return result


def mapX(Helper_Function,Data):
    result = []
    for no in Data:
        value = Helper_Function(no)
        result.append(value)
    return result

def reduceX(Helper_Functionn,Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Functionn(Ans,no)
    return Ans

def main():
    print("enter a number of elements you want to enter :")
    isize = int(input())

    Data_input = []
    print("enter a elements")
    for icnt in range(0,isize,1):
        value = int(input())
        Data_input.append(value)

    print("Data is :",Data_input)

    Data_Filter = FilterX(CheckEven,Data_input)
    print("Data after filter is :",Data_Filter)

    Data_map = mapX(Doubles,Data_Filter)
    print("Data after map:",Data_map)

    Data_reduce = reduceX(sum,Data_map)
    print("Data after reduce is :",Data_reduce)

if __name__ == "__main__":
    main()