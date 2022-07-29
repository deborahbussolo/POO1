#1)Ano Bissexto
for i in range (2004, 2097):
    if i%4==0:
        print(i)

#2)Números impares
for i in range (1, 51):
    if i%2!=0:
        print (i)
        
#3)Melhor nota
melhorNota = 0
for i in range (5):
    nome= input("Nome: ")
    nota= float(input("Nota: "))
    valor= float(input("Mensalidade: "))
    if nota>melhorNota:
        melhorNota = nota
        aluno = nome
        mensalidade = valor
desconto = float (mensalidade*0.3)
total = mensalidade - desconto
print("Nome: ", aluno)
print("Nota: ", melhorNota)
print("Mensalidade total: ", mensalidade)
print("Mensalidade a pagar: ", total)

#4)Par e Impar
par = 0
impar = 0
for i in range(10):
    num = int(input("N:"))
    if num%2==0:
        par += 1
    else:
        impar += 1

print("Quantidade de numero par: ", par)
print("Quantidade de número impar: ", impar)

#5) Número primo
divisao = 0
num = int(input("Número inteiro: "))
for i in range(1 , num + 1):
    if num% i == 0:
        divisao += 1
if divisao == 2:
    print("É primo!")
else:
    print("Não é primo")

#6) Numeros divisiveis 
divisao = 0
num = int(input("Número inteiro: "))
for i in range(2 , num):
    if num % i == 0:
        divisao += 1
if divisao == 0:
    print("É primo!")
else:
    for i in range(1 , num +1):
        if num % i == 0:
            print(num, "é divisivel por", i)

#7) Idade dos alunos   
c1 = 0
c2 = 0
c3 = 0
soma= 0
n = int(input('Quantas pessoas têm na turma?: '))

for i in range (0,n):
    idade = int(input("Digite a idade: "))
    if 0 <= idade <= 25:
        c1 += 1
        soma = soma + idade
    elif 26 <= idade <= 60:
        c2 += 1
        soma = soma + idade
    elif idade > 60:
        c3 += 1
        soma = soma + idade
media=soma/n
if 0 <= media <= 25:
    print("Seguindo a media das idades, a turma é jovem")
elif 26 <= media <= 60:
    print("Seguindo a media das idades, a turma é adulta")
elif media > 60:
    print("Seguindo a media das idades, a turma é idosa")

#8)
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
soma= 0
if num1 > num2:
    for i in range(num2+1,num1):
        soma = soma + i
    print("A soma dos números é", soma)
            

elif num1 < num2:
    for i in range(num1+1,num2):
        soma = soma + i
    print("A soma dos números é", soma)
        

#9)Tabuada
num = int(input("Digite um número: "))
for i in range(11):
    total = num * i
    print("num", "x", i ,"=", total)

#10)Disciplina Calculo
melhorNota = 0
soma = 0
for i in range (5):
    nome= input("Nome: ")
    nota= float(input("Nota: "))
    soma = soma + nota
    
    if nota>melhorNota:
        melhorNota = nota
        aluno = nome
    if nota >= 5.75:
        print(nome ,"foi aprovado")
    elif 5.75> nota >=2.75:
        print(nome, "está em recuperação")
    elif nota <2.75:
        print(nome, "foi reprovado")
media = soma/5
print("A media das notas são: ", media)
print("O aluno com a media mais alta foi: ", aluno)