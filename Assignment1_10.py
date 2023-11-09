
def user():
    
    print("enter name:")
    name = input()
    return len(name)



def main():


    result = user()
    print(result)


if __name__ == "__main__":
    main()