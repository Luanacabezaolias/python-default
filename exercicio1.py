'''Escreva uma função chamada mostrar_informacoes que aceite três parâmetros 
nomeados: nome, idade e cidade. A função deve imprimir uma mensagem 
formatada com essas informações.'''

def mostrar_informacoes(nome, idade, cidade):
    print(f'Nome: {nome}, Idade:{idade}, Cidade:{cidade}')

n = input('Nome: ')
i = input('Idade: ')
c = input('Cidade: ')

mostrar_informacoes(nome=n, idade = i, cidade = c)

    