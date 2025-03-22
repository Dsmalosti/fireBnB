def verifica_numero(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'ímpar'


#testando a função verifica número
def teste_numeros_impares_positivos():
    assert verifica_numero(243) == 'ímpar'

def teste_numeros_impares_negativos():
    assert verifica_numero(-77) == 'ímpar'

def teste_numeros_pares_positivos():
    assert verifica_numero(84) == 'par'

def teste_numeros_pares_negativos():
    assert verifica_numero(-456) == 'par'



    