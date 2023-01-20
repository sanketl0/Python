print("Demonstraction of sequence data types:")

# Data : heterogenous
# orderd : no
# indexed : no
# duplicated : no
# mutable : yes

data = { 11,21,51,101,21,11}     #duplicate
data1 = {11, 90, 80, True, "Hello" }# heterogenous

print("first set data:",data)
print("length of data:",len(data))
print("Data is heterogenous :", data1)
print("data is ordered:",data1)
#print("Data at index 2 :" ,data1[2])
print("Data with unqie element:",data)

print("List is mutable:",data)
#insert element
data.add(211)
print("data after insert:",data)

#remove element
data.remove(211)
print("data after removel:",data)

data.discard(201)
print("data after removel:",data)



