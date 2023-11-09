from functools import reduce

Data_input = []

def AcceptList(size):
    for i in range(0 ,size ,1):
        value = int(input("Enter value : "))
        Data_input.append(value)

    return Data_input

multi = lambda a : a*2
IsEven = lambda no : no% 2==0

#def check(no):
    #for x in range(2,no):
        #if no % x == 0:
            #return True

# def ChkPrime(arr):
#     prime = []
#     for i in arr:
#         count = 0
#         for j in range(1,i):
#             if i % j ==0:
#                 count = count + 1
#
#         if count ==1:
#             prime.append(i)
#
#     return prime

def main():

    size = int(input("Enter size of List : "))
    print("Our list is :", AcceptList(size))

    filter_Data = list(filter(IsEven,Data_input))
    print("After filter data is :",filter_Data)

    map_Data = list(map(multi,filter_Data))
    print("After map data : ",map_Data)

    reduce_Data = reduce(max,map_Data)
    print("max number is : ",reduce_Data)


if __name__ == '__main__':
    main()