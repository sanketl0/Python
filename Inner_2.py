
def Demo():
    print("Inside Demo")

def fun():
    print("Inside Fun")

def Hello(FPTR):
    print("Inside Hello")
    FPTR()

Hello(Demo)
Hello(fun)


