
# how many ways we use static variables

class Test: 
    
    n= 100
    
    def __init__(self):         #constructor
        Test.n+= 10
        
    def nonstaticmethod(Self):      #non-static method
        Test.n += 10
        
        
    @staticmethod
    def mystaticmethod():           #static method
        Test.n += 10
    
    @classmethod    
    def myclassmethod(cls):           #class method
        cls.n  += 10
        

t=Test()
t.nonstaticmethod()
t.mystaticmethod()

Test.n+=10       #it uses the static outside the class method
print(Test.n)