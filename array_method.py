import array as arr
myarr = arr.array('i',[10,20,30,20,10,50,20])

myarr.reverse()
print(myarr)

myarr.insert(3,80)
print(myarr)

m = myarr.count(20)
print(m)


myarr.remove(30)
print(myarr)