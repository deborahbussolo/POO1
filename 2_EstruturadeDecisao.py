#1)Emprestimo da casa
valorCasa = float(input("Qual é o valor da casa? R$"))
salario = float(input("Quanto você recebe de salário? R$"))
anos = float(input("Em quantos anos pretende pagar? "))

valorMensal = valorCasa/(anos*12)

if valorMensal > (salario*0.3):
    print("Emprestimo negado!")
else: 
    print("Emprestimo aprovado!")


#2)Cartão
valorProduto = float(input("Qual é o valor do produto: R$"))

print("Opções de pagamento:\n 1- A vista\n 2- 1x no cartão\n 3- 2x no cartão\n 4- 3x ou mais no cartão ")
opcao = int(input("Qual é o número da opção desejada: "))

if opcao == 1:
    valorFinal = valorProduto*0.9
    print("O total à pagar será R$", valorFinal)        
elif opcao == 2:
    valorFinal = valorProduto*0.95
    print("O total à pagar será R$", valorFinal)
elif opcao == 3:
    parcela = valorProduto/2 
    print("O total à pagar será 2x de R$", parcela)
elif opcao == 4:
    numParcelas = int(input("Quantas parcelas deseja? "))
    if numParcelas == 1:
        opcao = 2    
    elif numParcelas == 2:
        opcao = 3     
    elif numParcelas >= 3:
        valorFinal = valorProduto * 1.2 
        valorParcela = valorFinal/numParcelas
        print("O total à pagar será 4x de R$", valorParcela)


#3)IMC
peso = float(input("Qual é o seu peso em kg: "))
altura = float(input("Qual é a sua altura em metros: "))

imc = peso/(altura*altura)

if imc <= 18.5:
    print("Você está abaixo do peso")
elif imc > 18.5 and imc <= 25:
    print("Você está no peso ideal")  
elif imc > 25 and imc <= 30:
    print("Você está com sobrepeso")
elif imc > 30 and imc <= 40:
    print("Você está com obesidade")
elif imc > 40:
    print("Você está com obesidade mórbida")


#1035 Teste de Seleção 1
print("Insira 4 números inteiros:")
a = int(input("1° número: "))
b = int(input("2° número: "))
c = int(input("3° número: "))
d = int(input("4° número: "))

soma1 = c + d
soma2 = a + b
if b>c and d>a and soma1 > soma2 > 0 and (a%2) == 0:
    print("Valores aceitos!")
else:
    print("Valores não aceitos!")
     

#1037 Intervalos 
num = float(input('Insira um valor: '))

if 0 <= num <= 25:
    print('Intervalo [0,25]')
elif 25 <= num <= 50:
    print('Intervalo [25,50]')
elif 50 <= num <= 75:
    print('Intervalo [50,75]')
elif 75 <= num <= 100:
    print('Intervalo [75,100]')
else:
    print('Fora de intervalo')


#1038 Lanches
codigo = int(input('Insira o código: '))
x = int(input('Insira a quantidade: '))

if codigo==1:
    total = 4 * x
    print("Total: R$" , round(total, 2))
elif codigo==2:
    total = 4.5 * x
    print("Total: R$" , round(total, 2))
elif codigo==3:
    total = 5 * x
    print("Total: R$" , round(total, 2))
elif codigo==4:
    total = 2 * x
    print("Total: R$" , round(total, 2))
elif codigo==5:
    total = 1.5 * x
    print("Total: R$" , round(total, 2))
else:
    print('Código não encontrado!')


#1040 Média3
a = float(input('1° nota: '))
b = float(input('2° nota: '))
c = float(input('3° nota: '))
d = float(input('4° nota: ')) 

media = float(((a*2)+(b*3)+(c*4)+(d))/10)
notaExame = 0

if media >= 7:
    print("Media:", media ,"\nAluno aprovado!")
elif media <= 5:
    print("Media:", media ,"\nAluno reprovado!")
elif 6.9 > media > 5:
    print("Media:", media,"\nAluno em exame!")
    nota = float(input('Insira a nota do exame: '))
    notaExame = nota
    
mediaFinal=(media + notaExame)/2

if mediaFinal >= 5:
    print("Media final:", mediaFinal ,"\nAluno aprovado!")
