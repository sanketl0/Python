
def square(No):
    return No*No


def main():

    Data = [1,2,3,4,5]

    result = []

    for value in Data:
        result.append(square(value))

    print("result after square is :",result)

if __name__ == "__main__":
    main()