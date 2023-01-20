
def factor():
    print("Enter number")
    num = int(input())

    print("factors are :")
    for i in range(1,int(num/2)+1,1):
        if num % i == 0:
            print(i)
      #  i = i+1


if __name__ == "__main__":
    factor()