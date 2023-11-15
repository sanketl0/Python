# here abstact class is used to get the properties of parent clss to child class
# in abstract class we cant create a object of main abstract class but we can use whole propeties of that clas using inheritace way
# Also we have mandatory to overide the abstact method in child class 
# Also we cant access the main  class method directly for that we cna access them using child class object



from abc import ABC , abstractmethod


class Button(ABC):
    
    @abstractmethod    
    def click(self):                     #abstractmethod
        pass
    
    def display(Self):             # simple class method 
        print("this is a abstract method")
        
        
class mycolor(Button):
    
    def click(self):             # override method  from parent class
        print("red color")
    
class myphoto(Button):
    
    def click(self):           # override method from parent class
        print("green color")
        
        



m = mycolor()                     #object of child
m.display()                          #this is parat class method accessed by  chideclass
m2 = myphoto()                 #object of child

m.click()                               
m2.click()













