n=int(input())
arr=list(map(int,input().split()))
lst=[]
A=arr[:len(arr)//2]
B=arr[len(arr)//2:]
for i in A:
    while (i >= 10 ):
        i = i // 10
    lst.append(i)
for i in B:
    j=i%10
    lst.append(j)
t=int("".join((map(str,lst))))

if(t%11==0):
    print("OUI")
else:
    print("NON")