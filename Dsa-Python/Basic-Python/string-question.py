#   palindrom

name = input()

isPlandrom = True

for i in range(len(name)):
    if name[i] != name[len(name) - i -1]:
        isPlandrom= False

if(isPlandrom):
    print("is palindrom")
else:
    print("not palindrom")