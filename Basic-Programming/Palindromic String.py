def rev(x):
    return x[::-1]
str1=input()
str2=rev(str1)
if str1==str2:
    print("YES")
else:
    print("NO")