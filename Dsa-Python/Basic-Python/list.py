# list / Array in python
# =================================== take array length and then loop for multiple input =============================================
# myList = []
# n = int(input())
# for i in range(n):
#     currEle = int(input())
#     myList.append(currEle)

# print(myList)


myList = input().split(" ")

for i in range(len(myList)):
    myList[i] = int(myList[i])

print(myList)
    
