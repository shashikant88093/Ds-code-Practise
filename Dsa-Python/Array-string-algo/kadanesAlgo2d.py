# kadanes Algo is applicable only for 1D array 
# Max sum reactangle 
# convert all into 1d array
import sys
# kadane algo
def kanadealorithm(givenNumber):
    maxSum = -sys.maxsize -1
    currSum = 0
    end =0
    start=0
    
    length = len(givenNumber)

    while end < length:
        while currSum <0:
            currSum -= givenNumber[start]
            start += 1
        
        currSum += givenNumber[end]
        end += 1
        maxSum = max(currSum,maxSum)
    return maxSum

matrix = [[3,8,9,1,3],[-4,-1,1,7,-6],[-2,-3,8,1,-1]]

n = len(matrix)
m = len(matrix[0])
ans = -sys.maxsize -1
# Outer Loop (Iterating Over Columns):
for i in range(m):
    temp = []
# Collects the elements of the current column into a temporary 1D array (temp).
    for j in range(n):
        temp.append(matrix[j][i])
# Computes the maximum sum subarray for temp using Kadane’s algorithm and updates ans with the larger value.
    ans = max(ans,kanadealorithm(temp))
# Iterates over columns starting from i + 1 to include more columns in the current submatrix.
# Updates temp: Adds the values from the new column to the existing temp array.
# Kadane’s Algorithm: Finds the maximum sum subarray for the updated temp.
    for j in range(i+1,m):
        for k in range(n):
            temp[k] += matrix[k][j]
        ans = max(ans,kanadealorithm(temp))

print(ans)