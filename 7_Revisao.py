#1017 GATO DE COMBUSTIVEL
tempo, km = [int (x) for x in input().split()]
litros = (km*tempo)/12
print(round(litros,3))

#1046 TEMPO DE JOGO
soma=0
h1, h2=[int(x) for x in input().split()]
if h1 >= h2:
    soma = (24 - h1) + h2
if h2>h1:
    soma = h2 - h1
    
print ("O JOGO DUROU ",soma,"HORA(S)")

#2927 IMPREVISTOS NATALINOS
A, C, X, Y= [int(x) for x in input().split()]
total = C - X -Y
if A < total:
    print("Igor feliz!")
if X > Y:
    print("Caio, a culpa é sua!")
else:
    print("Igor bolado")

#2434 SALDO DO VOVO
n, s= [int(x) for x in input().split()]
menor = s
if n>=1 and n<=30:
    if (-10)**3<= s and s <=(10)**3:
        for i in range(n):
            m = int(input("valor:"))
            s = s + m
            if s < menor:
                menor = s
        print("menor valor do mês:",menor)

#2116 DIVERSAO DOS ALUNOS
n , m = [int(x) for x in input().split()]
for i in range(1 ,n+1):
    cont = 0
    for divisor in range(1 , i+1):
        if i%divisor == 0:
            cont+=1
    if cont == 2:
        p1 = i

for i in range(1 ,m+1):
    cont = 0
    for divisor in range(1 , i+1):
        if i%divisor == 0:
            cont+=1
    if cont == 2:
        p2 = i
    
print(p1*p2)