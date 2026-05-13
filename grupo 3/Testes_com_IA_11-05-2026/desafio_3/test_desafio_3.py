import importlib.util
import pytest
from pathlib import Path

_module_path = Path(__file__).parent / "Desafio_3.py"
_spec = importlib.util.spec_from_file_location("Desafio_3", _module_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
classificar_chamado = _mod.classificar_chamado


# Sem sinal = prioridade alta
def test_sem_sinal_retorna_alta():
    assert classificar_chamado("sem_sinal", False) == "alta"

def test_sem_sinal_premium_retorna_alta():
    assert classificar_chamado("sem_sinal", True) == "alta"


# Cobrança + cliente premium = prioridade alta
def test_cobranca_cliente_premium_retorna_alta():
    assert classificar_chamado("cobranca", True) == "alta"


# Cobrança + cliente comum = prioridade média
def test_cobranca_cliente_comum_retorna_media():
    assert classificar_chamado("cobranca", False) == "media"


# Outros casos = prioridade baixa
def test_outro_tipo_nao_premium_retorna_baixa():
    assert classificar_chamado("suporte", False) == "baixa"

def test_outro_tipo_premium_retorna_baixa():
    assert classificar_chamado("suporte", True) == "baixa"

def test_tipo_vazio_retorna_baixa():
    assert classificar_chamado("", False) == "baixa"
