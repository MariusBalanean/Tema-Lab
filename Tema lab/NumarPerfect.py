n = int(input())
s = 0
for i in range(1, n+1):
    if n % i == 0:
        s = s + i

if s == 2*n:
    print(n, "este perfect")
else:
    print(n, "nu este pefect")

