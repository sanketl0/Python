
a = 0
b =1

def fibbo(n):
    global a,b
    if n == 0:
        return
    else:
        c = a+b
        print(c, end=" ")
        a = b
        b = c
        fibbo(n-1)


    
    
num = int(input("enter a limit:"))
x = 0
x = fibbo(num)

    


