#ESQUERDA, VOLVER
while True:
    direcao = 'NLSO'
    x = 0
    n = int(input())
    if n == 0:
        break
    else:
        comando = input().upper()
        comando [:n]
    for i in range(n):
        if comando[i] == 'D':
            x+=1
        if comando[i] == 'E':
            x-=1
    print(direcao[x])


#2813 EVITANDO CHUVA
n = int(input("N:"))
c= 0
e = 0
Dant = Nant = ''
for i in range(n):
    d,n =[x for x in input("D,N:").split()]
    if d == 'sol' and n == 'chuva' and i == 0:
        e += 1
    if d == 'chuva' and n == 'sol' and i == 0:
        c += 1
    if Dant + Nant == d + n:
        if d == 'chuva' and n=='sol':
            c += 1
        if d == 'sol' and n== 'chuva':
            e+= 1
        
    else:
        Dant = d
        Nant = n

print(c,e)


#1192 O JOGO MATEMATICO DE PAULA
n = int(input("N:"))
for i in range(n):
    soma= 0
    n1 ,letra, n2=[str(x) for x in input().split()]
    n1 = int(n1)
    n2 = int(n2)
    if letra == letra.upper():
        soma = n2 - n1
    if letra == letra.lower():
        soma = n1 + n2
        if n1 == n2:
            soma = n1*n2
    print(soma)


#1168 LED
n = int(input("N:"))
led1 = 2
led2 = 5
led3 = 5
led4 = 4
led5 = 5
led6 = 6
led7 = 3
led8 = 7
led9 = 6
led0 = 6
for i in range(n):
    v=input("")
    cont = 0
    for i in range(len(v)):
        if v[i]== '1':
            cont += led1
        if v[i]== '2':
            cont += led2
        if v[i]== '3':
            cont += led3
        if v[i]== '4':
            cont += led4
        if v[i]== '5':
            cont += led5
        if v[i]== '6':
            cont += led6
        if v[i]== '7':
            cont += led7
        if v[i]== '8':
            cont += led8
        if v[i]== '9':
            cont += led9
        if v[i]== '0':
            cont += led0
            
    print(cont, "leds")


#1094 EXPERIENCIA
num = int(input("N:"))
r = c = s = soma = 0
for i in range(num):
    n, tipo = [str(x) for x in input().split()]
    n = int(n)
    soma += n
    if tipo == 'C':
        c += n
    if tipo == 'R':
        r += n
    if tipo == 'S':
        s += n
perC = (c*100/soma)
perR = (r*100/soma)
perS = (s*100/soma)
print(c,s,r, soma , perC, perS, perR)


#6 DIVISIVEIS POR 3
while True:
    n ,m= [int(x) for x in input().split()]
    m = str(m)[:n]
    soma = 0
    for i in range(n):
        soma += int(m[i])
        
    if soma%3 == 0:
        print(soma, "sim")
    else:
        print(soma, "não")
    
    R = input("Quer continuar?[S,N]").upper()
    if R == 'N':
        break
    
print(soma)