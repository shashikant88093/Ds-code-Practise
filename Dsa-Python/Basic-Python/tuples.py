myTuple = (1,2,3,4,5,6,7,8,9,"shashikant")
#  we can't assign direct value to tuple so assign it by using list

mytuple = list(myTuple)
mytuple[0] = 23

myTuple = mytuple

print(myTuple)

# concact in tuple
a = (1,2,3)
b = (4,5)
a += b

print(a)