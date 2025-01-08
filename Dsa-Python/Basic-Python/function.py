# function add a + b

def add(a,b):
    print(a+b)

n = int(input())
m = int(input())
add(n,m)


# pass multiple argument in funcrion with pass *args
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)                  

add(1,2,3,4,5,6,7,8,9,10)
add(1,2)