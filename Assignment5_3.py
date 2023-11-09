

class Arithematic :
    def __init__(self):
        self.Value1  = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First Number : "))
        self.Value2 = int(input("Enter Second Number : "))

    def Addtion(self): # Behaviour (function)
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        result = self.Value1 * self.Value2
        return result

    def Division(self):
        result = self.Value1 / self.Value2
        return result

def main():

    obj = Arithematic()
    obj.Accept()

    add = obj.Addtion()
    print("Addition is : ",add)

    sub = obj.Subtraction()
    print("Subtraction is : ", sub)

    mul = obj.Multiplication()
    print("Multiplication is : ",mul)

    div = obj.Division()
    print("Division is : ",div)

if __name__ == '__main__':
    main()