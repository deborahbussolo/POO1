maispesada = maisleve = peso = 0
nomeleve = ''
nomepesada= ''
listaleve = []
listapesada = []
pessoas = []
maiorde20 = []
R = 'S'
while R=='S':
    pessoas.append([x for x in input("Digite nome, idade e peso: ").split()])
    R = input("Você deseja continuar?[S/N] ").upper()
    
for pessoa in pessoas:
    if int(pessoa[1]) > 20:
        maiorde20.append(pessoa[0:2])
    if pessoas.index(pessoa) == 0:
        maispesada = maisleve = peso = int(pessoa[2])
        if maispesada <= peso:
            maispesada = peso
            nomepesada =(pessoa[0])
        if maisleve >= peso:
            maisleve = peso
            nomeleve =(pessoa[0])
    else:
        peso = int(pessoa[2])
        if maispesada <= peso:
            maispesada = peso
            nomepesada =(pessoa[0])
        if maisleve >= peso:
            maisleve = peso
            nomeleve =(pessoa[0])
print("\nNúmero de pessoas cadastradas: ",len(pessoas))
print(len(maiorde20)," pessoas com mais de 20 anos: ", maiorde20)
print('Pessoa(s) mais pesada(s): ', nomepesada, "\nPessoa(s) mais leve(s): ", nomeleve)
#adicionar + de uma pessoa na lista de pesada ou leve