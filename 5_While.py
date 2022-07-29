#1075 RESTO DOIS
N = int(input("N:"))
for i in range(1,10001):
    res = i%N
    if res == 2:
        print(i)


#1078 TABUADA
num = int(input("N:"))
for i in range(1,11):
    if num >2 and num<=1000:
        soma = num * i
        print(i,"x",num,"=",soma)


#1146 SEQUENCIAS CRESCENTES
num = 1
while num != 0:
    num = int(input("\nN:"))
    for i in range(1,num+1):
        print(i, end = ' ')


#1134 TIPO COMBUSTIVEL
alcool = 0
diesel = 0
gasolina = 0
num=0
while num != 4:
    num = int(input("N:"))
    if num == 1:
        alcool += 1
    elif num == 2:
        gasolina += 1
    elif num == 3:
        diesel += 1
    
print("MUITO OBRIGADA!\nAlcool:",alcool,"\nGasolina:",gasolina,"\nDiesel:",diesel)


#1101 SEQUENCIA DE NUMEROS E SOMA
m = 1
n = 1
while m > 0 and n > 0:
    soma = 0
    m = int(input("m:"))
    n = int(input("n:"))
    if m > n:
        for i in range(n,m+1):
            soma += i
            print(i, end = ' ')
    else:
        for i in range(m,n+1):
            soma += i
            print(i, end = ' ')
    print("Sum =",soma)


#1113 CRSCENTE E DESCRECENTE
x = 0
y = 1
while x != y:
    x = int(input("X:"))
    y = int(input("Y:"))
    if x > y:
        print("decrescente")
    elif y > x:
        print("crescente")


#1099 SOMA DE IMPARES CONSECUTIVOS II??????????????????????SOMA
n = int(input("Quantidade de linhas:"))
cont = 0
while cont != n:
    x,y = [int(x) for x in input("").split()]
    cont +=1
    soma = 0
    maior = 0
    if x<y:
        for i in range(x+1,y):
            impar = i%2
            if impar != 0:
                soma+= i
    if y<x:
          for i in range(y+1,x):
            impar = i%2
            if impar != 0:
                soma+= i
    print(soma)

#1021 NOTAS E MOEDAS
num = float(input("Valor:"))
while num != 0:
    
    num = int(num*100)
    resto = 0
    restC = 0
    restL = 0
    restXX= 0
    restX= 0
    restV= 0
    restII= 0
    restI = 0
    restl= 0
    restxx= 0
    restx= 0
    restv= 0
    resti= 0

    if num <= 10000:
        restC = num//10000
        resto = num%10000
    if resto <= 10000:
        restL = resto//5000
        resto = num%5000
    if resto <= 5000 and resto >=2000:
        restXX = resto//2000
        resto = resto%2000
    if resto < 2000 and resto >=1000:
        restX = resto//1000
        resto = num%1000
    if resto < 1000 and resto >=500:
        restV = resto//500
        resto = num%500
    if resto < 1000 and resto >= 200:
        restII = resto//200
        resto = resto%200
    if resto >= 100:
        restI = resto//100
        resto = resto%100
    if resto <= 100 and resto >=50:
        restl = resto//50
        resto = num%50
    if resto <= 50 and resto >=25:
        restxx = resto//25
        resto = resto%25
    if resto < 25 and resto >=10:
        restx = resto//10
        resto = num%10
    if resto < 10 and resto >=5:
        restv = resto//5
        resto = resto%5
    if resto < 5 and resto >= 1:
        resti = resto//1
        resto = resto%1
            
            
    print("NOTAS:\n",restC,"nota(s) de R$ 100.00\n", restL,"nota(s) de R$ 50.00\n", restXX,"nota(s) de R$ 20.00\n", restX,"nota(s) de R$ 10.00\n", restV,"nota(s) de R$ 5.00\n", restII,"nota(s) de R$ 2.00\nMOEDAS:\n", restI,"moeda(s) de R$ 1.00\n", restl,"moeda(s) de R$ 0.50\n", restxx,"moeda(s) de R$ 0.25\n", restx,"moeda(s) de R$ 0.10\n", restv,"moeda(s) de R$ 0.05\n", resti,"moeda(s) de R$ 0.01\n")
    num = float(input("Valor:"))
    
 
#1247 GUARDA COSTEIRA
n = int(input("Quantos testes?"))
for i in range(n):
    d, vf, vg = [int(x) for x in input("").split()]
    if vg >= ((d**2)+(vf**2))**0.5:
        print("S")
    else:
        print("N")
 

