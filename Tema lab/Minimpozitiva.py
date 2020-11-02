def citire():
    lista_str = input()
    lista_num = lista_str.split(" ")
    for i in range(0, len(lista_num)):
        lista_num[i] = int(lista_num[i])

    return lista_num


def min(lista):
    min = lista[0]
    for num in lista:
        if num > 0 and num <= min:
            min = num
    return min


lista = citire()
if min(lista):
    print (min(lista))
else:
    print("NU EXISTA")
