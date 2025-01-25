# N lenght array     (1..........N)

# ================= twice and missing ===============
# def solve(givenNums):
#     repeating = - 1
#     missing = -1
#     currSum = 0

#     totalSum = (len(givenNums) * len(givenNums) + 1)//2

#     for i in range(len(givenNums)):
#         if givenNums[abs(givenNums[i]) -1 ]<0:
#             repeating = abs(givenNums[i])
#         givenNums[abs(givenNums[i]) - 1] *= -1

#         currSum+= abs(givenNums[i])
#     missing = totalSum - (currSum - repeating)

#     print(repeating ," " , missing)


# givenNums =[1,2,3,5,4]

# solve(givenNums)


# ============ find reapeting ===================

def findRepeating(givenNums):
    slow = givenNums[0]
    fast = givenNums[givenNums[0]]


    while slow != fast:
        slow = givenNums[slow]
        fast = givenNums[givenNums[fast]]
    
    slow =0

    while slow != fast:
        slow = givenNums[slow]
        fast = givenNums[fast]

    return slow

givenNums = [1,2,3,1,1]


print(findRepeating(givenNums))