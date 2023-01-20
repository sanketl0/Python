
data = [1,2,3,4]

print("output using for")
for no in data :
    print(no, end = " ")


print("\n_____________________________")

print("output using for with index")
for i in range(0,len(data)):
    print(data[i], end = " ")


print("\n________________________________")


print("output using while with index")
i =0
while(i< len(data)):
    print(data[i], end = " ")
    i+=1    # i= i=1



