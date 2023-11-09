
from functools import reduce

class Numbers:
    Data = []

    def __init__(self):
        self.value = int(input("Enter number:"))

    def chkprime(self):
        for i in range(2,self.value,1):
            if(self.value % i == 0):
                return False
            else:
                return True

    def chkperfect(self):
        sum = 0
        for i in range(1,self.value):
            if (self.value % i == 0):
                sum = sum +1
        if (sum == self.value):
            return True
        else:
            return False

    def Factor(self):
        for i in range(1,int(self.value/2)+1,1):
            if(self.value % i == 0):
                print(i)
                Numbers.Data.append(i)

    def sumfactor(self):
        result = reduce(lambda a,b : a+b ,Numbers.Data)
        print(result)

def main():
    obj1 = Numbers()
    obj1.chkprime()
    obj1.chkperfect()
    obj1.Factor()
    obj1.sumfactor()

    obj2 = Numbers()
    obj2.chkprime()
    obj2.chkperfect()
    obj2.Factor()
    obj2.sumfactor()

    obj3 = Numbers()
    obj3.chkprime()
    obj3.chkperfect()
    obj3.Factor()
    obj3.sumfactor()



if __name__ == "__main__":
    main()
