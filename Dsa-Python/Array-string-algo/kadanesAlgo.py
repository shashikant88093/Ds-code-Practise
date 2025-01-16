# largest subarray sum

# input 2 3 6 7 8 -9 -8 6 1
# input -1 -2 -3
import sys

#  with while loop
def largestsubsum(myInput):
    maxSum = -sys.maxsize - 1
    currSum = 0
    start =  0
    end = 0
    n = len(myInput)
    while end < n:
        while currSum < 0:
            currSum -= myInput[start]
            start += 1

        currSum += myInput[end]
        end += 1

        maxSum = max(currSum,maxSum)
        
    return maxSum


# with for loop

# def largestsubsum(myInput):
#     maxSum = -sys.maxsize -1  # Initialize with the smallest possible integer
#     currSum = 0

#     for num in myInput:
#         currSum = max(num, currSum + num)  # Include current number in sum or start a new sum
#         maxSum = max(maxSum, currSum)     # Update the maximum sum found so far

#     return maxSum
# myInput = [2,3,6,8,-9,-8,6,1]
# ouput = 19
# myInput = [1,4,-3,10,-20,12]
#  output = 12
myInput = [-1 -2 -3]
# output = -1

print(largestsubsum(myInput))