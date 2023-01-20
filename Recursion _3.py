
def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)            #recursive calling function
        print(No)              #backtracking          ##head recursion
def main():

    Display(4)


if __name__ == "__main__":
    main()