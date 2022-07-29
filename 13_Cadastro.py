#funções
def pessoas_cadastradas():
    quantidade = len(lista)
    return quantidade

def media_idade():
    soma = 0
    for pessoa in lista:
        soma += pessoa['idade']
    return soma/len(lista)

def mulheres():
    lista_mulheres = []
    for pessoa in lista:
        if pessoa['sexo']== 'F':
            nome = pessoa['nome']
            lista_mulheres.append(nome)
    return lista_mulheres

def idade_acima():
    lista_idade = []
    for pessoa in lista:
        if pessoa['idade']>media_idade():
            nome = pessoa['nome']
            lista_idade.append(nome)
    return lista_idade

#criação das listas e dicionarios
lista = []
pessoa = {}
while True:
    pessoa ['nome']= str(input("Nome:"))
    pessoa ['sexo']= str(input("Sexo? [F/M]")).upper()
    pessoa ['idade']= int(input("Idade:"))
    lista.append(pessoa.copy())
    
    R = input("Deseja continuar? [S/N]").upper()
    if R == 'N':
        break
    
print("n/Pessoas cadastradas: ",pessoas_cadastradas())
print("A média de idade do grupo é ",media_idade())
print("As mulheres cadastradas são: ",mulheres())
print("Pessoas com a idade acima da media: ",idade_acima())
      
