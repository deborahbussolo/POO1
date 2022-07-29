n = int(input("Número de elementos: "))
lista = []
for i in range(n):
    x = int(input("Digite um elemento: "))
    lista.append(x)
k = int(input("Digite um multiplicador: "))
for i in range(n):
    lista[i] = lista[i]*k
print(lista)

