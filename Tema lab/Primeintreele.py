def lista():
    lista_str = input()
    lista_num = lista_str.split(" ")
    for i in range(0, len(lista_num)):
        lista_num[i] = int(lista_num[i])
    return lista_num


lista_num = []
lista_num = lista()
a = lista_num[0]
b = lista_num[1]
k = 0
n = 0
if a > b:
    n = b
else:
    n = a
for i in range(2, n+1):
    if a % i == 0 and b % i == 0:
        print("NOPIE")
        k = i
        break
if k == 0:
    print("PIE")


