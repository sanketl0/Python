

Batches = {"PPA":1800,"LB":16700,"Python":16500,"Angular":15000}

print("Data of dictnary:",Batches)
print("_______________________________________")
print("data traversal using for loop")
for x in Batches :
    print(x)
print("_______________________________________")

print("data traversal using for loop")
for x in Batches :
    print(x ,Batches[x])
print("_______________________________________")

print("data traversal using for loop")
for x in Batches:
     print(x ,Batches.get(x))
print("_______________________________________")


keysBatches = Batches.keys()
print(type(keysBatches))
print(keysBatches)
print("_______________________________________")

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)
