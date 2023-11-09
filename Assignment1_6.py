
def new(no):

    if(no>0):
        return "positive number"
    elif(no<0):
        return "negative number"
    else:
        return "zero"

def main():
    
    print("enter a number")
    num1 = input()

    result = new(int(num1))

    print(result)

if __name__ == "__main__":
    main()