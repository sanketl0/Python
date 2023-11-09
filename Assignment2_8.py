

def main():
    print("enter a number:")
    num = int(input())


    for i in range(0,num+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


if __name__ == "__main__":
    main()