
class Arithametic:

    def __init__(self,A,B):
        print("inside init method:")
        self.NO1 = A
        self.NO2 = B

    def Add(self):
        Ans = self.NO1 + self.NO2
        return Ans

    def sub(self):
        Ans = self.NO1 - self.NO2
        return Ans


def main():
    print("inside main method:")

    obj = Arithametic(11,10)

    output = obj.Add()
    output = obj.sub()
    print("Adddition is :", output)
    print("subtraction is ",output)

    objx = Arithametic(12,8)
    
    outputx = objx.Add()
    print("Addition of objx:",outputx)

if __name__ == "__main__":
    main()