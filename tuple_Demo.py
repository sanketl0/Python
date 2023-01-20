print("Demonstare of tuple")

# Data : heterogenous
# orderd : yes
# indexed : yes
# duplicated : yes
# mutable : no

data = [ 11,21,51,101]       #duplicate
data1 = [11, 90, 80, True, "Hello" ] # heterogenous

print("Data is heterogenous :", data1)
print("data is ordered:",data1)
print("Data at index 4 :" ,data1[4])
print("Data with duplicate element:",data)
print("Length of element is",len(data1))
print(data1[1:4])
print(data1[0:])
print(data1[1:])
print(data1[:4])
print(data1[2:3])