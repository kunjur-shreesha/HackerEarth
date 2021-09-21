t = int(input())
for i in range(t):
    count = 0
    sum1 = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(len(a)):
        if a[i] + sum1 <= n:
            sum1 += a[i]
            count += 1
    print(count)
