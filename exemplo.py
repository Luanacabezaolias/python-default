# PARÂMETRO DEFAULT

#POSICIONAIS (RESPEITAM A ORDEM DOS VALORES)
# NOMEADOS (NÃO PRECISAM RESPEITAR A MESMA ORDEM)

def calcular_media(matematica: float, fisica: float, quimica: float = 0):
    print(f'Matematica: {matematica}')
    print(f'Fisica: {fisica}')
    print(f'Quimica: {quimica}')
    media = (matematica + fisica + quimica) / 3
    return media

m = float(input('Matematica: '))
q = float(input('Quimica: '))
f = float(input('Fisica: '))

print (f'Media: {calcular_media(m, quimica=q, fisica=f)}')
print (f'Media: {calcular_media(m, quimica=q)}')
print (f'Media: {calcular_media(quimica=q)}')