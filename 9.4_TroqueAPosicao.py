#print([i for i in range(20)][::-1])
lista=[i for i in range(20)]
lista2 = lista[:]
for i in range(len(lista)):
    lista[i]= lista2[-i]
for i in range(len(lista)):
    lista[i-1]=lista[i]
lista[18]=1   
   
print(lista)
