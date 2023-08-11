'''Crie uma função chamada enviar_email que aceite os parâmetros destinatario, 
assunto e corpo. O parâmetro assunto deve ter um valor padrão de "Sem assunto". 
O parâmetro corpo deve ter um valor padrão de uma string vazia. A função deve 
imprimir as informações formatadas. Inclua uma docstring que explique brevemente 
o propósito da função.'''

def enviar_email(destinatario, assunto="Sem assunto", corpo=''):
    print(f'Destinatario: {destinatario}')
    print(f'Assunto: {assunto}')
    print(f'Corpo: {corpo}')

enviar_email("lu.linda@gmail.com")
enviar_email("lu.linda@gmail.com, urgente")
enviar_email("lu.linda@gmail.com" corpo="conteudo do email")
