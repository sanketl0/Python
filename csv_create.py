import csv
def create():
    with open("data.csv","w") as obj:
        fobj = csv.writer(obj)
        fobj.writerow(['Roll',"Name","Marks"])

        while True:
            roll = int(input("enter a roll number:"))
            name = input("enter name:")
            mark = int(input("enter a marks:"))

            ret = (roll,name,mark)
            fobj.writerow(ret)

            ch = int(input("1-enter more\n  2-exit\n enter your choice:"))

            if ch ==2:
                break
def display():
    with open("data.csv","r") as obj:
        fobj = csv.reader(obj)
        for i in fobj:
            print(i)


create()
display()