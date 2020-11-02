n = int(input())
max = 0
i = 0
while n:
    i = n % 10
    n = n // 10
    if i % 2 and i >= max:
        max = i

print(max)