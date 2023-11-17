class Zero:
    
    def __init__(self):
        
        print("zero class constructor")
        
class First(Zero):
    
    def __init__(self):
        super().__init__()                         #it called the constructor of paraent class
        print("zero class constructor")


class Second(First):
    
    def __init__(self):
        super().__init__()                            #it called the constructor of paraent class
        print("zero class constructor")
        
        
s= Second()