

def star():
    print("enter a number:")
    num = int(input())

    for i in range(0,num):
        print()
        for j in range(1,num+1):
            print(j, end=" ")
            
def main():

    star()

if __name__ == "__main__":
    main()