import importlib.util
import pytest
from pathlib import Path

_spec = importlib.util.spec_from_file_location("desafio_2", Path(__file__).parent / "desafio_2.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
calcular_desconto = _mod.calcular_desconto


# Valor negativo = ValueError
def test_valor_negativo_levanta_value_error():
    with pytest.raises(ValueError):
        calcular_desconto(-1, False)

def test_valor_negativo_vip_levanta_value_error():
    with pytest.raises(ValueError):
        calcular_desconto(-100, True)


# Cliente VIP = 15% de desconto
def test_cliente_vip_recebe_15_porcento_desconto():
    assert calcular_desconto(100, True) == 85.0

def test_cliente_vip_compra_zero_sem_desconto():
    assert calcular_desconto(0, True) == 0.0


# Cliente VIP com compra >= 300 = aplica VIP (15%), não 10%
def test_cliente_vip_compra_acima_300_aplica_vip():
    assert calcular_desconto(300, True) == 255.0

def test_cliente_vip_compra_500_aplica_vip():
    assert calcular_desconto(500, True) == 425.0


# Compra >= 300 sem VIP = 10% de desconto
def test_compra_300_sem_vip_recebe_10_porcento():
    assert calcular_desconto(300, False) == 270.0

def test_compra_acima_300_sem_vip_recebe_10_porcento():
    assert calcular_desconto(500, False) == 450.0


# Demais casos = sem desconto
def test_compra_abaixo_300_sem_vip_sem_desconto():
    assert calcular_desconto(100, False) == 100.0

def test_compra_zero_sem_vip_sem_desconto():
    assert calcular_desconto(0, False) == 0.0
