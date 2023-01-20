class Value:

    def __init__(self, Data):
        self.No = Data

    def sumfactors(self):
        sum = 0
        for i in range(1, self.No):
            if (self.No % i == 0):
                sum = sum + i
        return sum

    def chkperfect(self):
        Ans = self.sumfactors()

        if (self.No == Ans):
            return True
        else:
            return False

    def chkprime(self):
        
def main():
    print("enter a number :")
    A = int(input())

    obj = Value(A)

    output = obj.chkperfect()
    if (output == True):
        print("{} is perfect number ", format(A))
    else:
        print("{} is not perfect number ", format(A))


if __name__ == "__main__":
    main()