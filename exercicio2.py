'''Crie uma função chamada calcular_area_retangulo que aceite dois parâmetros: 
base e altura, ambos com valores padrão iguais a 1. A função deve retornar a área 
do retângulo.
'''

def calcuar_area_retangulo(base=1, altura=1):
    return base * altura

b = float(input('Base: '))
a = float(input('Altura: '))

print(f'Área do retangulo: {calcuar_area_retangulo(b, a)}')
