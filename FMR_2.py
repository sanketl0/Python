def CheckEven(no):
    return (no%2==0)

def Doubles(no):
    return no*2

def sum(A,B):
    return A+B

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

def reduceX(Helper_Function,Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans,no)
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