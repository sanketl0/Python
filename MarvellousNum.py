
def ChkPrime(arr):
    prime = []
    for i in arr:
        count = 0
        for j in range(1,i):
            if i % j ==0:
                count = count + 1

        if count ==1:
            prime.append(i)

    return prime




