
def Area(Radius,PI= 3.14):    # default parameter PI = 3.14
    result = PI * Radius * Radius
    return result

def main():
    Rvalue = 10.5
    PIvalue = 3.14

#positional
    Ans = Area(Rvalue,PIvalue) #Ans = Area (10.5,3.14)
    print("Area of circle is:",Ans)

#keyword
    Ans = Area(Radius=Rvalue,PI=PIvalue) #keyword parameter
    print("Area of circle is:",Ans)

#positional and second default
    Ans = Area(10.5)
    print("Area of circle is:",Ans)

#keyword and default
    Ans = Area(Radius=10.5)
    print("Area of circle is:",Ans)
    
#keyword aeguments
    Ans = Area(PI=7, Radius=10.5)
    print("Area of circle is:",Ans)



if __name__== "__main__":
    main()