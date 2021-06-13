def fact(x):
    if x>=1:
        return x*fact(x-1)
    else:
        return 1
n=int(input())
print(fact(n))