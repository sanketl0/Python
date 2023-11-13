

class First:
    
    def __init__(self,s):
        self.s = s
    
    def __str__(self):
        return self.s
    # this is method which return a initialize tht given values 


t = First("hello")
print(t)