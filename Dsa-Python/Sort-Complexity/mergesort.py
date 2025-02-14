mylist = [1,4,3,2,1]

# divide and conduer
n = len(mylist)

def mergeSort(list,left,right):
    if left<right:
        mid = (left+right)//2
        mergeSort(list,left,mid)
        mergeSort(list,mid+1,right)
        merge(list,left,mid,right)

def merge(list,left,mid,right):
    i = left
    j = mid+1
    temp = []
    
    while i <= mid and j <= right:
        if list[i] <= list[j]:
            temp.append(list[i])
            i += 1
        else:
            temp.append(list[j])
            j += 1
            
    while i <= mid:
        temp.append(list[i])
        i += 1
        
    while j <= right:
        temp.append(list[j])
        j += 1
        
    for k in range(len(temp)):
        list[left+k] = temp[k]

mergeSort(mylist,0,n-1)

print(mylist)
