import math

result = lambda number : int(math.pow(number,2))

def main():

    print("Enter a number")
    number = int(input())

    #print("power of {} is : ".format(number),result(number))
    print("The power of given number is:",result(number))

if __name__ == '__main__':
    main()
