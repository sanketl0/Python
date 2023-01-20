
def subtraction(No1,No2):
    Ans = 0
    Ans = No1-No2
    return Ans

def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A < B):
            A,B = B,A
        return Function_Name(A,B)
    return Inner

def main():

    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))

    New_Function = Decorated_Function(subtraction)
    print(New_Function(Value1,Value2))
if __name__ == "__main__":
    main()