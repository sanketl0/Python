# Applicatin to find out maximum number.

def maximum(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2


def main():
    print("enter first numer:")
    value1 = input()

    print("enter second number:")
    value2 = input()

    Ans = maximum(int(value1), int(value2))

    print("largest number is :",Ans)
if __name__ == "__main__":
    main()