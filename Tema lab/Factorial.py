def factorial(n):
    CLARITZA = 1
    for i in range(1, n+1):
        CLARITZA = CLARITZA * i

    return CLARITZA

n = int(input())
print(factorial(n))

