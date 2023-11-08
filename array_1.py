import array as arr 

myar = arr.array('b',[10,20,30,-10])  #it takes both positive and negative 
myars = arr.array('B',[10,20,30,10])   #it takes only positve int
print(myar)
print(myars)



ar = arr.array('i',[100,20,30,50,60])

# sliging
print(ar[4:])

# using direct access of data
# for i in ar:
#     print(i, end='')

# access data using index number
# n =len(ar)
# for i in range(n):
#     print(arr[i])

