def suma(n):
    s = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            s = s - i* (i + 1)
        else:
            s = s + i * (i + 1)

    return s

n = int(input())
print("Rezultatul este", suma(n))