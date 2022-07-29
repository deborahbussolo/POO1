nome = 'O'
saltos = []
maiorsalto=0
menorsalto=10000
media=0
soma=0
while True:
    nome = input("[Para encerrar o progrograma digite O ]\nNome: ")
    if nome == 'O':
        break
    else:
        for i in range(1,6):
            salto = float(input(f"{i}° Salto : "))
            saltos.append(salto)
            if salto <= menorsalto:
                menorsalto = salto
            if salto >= maiorsalto:
                maiorsalto = salto
        for i in range(5):
            soma += saltos[i]
            
        media = (soma-(maiorsalto+menorsalto))/3
        print("\nMelhor salto: {:.1f} m\nMenor salto: {:.1f} m\n Média dos demais saltos: {:.1f} m\nResultado final: \n{}: {:.1f} m\n".format(maiorsalto,menorsalto,media,nome,media))
