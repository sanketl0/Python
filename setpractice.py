def set():

    x = {1,2,"PPA",3.14,"PYTON"}
    y = {5,4,6,"lodhe","rushi"}

    print(x)
    print(y)
    x.update(y)   #it used for add  two sets.
    print(x)
    print("_________________")
    print(len(x))
    x.remove(2)
    print(x)
    x.discard(1)
    print(x)
    x.add("sanket")
    print(x)

if __name__ == "__main__":
    set()