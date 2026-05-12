import pytest
from desconto import calcular_desconto

# Testes para o Desafio 2: Cálculo de Desconto

def test_deve_lancar_ValueError_quando_valor_da_compra_for_negativo():
    """Motivo: A regra diz que valores menores que 0 devem lançar ValueError."""
    with pytest.raises(ValueError, match="Valor inválido"):
        calcular_desconto(-1, False)

def test_deve_aplicar_desconto_de_15_por_cento_quando_cliente_for_vip_com_compra_abaixo_de_300():
    """Motivo: Cliente VIP deve receber 15% de desconto."""
    # 100 - 15% = 85
    assert calcular_desconto(100, True) == 85.0

def test_deve_aplicar_desconto_de_10_por_cento_quando_valor_da_compra_for_maior_ou_igual_a_300_e_cliente_nao_for_vip():
    """Motivo: Compra >= 300 para cliente comum deve receber 10% de desconto."""
    # 300 - 10% = 270
    assert calcular_desconto(300, False) == 270.0

def test_nao_deve_aplicar_desconto_quando_valor_da_compra_for_menor_que_300_e_cliente_nao_for_vip():
    """Motivo: Demais casos (não VIP e < 300) = Sem desconto."""
    assert calcular_desconto(200, False) == 200.0

def test_deve_priorizar_desconto_vip_sobre_desconto_por_valor_quando_cliente_for_vip_e_compra_for_maior_ou_igual_a_300():
    """Motivo: Validar que a regra VIP tem prioridade e os descontos não se acumulam."""
    # 400 - 15% = 340 (Se acumulasse ou aplicasse 10%, o valor seria diferente)
    assert calcular_desconto(400, True) == 340.0

# Casos de Borda (Boundary Cases)

def test_deve_retornar_zero_quando_valor_da_compra_for_zero_limite_inferior():
    """Caso de borda: Valor exato 0."""
    assert calcular_desconto(0, False) == 0.0

def test_nao_deve_dar_desconto_quando_valor_da_compra_for_imediatamente_abaixo_de_300():
    """Caso de borda: Valor 299.99 (não deve atingir a regra de >= 300)."""
    assert calcular_desconto(299.99, False) == 299.99

def test_deve_aplicar_desconto_de_10_por_cento_quando_valor_da_compra_for_exatamente_300_limite():
    """Caso de borda: Valor exato 300 deve aplicar o desconto de 10%."""
    assert calcular_desconto(300, False) == 270.0
