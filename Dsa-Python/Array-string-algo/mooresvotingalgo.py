# moore's voting algorithm

#  find majority elements

def majorityEle(arr):
    # arr.sort()
    # majorityElement = arr[0]
    maxCount =0
    char =0
    # count = 1
    obj={}
    for i in range(len(arr)):
        if arr[i] in obj:
            obj[arr[i]] += 1
        else:
            obj[arr[i]] = 1

    for key in obj:
        if(obj[key] > maxCount):
            maxCount = obj[key]
            char = key
    return maxCount,char
                 
    




arr=[1,3,2,1,1]

print(majorityEle(arr))