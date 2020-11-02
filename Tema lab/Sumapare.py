def suma(n):
    s = 0
    for i in range(1, n+1):
        s = s+i
    return 2*s

n = int(input())
print ("Suma este", suma(n))