

def quicksort(myList,left,right):

    if left < right:
        partitionPos = partition(myList,left,right)
        quicksort(myList,left,partitionPos -1)
        quicksort(myList,partitionPos+1,right)
    return myList

def partition(myList,left,right):
    i = left
    j =right - 1
    pivot = myList[right]

    while i<j:
        while i <right and myList[i] < pivot:
            i += 1
        while j>left and myList[j] > pivot:
            j -= 1

        if i <j:
            myList[i] ,myList[j] = myList[j] , myList[i]

    if myList[i] > pivot:
        myList[i] , myList[right] = myList[right] , myList[i]
    return i
myList = [2,6,8,9,7,5,4,2]
n = len(myList)
print(quicksort(myList,0,n-1))