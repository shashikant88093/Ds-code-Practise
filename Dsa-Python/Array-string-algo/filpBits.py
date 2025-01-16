# Kadannes Algo is used in Flip bits

# input 00110100
# output 11001100

# input 0001000
# output 1110111
import sys

def getNum(value):
    if value == "0":
        return 1
    else:
        return -1

def flipbit(inputBinary):
    ans =0
    for i in inputBinary:
        if i == "1":
            ans+=1
        
    maxSum = -sys.maxsize -1
    currSum = 0
    end =0
    start =0

    n = len(inputBinary)
    while end < n:
        while currSum <0:
            currSum -= getNum(inputBinary[start])
            start += 1

        currSum += getNum(inputBinary[end])
        end += 1
        maxSum= max(currSum,maxSum)
    return ans + maxSum







input = "0010111"
# input = "00110100"
# output = 11001100
# input = "0001000"
# output = 1110111

print(flipbit(input))