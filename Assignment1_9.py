

def even(no):
    
    for i in range(0,no+1,2):
        if i % 2==0:
            print(i)

def odd(no):
    
    for i in range(0,no+1,1):
        if i % 2 != 0:
            print(i)    


def main():
    
    no = int(input("enter number:"))
    print("Even Numbers are:")
    
    even(no)

    print("__________________")

    print("Odd numbers are:")
    odd(no)


if __name__ == "__main__":
    main()