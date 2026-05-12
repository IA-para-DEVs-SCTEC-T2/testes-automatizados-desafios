import pytest
from chamados import classificar_chamado

# Testes para o Desafio 3 utilizando parametrização para reduzir repetição

@pytest.mark.parametrize("tipo_problema, cliente_premium, esperado", [
    ("sem_sinal", False, "alta"),
    ("sem_sinal", True, "alta"),
    ("cobranca", True, "alta"),
    ("cobranca", False, "media"),
    ("internet_lenta", False, "baixa"),
    ("internet_lenta", True, "baixa"),
    ("", False, "baixa"),
    ("Cobranca", True, "baixa"), # O código atual é case-sensitive
], ids=[
    "sem_sinal_cliente_comum -> alta",
    "sem_sinal_cliente_premium -> alta",
    "cobranca_cliente_premium -> alta",
    "cobranca_cliente_comum -> media",
    "outro_problema_cliente_comum -> baixa",
    "outro_problema_cliente_premium -> baixa",
    "problema_vazio -> baixa",
    "cobranca_com_maiuscula (case sensitive) -> baixa"
])
def test_classificar_chamado_cenarios(tipo_problema, cliente_premium, esperado):
    """
    Testa a classificação de chamados para diversos cenários de negócio.
    Utiliza parametrização para testar múltiplos casos com o mesmo código de teste.
    """
    assert classificar_chamado(tipo_problema, cliente_premium) == esperado
