
class Circle:
    def __init__(self):
        self.Redius = 0
        self.Area =0
        self.Circumference =0
        self.PI = 3.14

    def Accept(self):
        print("Enter redius of Circle : ")
        self.Redius = int(input())

    def CalculateArea(self):
        self.Area = 2*self.PI*self.Redius *self.Redius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Redius
        return self.Circumference

    def Display(self):
        print("Redius of cirlce: ",self.Redius)
        print("Area of cirlc : ",self.CalculateArea())
        print("Circumference of circle :",self.CalculateCircumference())

def main():

    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2 = Circle()
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()


if __name__ == '__main__':
    main()