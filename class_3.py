class Test:
    
    def __init__(self):  # it is constuctor which called auto when obj is created and its main purpose is to initilaize value to given variables
        self.rollno=101
        self.name ="sanket"
        self.clg = "scsmcoe"
        
    def display(self):
        print(self.rollno)
        print(self.name)
        print(self.clg)
        
    def __str__(self):
        return "this is a first method called when obj is created"
        


t = Test()
print(t)
t.display()