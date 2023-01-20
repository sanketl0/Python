
def Add(*values):
    sum = 0
    for no in values:
        sum = sum + no
    return sum

#def Addx(*values):
  #  sum = 0
  #  for i in range(0,len(values),1):
    #    sum = sum + values[i]
   # return sum


def main():
    Ans = Add(1,2,3,4,5)
    print("Additon is :",Ans)
    
if __name__== "__main__":
    main()