elif mediaFinal <= 4.9:
    print("Media final:", mediaFinal ,"\nAluno reprovado!")
else:
    print('Presentation Error!')
    

#1043 Triângulo
a = float(input('Insira o valor a: '))
b = float(input('Insira o valor b: '))
c = float(input('Insira o valor c: '))

perimetro= a+b+c
area= ((a+b)*c)/2

if (b-c)< a <(b+c) and (a-c)< b <(a+c) and (a-b)< c <(a+b):
    print("Perimetro: ", round(perimetro,1))
else:
    print("Area: " , round(area,1))
    

#1044 Múltiplos 
num1 = int(input('1°  número: '))
num2 = int(input('2° número: '))

if num1%num2 ==0:
    print('São múltiplos!')
elif num2%num1 ==0:
    print('São múltiplos!')
else:
    print('Não são múltiplos!')
    
  
#1045 Tipos de Triângulos 
lado1 = float(input("Informe o 1° lado: "))
lado2 = float(input("Informe o 2° lado: "))
lado3 = float(input("Informe o 3° lado: "))

print("lado 1: ", lado1)
print("lado 2: ", lado2)
print("lado 3: ", lado3)
if lado1 >= (lado2 + lado3):
    print("Não forma um triangulo")
    exit()
if (lado1*lado1) == ((lado2*lado2) + (lado3*lado3)):
    print("Triangulo retangulo")
if (lado1*lado1) > ((lado2*lado2) + (lado3*lado3)):
    print("Triangulo obtusangulo")
if (lado1*lado1) < ((lado2*lado2) + (lado3 * lado3)):
    print("Triangulo acutangulo")
if lado1 == lado2 and lado2 == lado3:
    print("Triangulo equilatero")
if (lado1 != lado2 and lado2 == lado3) or (lado1 == lado2 and lado2 != lado3) or (lado1 != lado2 and lado1 == lado3):
    print("Triangulo isoceles")


#2339 Aviões de Papel
c = int(input("Qual é o número de competidores:? "))
p = int(input("Quantas folhas foram compradas? "))
f = int(input("Quantas folhas são usadas por aluno? "))
if 1 <= (c and p and f) <= 1000:
    if c * f <= p:
        print("S")
    else:
        print("N")

#1049 Animal
a = (input('Insira o primeiro nome: '))
b = (input('Insira o segundo nome: '))
c = (input('Insira o terceiro nome '))

if a =="vertebrado" and b =="ave" and c =="carnivoro":
    animal ="aguia"

if a =="vertebrado" and b =="ave" and c =="onivoro":
    animal ="pomba"

if a =="vertebrado" and b =="mamifero" and c =="onivoro":
    animal ="homem"

if a =="vertebrado" and b =="mamifero" and c =="herbivoro":
    animal ="vaca"

if a =="invertebrado" and b =="inseto" and c =="hematofago":
    animal ="pulga"
    
if a =="invertebrado" and b =="inseto" and c =="herbivoro":
    animal ="lagarta"
    
if a =="invertebrado" and b =="anelideo" and c =="hematofago":
    animal ="sanguessuga"
    
if a =="invertebrado" and b =="anelideo" and c =="onivoro":
    animal ="minhoca"

print(animal)


# 2382 Sedex Marciano
l = int(input("Qual é a largura da caixa? "))
a = int(input("Qual é a altura da caixa? "))
p = int(input("Qual é a profundidade da caixa? "))
r = int(input("Qual é o raio da esfera? "))

d = r * 2
dcaixa = int((l and a and p) * 3**1/2) # formula D=a√3

if 1<=(l and a and p and r)<=1000 and d >= dcaixa:
#se o maior lado da caixa entrar na esfera, logo os lados menores entram também
    print("S")
else:
    print("N")
    
    
#Notas  
nota1=float(input("Nota 1 do aluno: "))
nota2=float(input("Nota 2 do aluno: "))
nota3=float(input("Nota 3 do aluno: "))

media = (nota1+nota2+nota3)/3

print("A média do aluno foi ", round(media, 1))

if media < 5:
    print("Reprovado!")
elif media >= 5 and media < 7:
    print("Em recuperação!")
elif media >= 7:
    print("Aprovado!")