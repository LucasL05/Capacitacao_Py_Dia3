from dataclasses import dataclass

#Análise:
#Criar o programa de um caixa eletrônico
#As seguites opções são ofertadas ao usuário:
#sacar, depositar, mostrar o saldo e sair.
#O saldo não pode ficar abaixo de 0
#O programa não deve parar até o usuário decidir sair.
#
#Tipos de dados:
#saldo: Dinheiro

@dataclass
class Dinheiro:
    '''Representa dinheiro.'''
    reais: int
    centavos: int

def dinheiro_para_str(valor: Dinheiro) -> str:
    '''Transforma *valor* em uma string agradável ao usuário.'''

    reais = str(valor.reais)
    
    if valor.centavos < 10:
        centavos = '0' + str(valor.centavos) 
  
    else:
        centavos = str(valor.centavos)
        
    return reais + '.' + centavos


def string_para_dinheiro(valor: str) -> Dinheiro:
    '''Transforma *valor* no seu equivalente em Dinheiro'''
    
    if '.' in valor:
        divisor = valor.find('.')
        reais = int(valor[:divisor])
    
        if int(valor[divisor + 1]) == '0': 
            centavos = int(valor[divisor+2])
        elif len(valor[divisor + 1:]) == 1:
            centavos = int(valor[divisor + 1]) * 10
        else:
            centavos = int(valor[divisor + 1:])
            
    else:
        reais = int(valor)
        centavos = 0

    return Dinheiro(reais, centavos)

def subtrai_dinheiro(valor: Dinheiro, subtrai: Dinheiro) -> Dinheiro:
    '''Efetua a operação *valor* - *subtrai*.'''

    if valor.centavos >= subtrai.centavos:
        reais = valor.reais - subtrai.reais
        centavos = valor.centavos - subtrai.centavos
        
    else:
        reais = valor.reais - subtrai.reais - 1
        centavos = 100 - subtrai.centavos + valor.centavos
    
    return Dinheiro(reais, centavos)

def soma_dinheiro(v1: Dinheiro, v2: Dinheiro) -> Dinheiro:
    '''Efetua a operação *v1* + *v2*'''

    centavos1 = v1.centavos
    centavos2 = v2.centavos
    soma_cent = centavos1 + centavos2
    if len(str(soma_cent)) > len(str(centavos1)) and len(str(soma_cent)) > len(str(centavos2)):
        reais = v1.reais + v2.reais + 1
        centavos = v1.centavos + v2.centavos
        centavos = int(str(centavos)[1:])

    else:
        reais = v1.reais + v2.reais
        centavos = v1.centavos + v2.centavos

    return Dinheiro(reais, centavos)
    
    

def caixa_eletronico(saldo: Dinheiro) -> None:
    '''Possibilita ao usuário visualizar o seu saldo, depositar, sacar
    e sair.
    *saldo* não pode ser menor do que zero em momento algum.
    '''

    assert saldo.reais > 0 or saldo.centavos > 0, 'Saldo não pode ser negativo.'

    ligado = True

    while ligado:
        print('')
        print('')
        print('Para visualizar seu saldo, digite 1')
        print('Para efetuar um depósito, digite 2')
        print('Para efetuar um saque, digite 3')
        print('Para desligar o aparelho, digite 0')
        operacao = int(input())

        if operacao == 1:
            formatado = dinheiro_para_str(saldo)
            print(f'Seu saldo: {formatado}R$')
        

        elif operacao == 2:
            valor_deposito = (input('Digite o valor do depósito.'))
            deposito = string_para_dinheiro(valor_deposito)
            saldo = soma_dinheiro(saldo, deposito)
            formatado = dinheiro_para_str(saldo)
            print('Depósito efetuado.')
            print(f'Seu saldo: {formatado}R$')

        elif operacao == 3:
            valor_saque = input('Digite o valor do saque.')
            saque = string_para_dinheiro(valor_saque)

            if saque.reais <= saldo.reais or (saque.reais == saldo.reais)\
               and (saque.centavos <= saldo.centavos):
                
                saldo = subtrai_dinheiro(saldo, saque)
                formatado = dinheiro_para_str(saldo)
                print('Saque efetuado com sucesso.')
                print(f'Seu saldo: {formatado}R$')
            else:
                print('Saldo insuficiente.')

        elif operacao == 0:
            ligado = False

        else:
            print('Por favor, digite um valor válido.')

    return None
