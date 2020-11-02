from audioop import reverse


def impare(n):
    lista = []
    for i in range(1, 2*n, 2):
        lista.append(i)
    return lista


n = int(input())
lista = impare(n)
print(lista[::-1])
