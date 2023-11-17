
class Base:
    
    def add(self,a,b):
        c = a+b
        return c
    
    
class derived(Base):                  #this is known as is a relation ship
    
    def sub(self,a,b):
        c = a - b
        return c
    


d= derived()         #obj of derived class 
x= d.add(10,20)          #we can access  method of base class 
y = d.sub(10,2)
print (x,y)
          










