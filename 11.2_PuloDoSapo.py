direita = 0
esquerda = 0
posicoes = set()
pedras, sapos = [int(x) for x in input().split()]
for sapo in range(sapos):
    inicial, distancia = [int(x) for x in input().split()]
    pulos = 0
    while inicial + distancia * pulos <= pedras:
        posicoes.add(inicial + distancia * pulos)
        pulos+=1
    pulos = 0
    while inicial - distancia * pulos > 0:
        posicoes.add(inicial - distancia * pulos)
        pulos+=1
posicoes = list(posicoes)
for i in range(1, pedras+1):
    if posicoes.count(i) > 0:
        print("1")
    if posicoes.count(i) == 0:
        print("0")


