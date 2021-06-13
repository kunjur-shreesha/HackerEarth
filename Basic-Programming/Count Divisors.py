temp =[x for x in input().split()]
l,r,k=temp[0:]
count=0
for i in range(int(l),int(r)+1):
    if i%int(k)==0:
        count+=1
print(count)


