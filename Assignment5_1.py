
class Demo():
    def __init__(self,no1,no2):
        self.value1 = no1
        self.value2 = no2

    def Fun(self):
            print(self.value1)
            print(self.value2)

    def Gun(self):
            print(self.value1)
            print(self.value2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    # call the instance method

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == '__main__':
    main()
