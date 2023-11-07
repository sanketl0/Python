

mystr = "I am sanket lodhe and i am software developer a"

mynew = list(filter(lambda v :( v =='a'or v =='e'or v =='i'or v =='o'or v =='u'),mystr))

print(mynew)
count = 0
for i in mynew:
    count = count+1
    print(count)
