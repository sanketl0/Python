
values =[10,20,30,40]

print(values)

print(type(values))

print(len(values))

print(values[0])
print(values[1])
print(values[2])
print(values[3])

values.append(50)   # Using .append add new things.
print(values)

values.remove(20)

print(values)

values.append(50)
print(values)

print(type(values[0]))

values.append(90.89)
print(values)

values.insert(2,11)
print("Data after insert:",values)

values.insert(15,89)
print("data after insert is:",len(values))

#append insert value in last position.
