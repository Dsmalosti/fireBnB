# Verificando se o número é par ou ímpar
No arquivo chamado 'funcoes.py' onde está a função 'verifica_numero()' que verifica se o número é par ou ímpar e nesse arquivo também está localizado os testes dessa função.

## Testes da função 'verifica_numero()' 
foi utilizado a ferramenta 'pytest' que detecta automaticamente funções de teste e fornece mensagens de erro mais descritivas.
as funções de testes também estão localizadas no arquivo 'funcoes.py', elas são: 

def teste_numeros_impares_positivos():
    assert verifica_numero(243) == 'ímpar'

def teste_numeros_impares_negativos():
    assert verifica_numero(-77) == 'ímpar'

def teste_numeros_pares_positivos():
    assert verifica_numero(84) == 'par'

def teste_numeros_pares_negativos():
    assert verifica_numero(-456) == 'par'

Cada função está verificando se um número é par ou ímpar, no caso para os testes estão usando tanto números positivos quanto negativos.
Para verificar se os testes estão ok é necessário digitar 'pytest funcoes.py' no terminal, então a ferramenta irá informar o resultado do teste.

## Arquivo 'main.py'
No arquivo main foi importado a função 'verifica_numero()', que será utilizado para verificar se o número é par ou ímpar.
Irá aparecer na tela um input para o úsuario digitar um número, retornando então se o número é par ou ímpar.
 