#1708 VOLTA
x = int(input("X:"))
y = int(input("Y:"))
total = 0
volta = 1
while total != x:
    volta += 1
    sobra = y - x
    total += sobra
    if total >= x:
        print(volta)
        break


#2418 CARNAVAL
n = int(input("nota:"))
menor = maior = n
cont = 0
soma = 0
if n >= 5  and n<=10:
    while cont != 6:
        cont += 1
        soma += n
        if n >= maior:
            maior = n
        elif n<=menor:
            menor= n
        if cont == 5:
            break
        n = int(input("nota:"))
    print("Média:",(soma-menor-maior)/3)
else:
    print("valor não permitido!")


#2247 COFRINHO DA VÓ VITORIA
n = int(input("N de teste:"))
soma= 0
cont=0
while cont !=n+1:
    if n == 0:
        break
    elif cont<n:
        cont +=1
        j,z= input("J , Z:").split()
        nj = int(j)
        nz = int(z)
        res = nj - nz
        soma+= res
        print (cont, res , soma)
    elif cont == n:
        n = int(input("N de teste:"))
        cont = 0


#2187 BITS TROCADOS
import math

v = int(input("valor:"))
i = 50
j = 10
k = 5
l = 1
while v != 0:
    resti=0
    restj=0
    restk=0
    restl=0
    if v >= i:
        resti = v/i
        resto = v%i
        if resto <= i:
            restj = resto/j
            resto = v%j
        if resto <= j and resto >=k:
            restk = resto/k
            resto = v%k
            if resto < k:
                restl = resto/l
        if resto < k:
                restl = resto/l
        
    elif v < i and v >=j:
        restj = v/j
        resto = v%j
        if resto <= j and resto >=k:
            restk = resto/k
            resto = v%k
            if resto < k:
                restl = resto/l
        if resto < k:
                restl = resto/l
            
    elif v <= j and v >=k:
        restk = v/k
        resto = v%k
        if resto < k:
            restl = resto/l
            
    elif v < k:
        restl = v/l
        
    print(math.floor(resti), math.floor(restj), math.floor(restk), math.floor(restl))
    v = int(input("valor:"))


#2376 COPA DO MUNDO
for partida in range(15):
    m,n = [int(x) for x in input("").split()]
    if n >= 0 and n <= 20 and m != n and m >= 0 and m <= 20:
        resultado = m - n
        if resultado > 0:
            if partida == 0:
                time1 = "A"
                print("A")
            if partida == 1:
                time2 = "C"
                print("C")
            if partida == 2:
                time3 = "E"
                print("E")
            if partida == 3:
                time4 = "G"
                print("G")
            if partida == 4:
                time5 = "I"
                print("I")
            if partida == 5:
                time6 = "K"
                print("K")
            if partida == 6:
                time7 = "M"
                print("M")
            if partida == 7:
                time8 = "O"
                print("O")
            if partida == 8:
                time9 = time1
                print(time9)
            if partida == 9:
                time10 = time3
                print(time10)
            if partida == 10:
                time11 = time5
                print(time11) 
            if partida == 11:
                time12 = time7
                print(time12)
            if partida == 12:
                time13 = time9
                print(time13) 
            if partida == 13:
                time14 = time11
                print(time14)
            if partida == 14:
                time15 = time13
                print(time13)
                
        else:
            if partida == 0:
                time1 = "B"
                print("B")
            if partida == 1:
                time2 = "D"
                print("D")
            if partida == 2:
                time3 = "F"
                print("F")
            if partida == 3:
                time4 = "H"
                print("H")
            if partida == 4:
                time5 = "J"
                print("J")
            if partida == 5:
                time6 = "L"
                print("L")
            if partida == 6:
                time7 = "N"
                print("N")
            if partida == 7:
                time8 = "P"
                print("P")
            if partida == 8:
                time9 = time2
                print(time9)
            if partida == 9:
                time10 = time4
                print(time10)
            if partida == 10:
                time11 = time6
                print(time11) 
            if partida == 11:
                time12 = time8
                print(time12)
            if partida == 12:
                time13 = time10
                print(time13) 
            if partida == 13:
                time14 = time12
                print(time14)
            if partida == 14:
                time15 = time14
                print(time15)
                
               
#2229 DOBRADURA
n=0
while n != -1:
    n = int(input("N:"))
    if n>=0 and n<=15:
        totalpapel = (2**n + 1)**2
        print("Teste 1\n"totalpapel"\n ")