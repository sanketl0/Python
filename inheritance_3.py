class Marks1:
    
    def __init__(self,eng,hindi):
        self.eng = eng
        self.hindi = hindi
        

class Marks2(Marks1):
    
    def __init__(self,math,comp,e,h):
        super().__init__(e,h)
        self.math = math
        self.comp = comp
        
    def display(self):
        print("math: " , self.math)
        print("comp: " , self.comp)
        print("eng: " , self.eng)
        print("hindi: " , self.hindi)
        
        if self.math > 50:
            print("marks is good")
        else:
            print("marks is bad")
            
        
        
s = Marks2(40,70,40,90)
s.display()