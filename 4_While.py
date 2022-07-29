#1 M/F
sexo=input("(M)Masculino\n(F)Feminino\nSexo:").upper()
while sexo != "F" and "M":
    sexo=input("Valor não é valido!\nDigite novamente:").upper()

#2 Número Aleatório
from random import randrange
x = randrange(11)
num = int(input("Digite um número:"))
cont = 1
while num != x:
    num = int(input("Tente novamente:"))
    cont += 1
print(f"Você acertou! Na {cont}° tentativa!")

#3 MEDIA MAIOR MENOR
soma = 0
cont = 0
r = "S"
while r == "S":
    num = int(input("Digite um número:"))
    cont += 1
    if num == 0:
        break
    if cont == 1:
        menornum = maiornum = num
    else:
        if maiornum <= num:
            maiornum = num
        if menornum >= num:
            menornum = num      
    soma += num
    
    r = input("Gostaria de Continuar? S / N").upper()
print("Media:",round(soma/cont,2),"\nMaior valor:", maiornum,"\nMenor valor:" ,menornum)


#4 DESCONTO SALARIO
r = "S"
while r == "S":
    salario = int(input("Salario:"))
    desconto = salario*0.11
    if desconto <= 320:
        total = salario - desconto
        print("Seu desconto é de R$", desconto,"\nTotal:R$", total)

    else:
        desconto = 320 * 100/salario
        total = salario - 320
        print("Seu desconto é de RS320,00 =",round(desconto, 2),"%\nTotal: R$", total)
    r = input("Deseja continuar? [S/N]").upper()

#5 PRAIAS FLORIANOPOLIS
#os km das praias estão com base no google maps, na opção "Caminhando"
opcao = int(input("Você deseja:\n1 - Número de praias solicitadas.\n2 - Saber a praia mais distante do centro da cidade\n3 - Saber quais são as praias entre 15 e 20 km do centro.\n4 - Saber a distância média das praias."))
if opcao == 1:
    num = int(input("Numero de praias que deseja encontrar?"))
    for i in range(1,num+1):
        if i == 1:
            print("Praia Mole - 15.3 km")
        elif i == 2:
            print("Praia Santo Antônio de Lisboa - 15.5 km")
        elif i == 3:
            print("Praia Campeche - 16.1 km")
        elif i == 4:
            print("Praia Joaquina - 16.3 km")
        elif i == 5:
            print("Praia do Morro das Pedras - 16.3 km")
        elif i == 6:
            print("Praia do Sambaqui - 17.1 km")
        elif i == 7:
            print("Praia do Cacupe Grande - 17.2 km")
        elif i == 8:
            print("Praia da Barra da Lagoa - 19.3 km")        
        elif i == 9:
            print("Praia do Ribeirão da Ilha - 21.7 km")        
        elif i == 10:
            print("Praia Galheta - 22.1 km")
        elif i == 11:
            print("Praia da Armação - 23 km")        
        elif i == 12:
            print("Praia do Matadeiro - 23.3 km")        
        elif i == 13:
            print("Praia Lagoinha do Leste - 25.4 km")        
        elif i == 14:
            print("Praia do Pântano do Sul - 26.5 km")        
        elif i == 15:
            print("Praia de Canasvieiras - 26.8 km")        
        elif i == 16:
            print("Praia dos Açores - 28.3 km")        
        elif i == 17:
            print("Praia Cachoeira do Bom Jesus - 28.4 km")        
        elif i == 18:
            print("Praia Moçambique - 29.8 km")        
        elif i == 19:
            print("Praia Solidão - 30 km")
        elif i == 20:
            print("Praia de Jurerê - 31.2 km")        
        elif i == 21:
            print("Praia dos Ingleses - 31.6 km")        
        elif i == 22:
            print("Praia Ponta das Canas - 32.5 km")         
        elif i == 23:
            print("Praia da Lagoinha - 33.5 km")            
        elif i == 24:
            print("Praia do Forte - 33.8 km")
        elif i == 25:
            print("Praia Brava - 34.2 km") 
        elif i == 26:
            print("Praia do Santinho - 34.2 km")
        elif i == 27:
            print("Praia Daniela - 35.3 km")        
        elif i == 28:
            print("Praia de Naufragados - 37.2 km")
        else:
            break
elif opcao == 2:
    print("A praia mais distante do centro da cidade é a Praia de Naufragados - 37.2 km de distancia.")
elif opcao == 3:
    print("As praias entre 15 e 20 km do centro são:\nPraia Mole - 15.3 km\nPraia Santo Antônio de Lisboa - 15.5 km\nPraia Campeche - 16.1 km\nPraia Joaquina - 16.3 km\nPraia do Morro das Pedras - 16.3 km\nPraia do Sambaqui - 17.1 km\nPraia do Cacupe Grande - 17.2 km\nPraia da Barra da Lagoa - 19.3 km")
elif opcao == 4:
    soma = round((15.3+15.5+16.1+16.3+16.3+17.1+17.2+19.3+21.7+22.1+23+23.3+25.4+26.5+26.8+28.3+28.4+29.8+30+31.2+31.6+32.5+33.5+33.8+34.2+34.2+35.3+37.2)/28 , 1)
    print("Distancia media das praias do centro é de",soma)