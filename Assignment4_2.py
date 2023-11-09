
multiplication = lambda a,b : a * b

def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter Second number : "))

    print("Multiplication of {} and {} is : ".format(num1,num2),multiplication(num1,num2))

if __name__ == '__main__':
    main()