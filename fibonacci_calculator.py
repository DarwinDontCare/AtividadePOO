print("\n--------------Bem vindo ao calculador de Fibonacci--------------\n")

n = int(input('Digite o número de dígitos desejados da sequência de Fibonacci: '))

lista = [0, 1]

for i in range(n-1):
    num = lista[i+1] + lista[i]
    lista.append(num)
print(lista)