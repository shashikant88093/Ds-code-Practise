# hash map inpmelention in python is dictoinary

myDict = {
    "name":"shashikant",
    "age":28,
    "contact":8789750652
}

print(myDict.get("name"))
# all values
for key in myDict.values():
    print(key)
# key and value both

for key,value in myDict.items():
    print(key,value)

print(myDict.values())
print(myDict.keys())
print(myDict.items())
