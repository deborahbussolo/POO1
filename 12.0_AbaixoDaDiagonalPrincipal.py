valores = []
matrix = []
media = 0
soma = 0
div = 0
n = 12
T = input("Soma ou Media? [S/M]").upper()
for l in range(n):
    linha = []
    for e in range(n):
        valor = float(input("valor:  "))
        linha.append(valor)
    matrix.append(linha)
    print(matrix)
for x in range(len(matrix)):
    for e in range(len(matrix[x])):
        if e < x:
            soma += matrix[x][e]
            div += 1
if T == 'S':
    print(soma)
  
elif T == 'M':
    media = soma/div
    print(media)
    
