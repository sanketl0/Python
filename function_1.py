#function whitch accepts nothin and return nothing
def Demo1():
    print("inside Demo1")



#function accepts one paramerter and return nothing
def Demo2(no):
    print("Inside Demo with argument:",no)


#function accepts one parameter and return one parameter
def Demo3(no):
    print("Inside Demo with argument:",no)
    return no+2

#function accepts two parameter and return one paremeter
def Demo4(no1,no2):
    print("Inside Demo4")
    Add = no1 + no2
    return Add

# function acceetps two  parameter and return two parameter
def Demo5(no1,no2):
    print("Inside Demo5")
    Add = no1 + no2
    Sub = no1 - no2
    return Add,Sub

def main():

    Demo1()

    Demo2(11)

    Ans = Demo3(10)
    print("return value of Demo3 is :",Ans)
    
    Ans = Demo4(11,10)
    print("return value is :",Ans)

    Ans1,Ans2 = Demo5(11,10)
    print("Add and sub :",Ans1,Ans2)
    #print("second value:",Ans2)

if __name__ == "__main__":
    main()