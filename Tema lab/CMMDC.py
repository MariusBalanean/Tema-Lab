def lista():
    lista_str = input()
    lista_num = lista_str.split(" ")
    for i in range(0, len(lista_num)):
        lista_num[i] = int(lista_num[i])
    return lista_num

lista_num = []
lista_num = lista()
n = lista_num[0]
m = lista_num[1]
while(n != m):
    if(n > m):
        n -= m
    else:
        m -= n
if n == 0 and m == 0:
    print(-1)
else:
    print(n)
