
def number(no):

    if(no%5==0):
        return "true"
    else:
        return "false"

def main():
    print("Enter number")
    num = input()

    Divisions = number(int(num))

    print(Divisions)


if __name__ == "__main__":
    main()