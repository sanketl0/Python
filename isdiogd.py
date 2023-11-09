
def Addition(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Decorator_function(Function_Name):
    def Inner(A,B):
        if(A < B):
            A,B = B,A
        return Function_Name(A,B)
    return Inner


def main():
    Value1 = int(input("Enter first value:"))
    Value2 = int(input("enter second value:"))

    New_function = Decorator_function(Addition)
    print(New_function(Value1,Value2))

if __name__ == "__main__":
    main()
