import pytest
from classificar_chamado import classificar_chamado


def test_sem_sinal_retorna_prioridade_alta():
    assert classificar_chamado("sem_sinal", False) == "alta"


def test_sem_sinal_cliente_premium_retorna_prioridade_alta():
    assert classificar_chamado("sem_sinal", True) == "alta"


def test_cobranca_cliente_premium_retorna_prioridade_alta():
    assert classificar_chamado("cobranca", True) == "alta"


def test_cobranca_cliente_comum_retorna_prioridade_media():
    assert classificar_chamado("cobranca", False) == "media"


def test_outro_tipo_retorna_prioridade_baixa():
    assert classificar_chamado("instalacao", False) == "baixa"


def test_outro_tipo_cliente_premium_retorna_prioridade_baixa():
    assert classificar_chamado("manutencao", True) == "baixa"
