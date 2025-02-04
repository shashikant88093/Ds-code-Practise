
# arr = [5,3,2,1,4]
arr = [1,4,3,2,1]


def insertionfunction(arrlist):
    for i in range(1,len(arrlist)):
        key = arrlist[i]
        j = i -1
        while( j>= 0 and arrlist[j] > key):
            arrlist[j+1] = arrlist[j]
            j -= 1

        arrlist[j+1] = key
        print(arrlist,"arrlist")
    return arrlist



print(insertionfunction(arr))

