# Jugglingalgo Algo
#  arr = [1,2,3,4,5]

# d times right rotation  
from math import gcd
def rotatearr(arr,rot):
    n = len(arr)
    gcdVal = gcd(n,rot%n)
    print(gcdVal)
    for i in range(gcdVal):
        temp = arr[i]
        j=i
        while True:
            k = (j-rot)%n
            if k == i:
                break

            arr[j] = arr[k]
            j=k
        arr[j] = temp
    return arr

arr = [1,2,3,4,5]
rot = 2


print(rotatearr(arr,rot))