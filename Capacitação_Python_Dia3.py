from dataclasses import dataclass

#Análise:
# Exibir na tela todos os números pares até 20.

def pares_ate_20() -> None:
    '''Exibe na tela todos os números pares até 20, inclusive o 20.
    Utiliza o while loop.
    Exemplo:
    >>> pares_ate_20()
    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    '''
    
    i = 0
    while i <= 20:
        if i % 2 == 0:
            print(i)
            
        i += 1

    return None

#Análise:
#O usário deve cria uma senha
#A função deve perguntar ao usuário qual é a senha que ele criou.
#A função não se encerra até o usuário acertar a senha.

def cria_e_pergunta_senha() -> None:
    '''Possibilita ao usuário criar uma senha. Indaga ao usuário qual
    foi a senha cirada.
    A função não se encerra até que o usuário acerte a senha.

    >>> cria_e_pergunta_senha()
    
    
    '''

    senha = input('Por favor, digite a sua senha.')

    errou = True
    while errou:
        resposta = input('Digite a sua senha novamente.')

        if resposta == senha:
            errou = False

    return None


            
            







                
            
        
        








        
        







    
