myList = []
target = 0

def binarySearch(start,end):
    global myList
    global target

    if end-start <= 1:
        if myList[start] == target:
            return start
        
        if myList[end] == target:
            return end
        return -1
        
    middle=(start+end)/2

    if myList[middle] > target:
        return binarySearch(start,middle)
        
    return binarySearch(middle,end)
    
n = int(input())

target = int(input())

myList = [int(ele) for ele in input().split() ]

index = binarySearch(0,n-1)

print(index)

