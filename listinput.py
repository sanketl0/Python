def main():
    Arr = []

    print("Enter how many element you want to store?")
    size = int(input())

    print("please enter the values:")
    
    for i in range(0,size,2):
        no = int(input())
        Arr.append(no)   # Arr.insert(i,no)

    print(Arr)

if __name__ == "__main__":
    main()










