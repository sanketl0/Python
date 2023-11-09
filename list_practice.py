
def main():
    set = ["sanket","lodhe","rushi","sid"]
    set_1 = [11,12,"vikee",3.14]
    print(set)
    print(set[0])
    print(set[1])
    print(set[-1])
    print(set[1:])
    print(set[:3])
    print(set[1:4])
    print()


    combined = [set,set_1]
    print(combined)
    print()

    set.append("shubham")
    print("data after append ",set)
    print()

    set.insert(2,"ksp")
    print("data after insert",set)
    print()

    set.remove("ksp")
    print("data after remove",set)
    print()

    set.pop()
    print("data after pop",set)
    print()

    set.pop(2)
    print("data after pop",set)
    print()

    del set[3:]
    print("data after del",set)
    print()

    set.extend(["sanket","lodhe","rushi","sid"])
    print("Data after extend ",set)
    print()

    set.sort()
    print("Data after sort",set)

if __name__ == "__main__":
     main()