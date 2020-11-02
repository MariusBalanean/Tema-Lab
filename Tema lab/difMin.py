def citire():
    n = int(input())
    lista_str = input()
    lista_num = lista_str.split(" ")
    for i in range(0, n):
        lista_num[i] = int(lista_num[i])

    return lista_num


def perechi(lista):
    min = abs(lista[0] - lista[1])
    for i in range(0, len(lista)-1):
        if abs(lista[i] - lista[i+1]) <= min:
            min = abs(lista[i] - lista[i+1])
            x = i
            y = i+1
    print(lista[x], lista[y])



lista = citire()
perechi(lista)

