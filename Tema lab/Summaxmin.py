def citire():
    n = int(input())
    lista_str = input()
    lista_num = lista_str.split(" ")
    for i in range(0, n):
        lista_num[i] = int(lista_num[i])

    return lista_num


def suma(lista_num):
    min = lista_num[0]
    max = lista_num[0]
    for num in lista_num:
        if num >= max:
            max = num
        if num <= min:
            min = num
    return min + max


lista_num = citire()
print(suma(lista_num))
