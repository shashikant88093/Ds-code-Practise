#  sum of n input    ============ and sum of all list

# n = int(input())
# myList = input().split(" ")
# sum = 0
# for i in range(n):
#     sum += int(myList[i])

# print(myList)
# print(sum)

#  ================ min and max in list ===========================

myList = [2,3,4,6,8,9,1,10]

max = myList[0]
min = myList[0]

for val in myList:
    if val > max :
        max = val
    if val < min :
        min = val
print(max)
print(min)