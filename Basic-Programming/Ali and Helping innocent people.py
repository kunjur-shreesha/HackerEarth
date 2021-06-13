n=[x for x in input()]
v="AEIOUY"
i1=i2=i3=i4=i5=0
for i in n:
    if (int(n[0]) + int(n[1])) % 2 == 0:
        i1=1

    if (int(n[3])+int(n[4]))%2==0:
        i3=1
    if (int(n[4]) + int(n[5])) % 2 == 0:
       i4=1
    if (int(n[7]) + int(n[8])) % 2 == 0:
        i5=1
if((i1  and i3 and i4 and i5)==1 and n[2] not in v):
    print("valid")
else:
    print("invalid")