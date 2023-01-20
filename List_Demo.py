print("Demonstraction of sequence data types:")

# Data : heterogenous
# orderd : yes
# indexed : yes
# duplicated : yes

data = [ 11,21,51,101]
data1 = [11, 90, 80, True, "Hello" ] # heterogenous

print("Data is heterogenous :", data1)
print()
print("data is ordered:",data1)
print()
print("Data at index 2 :" ,data1[2])
print()
print("Data with duplicate element:",data)
print()
print("List is mutable:",data)
print()
data.append(201)
print("data after append:",data)
print()
data.pop()
print("data after pop:",data)