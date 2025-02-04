# selection sort

# input array = [1, 4, 2, 3, 5]

# output array = [1, 2, 3, 4, 5]


n = int(input())

myList = [int(ele) for ele in input().split()]

for i in range(n):
    # print(i,"i")
    minValue =i
    for j in range(i,n):
            # print(j,"j out")
            print(myList[minValue],"myList[minVal]")
            print(myList[j],"myList[j]")
            if myList[minValue] > myList[j]:
                minValue = j
                # print(j,"j in")
                print(myList,"in 2nd loop")
    temp = myList[minValue]
    # print(temp,"temp")
    myList[minValue] = myList[i]
    myList[i] = temp
    print(myList,"in 1st loop")




print(myList)