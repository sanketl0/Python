#Normal function or named function
#def function_Name(function_parameter):
#function body

def Add(no1,no2):
    return no1+no2


#Lambda function or unnamed function
#lambda parameter : body

Addfunction = lambda A,B : A+B

Ans1 = Add(10,11)
Ans2 = Addfunction(10,11)

print("addition using normal function :",Ans1)
print("addition using lamba function  :",Ans2)

print("Type of lambda function is:",type(Addfunction))