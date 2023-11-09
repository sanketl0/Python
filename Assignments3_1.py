
def sumOfElement(n):
    sum = 0
    for value in n:
        sum = sum + value
    return sum


def main():
    
    Arr = list()
    print("number of elements:")
    num = int(input())

    print("please enter the values:")
    for i in range(num):
        no = int(input())
        Arr.append(no)
        
    print("List is :",Arr)

    result = sumOfElement(Arr)
    print("sum of list :",result)
    
if __name__ == "__main__":
    main()
    
    
    

    

