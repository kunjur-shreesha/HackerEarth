n=int(input())
temp=[x for x in input()]
t="".join(temp)
if "HH" in t:
    print("NO")
else:
    for i in range(n):
        if(temp[i]=='.'):
         temp[i]='B'
    print("YES")
    print("".join(temp))