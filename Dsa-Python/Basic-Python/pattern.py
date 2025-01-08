# input 2,5
# output 12345
#        12345

# n = int(input())
# m= int(input())

# for i in range(n):
#     for j in range(m):
#         print(j+1,end=" ")
#     print(" ")

# input n =5
# output 1
#        12
#        123
#        1234

# n = int(input())

# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     print(" ")

# input n = 5
# output        *
#             * *
#           * * *
#         * * * *
#       * * * * *

n = int(input())

for i in range(n):
    for k in range(n):
        if(k < n-(i+1)):
            print(" ",end="")
        else:
            print("*",end="")
    print(" ")
