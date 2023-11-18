  
# a = int (input ("enter a numbe:"))
# b = int (input ("enter a number:"))

# c =a //b
# print(c)



try:
    a = int (input ("enter a numbe:"))
    b = int (input ("enter a number:"))
    c = a // b
    print(c)
    
except ZeroDivisionError as obj:
    print("enter only numbers")

except ValueError as e:
    print(e)
    
print("visit again with a numbe which is grater than zero")

  
  
  