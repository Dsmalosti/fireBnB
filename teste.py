import pytest
from app import *

#testando capacidade pessoas
def test_capacidade_poucas_pessoas():   
    imoveis_disponiveis = verifica_imovel_disponivel(1, '2025-12-12', '2025-12-13')
    assert  len(imoveis_disponiveis) == 5

def test_capacidade_media_pessoas():
    imoveis_disponiveis = verifica_imovel_disponivel(4, '2025-12-12', '2025-12-13')
    assert  len(imoveis_disponiveis) == 3

def test_capacidade_quase_todas_pessoas():
    imoveis_disponiveis = verifica_imovel_disponivel(6, '2025-12-12', '2025-12-13')
    assert  len(imoveis_disponiveis) == 1

def test_capacidade_maxima_pessoas():
    imoveis_disponiveis = verifica_imovel_disponivel(8, '2025-12-12', '2025-12-13')
    assert  len(imoveis_disponiveis) == 0

#testando pela data
def test_data():
    imoveis_disponiveis = verifica_imovel_disponivel(1, '2025-04-05', '2025-06-22')
    assert  len(imoveis_disponiveis) == 2

#testando pela data de inicio
def test_data_inicio():
    imoveis_disponiveis = verifica_imovel_disponivel(1, '2025-04-08', '2025-04-10')
    assert  len(imoveis_disponiveis) == 5

def test_data_inicio_reservada_comeco():
    imoveis_disponiveis = verifica_imovel_disponivel(1, '2025-05-10', '2025-05-12')
    assert  len(imoveis_disponiveis) == 4

def test_data_inicio_reservada_fim():
    imoveis_disponiveis = verifica_imovel_disponivel(1, '2025-06-24', '2025-06-29')
    assert  len(imoveis_disponiveis) == 4

#testando pela data de saida
def test_data_saida_reservada_comeco():
    imoveis_disponiveis = verifica_imovel_disponivel(1, '2025-08-12', '2025-08-16')
    assert  len(imoveis_disponiveis) == 4

#testando pela capacidade e data
def test_capacidade_data():
    imoveis_disponiveis = verifica_imovel_disponivel(4, '2025-08-15', '2025-08-20')
    assert  len(imoveis_disponiveis) == 2







    
    