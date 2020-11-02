n = int(input())
c = 0
for i in range(2, n+1, 2):
    if n % i == 0:
        c = c + 1
print(c)