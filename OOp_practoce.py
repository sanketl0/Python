
class Arithematic:
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B


    def Add(self):
        return self.no1 + self.no2

    def sub(self):
        return self.no1 - self.no2
        

def main():
    print("Enter a first number")
    value1 = int(input())

    print("enter a second number:")
    value2 = int(input())

    obj = Arithematic(value1,value2)

    Ans = obj.Add()
    print("Addition is:",Ans)

    Ans = obj.sub()
    print("Subtraction is :",Ans)


if __name__== "__main__":
    main()



