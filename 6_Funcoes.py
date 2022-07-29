#1048 AUMENTO SALARIO
def aumentoSalario(valor):
    if 0<= valor <= 400:
        total= valor *1.15
    elif 400.01 <= valor <= 800:
        total = valor * 1.12
    elif 800.01 <= valor <= 1200:
        total = valor * 1.1
    elif 1200.01 <= valor <= 2000:
        total = valor * 1.07
    else:
        total = valor * 1.04
    print(f'Novo salário: {total:.2f}')
    print(f'Reajuste ganho: {total - valor:.2f}')
    print(f'Em percentual: {(total/valor)*100 - 100:.0f} %')
    
ok = aumentoSalario(2000)

#2057 FUSO HORARIO
def fuso_horario(partida, viagem, fuso):
    soma = partida + viagem + fuso
    if soma == 24:
        print('0')
    elif soma > 24:
        print(soma - 24)
    else:
        print(soma)

fh = fuso_horario(22, 6, -2)

#1150 ULTRAPASSANDO Z
def ultrapassando(X, Z):
    s = X
    while Z <= X:
        Z = int(input('Digite outro número: '))
    while s <= Z:
        s = s + 1
    print(X, Z, s)
ok = ultrapassando(21, 21)

#1154 MEDIA DE IDADES
def calcularSoma (num):
    soma = 0
    cont = 0
    while num > 0:
        num = int(input("Digite uma idade:"))
        if num>0:
            soma = soma + num
            cont += 1
            media = soma/cont
            
    print("Media:",round(media,2))

ok = calcularSoma (1)

#1064 POSITIVOS E MEDIA
def calcularMedia (num):
    positivo = 0
    soma = 0
    for i in range(0,6):
        num = int(input("Digite um numero:"))
        if num > 0:
            positivo += 1
            soma = soma + num
            media = soma/positivo
            
    print(positivo,"valores positivos\nMedia",round(media,2))

ok = calcularMedia (0)

#1115 QUADRANTE
def quadrante (x,y):
    while x !=0 and y!= 0:
        x = int(input("valor x:"))
        y = int(input("valor y:"))
        if x> 0 and y > 0:
            print("primeiro quadrante")
        elif x< 0 and y > 0:
            print ("segundo quadrante")
        elif x< 0 and y < 0:
            print ("terceira quadrante")
        elif x> 0 and y < 0:
            print ("quarta quadrante")
ok = quadrante (1, 1)

#2378 ELEVADOR
def elevador (s,n):
    n = int(input("Número de leitura do sensor:"))
    c = int(input("Capacidade maxima do elevador:"))
    cont =0
    saida = 0
    entrada = 0
    while cont != n:
        cont +=1
        s = int(input("pessoas sairam nesse andar:"))
        e = int(input("pessoas entraram nesse andar:"))
        saida = saida + s
        entrada = entrada + e
        soma = entrada - saida
        
    if soma > c:
        print("s")
    else:
        print("n")
    
ok = elevador(0,0)


#2409 COLCHÃO
def colchao(A,B,C):
    h , l = [int(x) for x in input("H,L:").split()]
    if B > h and C > h:
        n = print("N\nVocê deve comprar outro colchão")
        return n
    else:
        s = print("S\nParabens pela compra!")
        return s
    
A, B, C = [int(x) for x in input("A,B,C:").split()]
ok = colchao (A,B,C)


#CALCULO I
def media (aluno):
    melhornota = 0
    soma = 0
    for i in range (aluno):
        nota = float(input("Nota:"))
        if nota>melhornota:
            melhornota = nota
            soma += nota
    if melhornota>=5.75:
        print("Aprovado!")
    elif melhornota<5.75 and melhornota>=2.75:
        print("Em Recuperação")
    elif melhornota<2.75:
        print("Reprovado!")
    
    resultado = print("\nMedia da turma:", soma/5,"\nNota do melhor aluno:", melhornota)
    return resultado

ok = media(5)


#PAR E IMPAR - PS:descobri a melhor funcionalidade da função e return dps desse exemplo.
def isPair (num):
    if num%2 == 0:
        return True
    else:
        return False

countPar = countImpar = 0
for i in range (10):
    numero=int(input("n:")) 
    if isPair(numero):
        print("par")
        countPar +=1
    else:
        print("impar")
        countImpar +=1

print("pares:",countPar, "impares:", countImpar)


#NUMEROS PRIMOS
def primo(resto):
    for i in range(n):
        if resto == 2:
            return True
        else:
            return False
   
n=1
quant = 0
while n!=0:
    n = int(input("n:"))
    resto = 0
    for i in range(1 , n + 1):
        if n% i == 0:
            resto+=1
    if primo(resto):
        quant +=1
print(quant) 