#  2 sum problem 

# [1,2,5,7,10] target = 17

# def twosum(givenNums,targetVal):
#     temp = givenNums.copy()
#     givenNums.sort()
#     start = 0
#     end = len(givenNums) - 1

#     while start < end:
#         currentsum = givenNums[start] + givenNums[end]
#         if currentsum == targetVal:
#             # return [start,end]
#             ans = []
#             for i in range(len(temp)):
#                 if givenNums[start] == temp[i] or givenNums[end] == temp[i]:
#                     ans.append(i)
#             return ans
#         if currentsum > targetVal:
#             end -= 1
#         else:
#             start += 1
#     return -1
        

# arr = [1,7,5,2,10]
# targetVal=17
# print(twosum(arr,targetVal))

# three sum

def thresum(givenNums,targetVal):
    temp = givenNums.copy()
    givenNums.sort()
    
    for k in range(len(givenNums)):
        tempTarget = targetVal
        tempTarget -= givenNums[k]

        start = k+1
        end = len(givenNums) - 1

        while start < end:
            currsum = givenNums[start] + givenNums[end]

            if currsum == tempTarget:
                ans = []

                for i in range(len(temp)):
                    if givenNums[start] == temp[i] or givenNums[end] == temp[i] or givenNums[k] == temp[i]:
                        ans.append(i)

                return ans
            
            if currsum > targetVal:
                end -= 1

            else:
                start += 1

    return -1
arr = [1,4,6,7,9,8,3]
targetVal = 18

print(thresum(arr,targetVal))
