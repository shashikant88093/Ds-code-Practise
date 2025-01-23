# DNF

# sort arr with sorting arr 

def sort(arrVal):
    n = len(arrVal)
    mid = 0
    low = 0
    high = n - 1

    while mid < high:
        if arrVal[mid] == 0:
            arrVal[low] ,arrVal[mid] = arrVal[mid] , arrVal[low] 
            # swap(low,mid,arrVal)
            low += 1
            mid += 1
        elif arrVal[mid] == 1:
            mid +=1
        else:
            arrVal[high] ,arrVal[mid] = arrVal[mid] , arrVal[high]
            high -= 1
    return arrVal

arr=[0, 1, 2, 0, 1, 2, 1, 0, 2]

print(sort(arr))