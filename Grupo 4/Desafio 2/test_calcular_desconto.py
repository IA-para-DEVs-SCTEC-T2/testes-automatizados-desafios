import pytest
from calcular_desconto import calcular_desconto


def test_valor_invalido():
    with pytest.raises(ValueError):
        calcular_desconto(-10, False)


def test_desconto_vip():
    resultado = calcular_desconto(200, True)
    assert resultado == 200 * 0.85


def test_desconto_compra_acima_300():
    resultado = calcular_desconto(300, False)
    assert resultado == 300 * 0.90


def test_sem_desconto():
    resultado = calcular_desconto(150, False)
    assert resultado == 150


def test_vip_tem_prioridade_sobre_regra_300():
    resultado = calcular_desconto(400, True)
    assert resultado == 400 * 0.85
