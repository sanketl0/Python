

# class First(object):
#     def __init__(self):
#         super().__init__()                            #it called constructor of second
#         print("First constructor")
        
# class Second(object):
#     def __init__(self): 
#         print("Second constructor")
        
# class Third( First,Second):
#     def __init__(self):                         #it called constructor of first
#         super().__init__()
#         print("Third constructor")


# t= Third()




class First(object):
    def __init__(self):                                 
        print("First constructor")
        
class Second(object):
    def __init__(self): 
        super().__init__()                             #it called constructor of first
        print("Second constructor")
        
class Third(Second,First):
    def __init__(self):                         #it called constructor of first
        super().__init__()
        print("Third constructor")


t= Third()



















