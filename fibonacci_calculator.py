n = int(input('digite um numero: '))

lista = [0, 1]

for i in range(n-1):
    num = lista[i+1] + lista[i]
    lista.append(num)
print(lista)