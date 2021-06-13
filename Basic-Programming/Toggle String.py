inp=input()
for i in inp:
    if(i.isupper()):
        i=i.lower()
        print(i,end="")
    else:
       i=i.upper()
       print(i,end="")