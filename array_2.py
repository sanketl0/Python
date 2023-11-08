import array as arr

myarr = arr.array('i',[])   #it an empty array

n = int(input("enter limit"))     #for limit that how many element u want to store

print("enter element")
for i in range(n):
    x=int(input())
    myarr.append(x)
    

for i in range(n):
    print(myarr[i],end=" ")