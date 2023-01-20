# Take a number from user and store it in to list and addition of that listed element.

class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = []

    def Accept(self):
        print("How many element you want to store?")
        self.size = int(input())

        print("Enter a element:")
        value = 0
        for i in range(0,self.size):
            value = int(input())
            self.Arr.append(value)

    def Display(self):
        print("Element from list are :")
        for i in range(0,self.size):
            print(self.Arr[i])

    def Addition(self):
        sum = 0
        for i in range(0,self.size):
            sum = sum + self.Arr[i]
        return sum
    

def main():

    obj = Numbers()
    obj.Accept()
    obj.Display()

    output = obj.Addition()
    print("Addition of list is :",output)


if __name__ == "__main__":
    main()