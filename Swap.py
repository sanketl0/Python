

def swap():
    print("enter first number")
    a = int(input())

    print("enter second number:")
    b = int(input())

    print()
    print("first number before a:",a)
    print("second number before b:",b)
    
    print()

    a,b = b,a

    print("first value after a :",a)
    print("second number after b:",b)
    
if __name__ == "__main__":
    swap()