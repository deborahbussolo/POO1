valores = []
matrix = []
media = 0
soma = 0
n = 12
L = int(input('linha:'))
T = input("Soma ou Media? [S/M]").upper()
for l in range(n):
    linha = []
    for e in range(n):
        valor = float(input("valor:"))
        linha.append(valor)
    matrix.append(linha)
print(matrix)


for i in matrix[L]:
    soma +=i

if T == 'S':
    print(soma)
  
elif T == 'M':
    media = soma/len(linha)
    print(media)