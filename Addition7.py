print("application to demonstate Industrial Programming")

import add
import sub 

def main():
    print("Value of __name__ from main is :",__name__)

    print("Enter first number:")
    no1 = int(input())

    print("Enter second number:")
    no2 = int(input())

    results= add.Addition(no1, no2)
    result= sub.Subtraction(no1, no2)

    print("Addition is:",results)
    print("Subtraction is:",result)

if __name__ == "__main__":
    main()