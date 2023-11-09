print("Our calculator")

import add
import sub
import mul
import div

def main():
    print("Enter first number:")
    no1 = int(input())

    print("enter second number:")
    no2 = int(input())

    addn = add.Addition(no1, no2)
    subn = sub.Subtraction(no1, no2)
    muln = mul.Multiplication(no1, no2)
    divn = div.Division(no1, no2)

    print("Addition is:",addn)
    print("subtraction is:",subn)
    print("multiflicatiom is:",muln)
    print("Division is:",divn)
if __name__ == "__main__":
    main()