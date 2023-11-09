

Data_input = []

CheckMax = lambda no : no >=2 and no <= 8

add = lambda a : a+10

product = lambda a,b : a * b

def AcceptList(size):
    for i in range(0,size,1):
        value = int(input("Enter value : "))
        Data_input.append(value)
    return Data_input


def filterx(Helper_function,arr):
    ans = []

    for i in arr:
        if Helper_function(i)==True:
            ans.append(i)
    return ans


def mapx(Helper_function ,arr):
    ans=  []
    for no in arr:
        value = Helper_function(no)
        ans.append(value)
    return ans

def reduceX(Helper_Function, Data):
    Ans = 1
    for no in Data:
        Ans = Helper_Function(Ans, no)

    return Ans


def main():
    size = int(input("Enter size of List : "))
    print("Our list is :",AcceptList(size))

    Data_filter = filterx(CheckMax,Data_input)
    print("After filter Data : ",Data_filter)

    Data_map = mapx(add , Data_filter)
    print("After map data : ",Data_map)

    Data_reduce= reduceX(product,Data_map)
    print("Product is : ",Data_reduce)

if __name__ == '__main__':
    main()