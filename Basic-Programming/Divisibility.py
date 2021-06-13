n=int(input())
arr=list(map(int,input().split()))
lst=[]
for i in arr:
    j=i%10
    lst.append(j)
t=int("".join((map(str,lst))))
if(t%10==0):
    print("Yes")
else:
    print("No")