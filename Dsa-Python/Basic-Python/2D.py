# 2D list
# twod = [[1,2,3],[4,5,6],[7,8,9]] 
# print(twod[0][1],"array")
# print(twod[1][1],"array")
# print(twod[2][1],"array")

# take input as 3 * 3 and print from 1 to 9

# n = int(input())
# grid = []
# for i in range(n):
#     grid.append([int(item) for item in input().split()]) 
# print(grid)

# n = int(input())

# grid = []

# for i in range(n):
#     grid.append([int(item) for item in input().split()])

# print(grid,"grid")

# dia = []
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             dia.append(grid[i][j])

# print(dia)
# output [1,5,9]

#  input 1 2 3
      #  4 5 6
      #  7 8 9
# output 1 4 7
      #  2 5 8
      #  3 6 9

# first approach 
#  draw back need to iterate all 
# input = [[1,2,3],[4,5,6],[7,8,9]]
# grid = []
# for i in range(len(input)):
#     new_row = []
#     for j in range(len(input)):
#         new_row.append(input[j][i])
#     grid.append(new_row)

# print(grid)
        
# Second approach
# reduce loop 
input = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(input)):
    for j in range(len(input)):
        if j > i:
            temp = input[j][i]
            print(temp,"temp")
            input[j][i] = input[i][j]
            print(input[j][i],"input[j][i]")
            print(input[i][j],"input[i][j]")

            input[i][j] = temp
print(input)