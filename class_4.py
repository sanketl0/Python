
class First:
    
    def __init__(self):
        self.name="sanket"
        self.sr = 10
        self.course = "BE"
        
class Second(First):
    
    def __init__(self):  # is a constructor which gets override the parant class constructor 
        print("this is a constructor of second class")    
        self.name = "sanket"
    
    def display(self):
        print(self.name)
        # print(self.sr)
        # print(self.course)
        


t = Second()
t.display()