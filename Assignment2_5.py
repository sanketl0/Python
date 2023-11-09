
def checkPrime(num):
    if num > 1:
        for i in range(2,int(num/2)+1):
            if (num % i)==0:
                print(num,"is not prime nmmber")
                break
        else:
            print(num,"is  prime number")

    else:
        print(num,"is not a prime number")



def main():


    print("enter a number :")
    num = int(input())

    checkPrime(num)

if __name__ == "__main__":
    main()