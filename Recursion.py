
def Display(No):
    if(No > 0):
        print("Hello")
        No = No - 1
        Display(No)    #recursive function call      #tail recursion


Display(4)   # function call