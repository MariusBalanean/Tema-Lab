n = int(input())
i = 0
par = -1
if n == 0:
    print(0)
else:
    while n:
        i = n % 10
        n = n // 10
        if i % 2 == 0:
            par = i
            break

    print(par)

