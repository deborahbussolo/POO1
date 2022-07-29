#1003 
As = int(input("Numero que deseja somar: "))
Bs = int(input("Numero que deseja somar: "))
soma = As + Bs
print("Soma :" , soma)

#1004 
Ap = int(input("Numero que deseja achar o produto: "))
Bp = int(input("Numero que deseja achar o produto: "))
prod = Ap*Bp
print("O produto é :" , prod)

#1005 
Am = float(input("Numero que deseja saber a media: "))
Bm = float(input("Numero que deseja saber a media: "))
media = (Am*3.5+Bm*7.5)/11
print("A media dos dois numeros é: " , round( media , 5))

#1006 
Ap= float(input("n1: "))
Bp= float(input("n2: "))
Cp= float(input("n3: "))
media = (Ap*2+Bp*3+Cp*5)/10
print("media é: " , media )

#1007 
A = int(input("Valor 1: "))
B = int(input("Valor 2: "))
C = int(input("Valor 3: "))
D = int(input("Valor 4: "))
diferenca = A*B - C*D
print("DIFERENÇA = " , diferenca )

#1008
funcionario = int(input("Qual o seu numero? "))
valorh = float(input("Quanto recebe por hora? "))
hora = int(input("Quantas horas trabalha? "))
total = valorh*hora
print("NUMERO =  " , funcionario)
print("SALARIO = R$ " , round(total , 2))


#2374
N = int(input("Pressão desejada: "))
M = int(input("Pressão lida: "))
if 1 <= N <= 40:
    if 1 <= M <= 40:
        total = N - M
else:
     print ("problema com a contagem")
print(total)

#2413
t = int(input("Número: "))
if 1 <= t <= 100:
    total = (t * 2)*2
else:
    print ("valor não encontrado")
print (total)

#1012
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
triangulo = (A*C)/2
circulo = (3.14159*C)*(3.14159*C)
trapezio = (A+B)*C/2
quadrado = B^2
retangulo = A * B
print ("TRIANGULO: " , triangulo)
print ("CIRCULO: " ,  round(circulo, 2))
print ("TRAPEZIO: " , trapezio)
print ("QUADRADO: " , quadrado)
print ("RETANGULO: " , retangulo)

#1020
total= int(input("Total de dias: "))
anos=  int(total /365)
resto = total - (anos * 365)
meses = int(resto /30)
dias = resto - meses *30
print("anos: " , anos)
print("meses: " , meses)
print("dias: " , dias)

#1019
total= int(input("Total de segundos: "))
hora=  int(total /3600)
resto = total - (hora * 3600)
minutos = int(resto /60)
segundos = resto - minutos *60
print("horas: " , hora)
print("minutos: " , minutos)
print("segundos: " , segundos)

#1015 
x1 , y1 = input("Escolha dois numeros: ").split()
x1 = int(x1)
y1 = int(y1)
x2 , y2 = input("Escolha mais dois numeros: ").split()
x2 = int(x2)
y2 = int(y2)
distancia = ((x2 - x1)**(2) + (y2 - y1)**(2)) **(1/2)
print( round(distancia , 4))

#1017
km = int(input("velocidade: "))
hora = int(input("duração: "))
litro = (hora*km)/12
print ("total de litros gastos: " , round(litro , 3))

#1014
km = int(input("distancia em km: "))
combustivel = int(input("Total de combustivel gasto: "))
media = km/combustivel
print(round(media, 3) , "km/l")

#1009
nome = input("Seu nome: ")
fixo = int(input("Salario fixo: "))
vendas = int(input("Total de vendas: "))
desconto = vendas*0.15
total = fixo + desconto
print ("total", total )