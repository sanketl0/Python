
def Add(A,B):
    return A+B

def sub(A,B):
    return A-B

def calculator(Target, Value1,Value2):
    return Target(Value1,Value2)


Ret = calculator(Target=Add,Value1=10,Value2=11)
print("Addition is :",Ret)

Ret = calculator(Target=sub,Value1=10,Value2=11)
print("subtraction is :",Ret)

