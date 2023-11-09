import array as arr 
import numpy as np

n = int(input("enter a limt:"))
myar= arr.array('i',[])
print("enter a element:")
for i in range(n):
    x= int(input())
    myar.append(x)

s= int(input("enter a element to search in array"))

# if s in myar:
#     print("success")
# else:
#     print("failure")

myar1 = np.reshape(myar,(n))
myar1.sort()
print("after sorted:",myar1)

low = 0
high = n-1
f = 0

while low <= high:
    mid=((low+high)//2)
    
    if(s==myar1[mid]):
        f=1
        break
    elif(s>myar1[mid]):
        low =mid+1
    else:
        high = mid-1
        
if f == 1:
    print("success")
    
else:
    print("unsucess")

















