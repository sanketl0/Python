mylist = [10,20,30,40,50,60,70,80]
try:
    i = int(input("enter index number:"))
    print(mylist[i])

except ValueError as v:
    print(v)
    
except IndexError as s:
    print(s)
    
finally:
    print("Im  last")                       # finally is a exception which always prints last at the program 
    
    
    