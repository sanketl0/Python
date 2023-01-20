
def main():
    try:
        print("enter a first number :")
        No1 = int(input())

        print("enter a second number:")
        No2 = int(input())

        Ans = No1 / No2
        print("Division is :",Ans)

    except ZeroDivisionError:
        print("Inside Zero Division errror")

    except ValueError:
        print("Inside value error")

    except Exception:
        print("Inside last except block")

    finally:
        print("Inside finally block")
        
if __name__ == "__main__":
    main()