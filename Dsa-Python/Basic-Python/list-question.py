#  sum of n input    ============ and sum of all list

# n = int(input())
# myList = input().split(" ")
# sum = 0
# for i in range(n):
#     sum += int(myList[i])

# print(myList)
# print(sum)

#  ================ min and max in list ===========================

# myList = [2,3,4,6,8,9,1,10]

# max = myList[0]
# min = myList[0]

# for val in myList:
#     if val > max :
#         max = val
#     if val < min :
#         min = val
# print(max)
# print(min)


#  ========= Mean ===========
# defination = mean = sum/lenght 

# myList = [2,3,4,6,8,9,1,10]
# sum = 0
# for val in myList:
#     sum += int(val)

# print(sum)
# print(sum/len(myList))

#  =========== medain ==================

#   if odd length and even length
# myList = [2,1,3,5,4,7]
# myList.sort()
# print(myList)
# length = len(myList)
# if length % 2 == 1:
#      print(myList[length//2])
# else : 
#     n1 = myList[length//2]
#     n2 = myList[(length-1)//2]
#     print((n1 + n2)/2)


#  ============== mode ===============

myList = [1,2,3,1,4,5,1,3,2,2,2]

dic = {}

for i in myList:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)
maxNumber = 0
maxChar = ""
for char in dic:
    if dic[char] > maxNumber:
        maxNumber = dic[char]
        maxChar = char

print(maxChar)
print(maxNumber)