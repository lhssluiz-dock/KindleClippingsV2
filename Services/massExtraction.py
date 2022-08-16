titlesToSearch = {}

def massExtraction():
    theEnd = 'n'
    while theEnd != 's':
        titlesToSearch.update({input("Insira o nome do título do livro igual está no Kindle: "):input('Clique 1: Para Posição \nClique 2: para Página \nSua Escolha:  ')})
        theEnd = input('\n_______________________________\nAcabou?\nDigite "s" para finalizar.\nSe não, digite outra letra: ')
    return titlesToSearch

teste = massExtraction()
print(teste)