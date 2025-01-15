
# asc key
# A = 65 to Z = 90
# a = 97 to z = 122

#  ==================================== ASC Value ============================================

#  to print asc value use ord method

x = "ShashikantKumar"
ans = ""
for i in range(len(x)):
    if ord(x[i]) > 90:
        ans += x[i]

x = ans
print(x)