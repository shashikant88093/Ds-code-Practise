# factorial using recursion

# def fac(n):
#     if n==0 or n==1:
#         return 1
#     return n * fac(n-1)

# ans = fac(int(input()))

# print(ans)


# input n
# output 1 1 2 3 5 8 13


def rec(n):
    if n==1 or n==2:
        return 1
    return rec(n-1) + rec(n-2)
ans = rec(6)
print(ans)