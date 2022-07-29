n = int(input())
for i in range(n):
    cont = 0
    respostas = []
    respostas = [int(x) for x in input().split()][0:5]
    for e in respostas:
        if e < 225:
            posicao = respostas.index(e)
            cont += 1
    if posicao == 0 and cont == 1:
        print("A")
    elif posicao == 1 and cont == 1:
        print("B")
    elif posicao == 2 and cont == 1:
        print("C")
    elif posicao == 3 and cont == 1:
        print("D")
    elif posicao == 4 and cont == 1:
        print("E")
    else:
        print("*")
    
