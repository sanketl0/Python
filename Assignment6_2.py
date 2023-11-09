class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter your name:")
        self.Amount = int(input("Enter Amount in your Account:"))

    def Display(self):
        print("Name:",self.Name)
        print("Amount in your Accont:",self.Amount)

    def Deposit(self):
        self.Amount += int(input("Enter Amount You want to Deposite:"))


    def Withdrawl(self):
        self.Amount -= int(input("Enter Amount you want to withdrawal:"))

    def CalculateInterest(self):
        rateofInterst = (BankAccount.ROI * self.Amount *12) /100
        print("Rate of interest on your amount is per year is :",rateofInterst)


def main():

    customer1 = BankAccount()
    customer1.Deposit()
    customer1.Withdrawl()
    customer1.Display()
    customer1.CalculateInterest()

    customer2 = BankAccount()
    customer2.Deposit()
    customer2.Withdrawl()
    customer2.Display()
    customer2.CalculateInterest()

    customer3 = BankAccount()
    customer3.Deposit()
    customer3.Withdrawl()
    customer3.Deposit()
    customer3.CalculateInterest()

if __name__ == "__main__":
    main()