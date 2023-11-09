

def main():

    num = int(input("enter number:"))

    for i in range(0,num):
        for j in range(1,num+1):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    main()