#instance variable : Name , Amount ,Address , AccountNO
# Instance method : CreateAccount(), DisplayAccountInfo()

class Bank_Account:
    Bank_Name = "HDFC bank PVT LTD"
    RoI_on_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def createAccount(self):

        print("enter your name :")
        self.Name = input()

        print("enter your initial amount :")
        self.Amount = int(input())

        print("enter your Address:")
        self.Address = input()

        print("enter your Account number:")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("Your Account information is below---------")
        print("Name of Acount Holder:",self.Name)
        print("Account number:",self.AccountNo)
        print("Address of Acount Holder:",self.Address)
        print("current Amountof Acount Holder:",self.Amount)

def main():
    print("Name of Bank :",Bank_Account,Bank_Name)
    print("Rate of interst fixed deposit:",Bank_Account,ROI_On_FD)
    Bank_Account.DisplayBankInformation()

    user1 = Bank_Account()
    user2 = Bank_Account()

    print("Creating first Account:")
    user1.createAccount()

    print("Creating second Account:")
    user2.createAccount()

    user1.DisplayAccountInfo()
    user2.DisplayAccountInfo()

if __name__ =="__main__":
    main()