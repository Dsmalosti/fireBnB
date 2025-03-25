import os
import pandas as pd
from datetime import datetime

# Lendo o arquivo CSV
df = pd.read_csv('catalogo_imoveis.csv', encoding='utf-8')
# Convertendo para dicionário
dicionario_imoveis = df.to_dict('records')
dfReservas = pd.read_csv('controle_reservas.csv', encoding='utf-8')
dicionario_reservas = dfReservas.to_dict('records')


def exibir_nome_programa():
    """Função responsavel para mostrar titulo principal"""
    print('-='*12)
    print('Fire BnB'.center(24))
    print('-='*12)

    
def verifica_imovel_disponivel(quantidade_pessoas, data_entrada, data_saida):
    data_entrada = datetime.strptime(data_entrada, "%Y-%m-%d")
    data_saida = datetime.strptime(data_saida, "%Y-%m-%d")

    imoveis_disponiveis = []

    # Verificar cada imovel
    for imovel in dicionario_imoveis:
        # Verifica se a capacidaade do imóvel é suficiente
        if imovel['capacidade_de_pessoas'] >= quantidade_pessoas:
            # Verificar se o imóvel está reservado no periodo que foi informado
            conflito = False
            for reserva in dicionario_reservas:
                if reserva['codigo_do_imovel'] == imovel['codigo_do_imovel']:
                    reserva_entrada = datetime.strptime(reserva['data_de_entrada'], "%Y-%m-%d")
                    reserva_saida = datetime.strptime(reserva['data_de_saida'], "%Y-%m-%d")

                    # Verificar se as datas estao conflitando
                    if not (data_saida <= reserva_entrada or data_entrada >= reserva_saida):
                        conflito = True
                        break

            # Se não houver conflito, adicionar o imóvel à lista de disponíveis
            if not conflito:
                imoveis_disponiveis.append(imovel)

    return imoveis_disponiveis


def main():
    """Função responsavel para exibir a tela principal"""
    os.system('cls')
    exibir_nome_programa()
    try:
        quantidade_pessoas = int(input("Informe a quantidade de pessoas: "))
        data_entrada = input("Informe a data de entrada (YYYY-MM-DD): ")
        data_saida = input("Informe a data de saída (YYYY-MM-DD): ")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números para a quantidade de pessoas e datas no formato correto.")
        exit()
    
    imoveis_disponiveis = verifica_imovel_disponivel(quantidade_pessoas, data_entrada, data_saida)

    # Exibir resultados
    if imoveis_disponiveis:
        print(f'{"Código do imóvel".center(22)} | {"Capacidade de pessoas".center(20)} | {"Cidade".center(21)} | {"Código postal".center(21)} | {"Preço por dia".center(21)} |')
        for imovel in imoveis_disponiveis:
            for valor in imovel.values():
                print('-',end='')
                print(f"{valor}".ljust(22), end='|')
            print()
    else:
        print("\nNenhum imóvel disponível para o período e quantidade de pessoas informados.")



if __name__  ==  '__main__':
    main()