
def Outer():                          #100
    print("Inside Outer")

    def Inner():                      #200
        print("Inside inner")

        return Inner               #return 200


ret = Outer()
print(type(ret))
print(id(ret))
ret                                #ret  = 200()