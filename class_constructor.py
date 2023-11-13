# role of constructor in inheritace


class First:
    
    def __init__(self):
        print("this is  first class a constructor")
        
class Second(First):
    pass


t =Second()
print(t)