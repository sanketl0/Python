#
# def Display(No):
#     if(No > 0):
#         print(No)
#         No = No - 1
#         Display(No)            #recursive calling function
#
# def main():
#
#     Display(4)
#
#
# if __name__ == "__main__":
#     main()


def Patter(N):
    i=0
    if(i<=N):
        print("*",end=" ")
        i = i+1
        Patter(N)



Patter(5)