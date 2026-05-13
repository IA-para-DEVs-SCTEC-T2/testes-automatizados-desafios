import importlib.util
import pytest
from datetime import datetime
from pathlib import Path

_spec = importlib.util.spec_from_file_location("desafio_1", Path(__file__).parent / "desafio_1.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
validar_senha = _mod.validar_senha

LOG_FILE = "resultados_testes.log"


def registrar(nome_teste, senha, esperado, resultado):
    status = "PASSOU" if resultado == esperado else "FALHOU"
    linha = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {status} - {nome_teste} | senha='{senha}' | esperado={esperado} | obtido={resultado}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linha)


# Senhas inválidas
def test_senha_muito_curta():
    senha, esperado = "Ab1", False
    resultado = validar_senha(senha)
    registrar("test_senha_muito_curta", senha, esperado, resultado)
    assert resultado == esperado

def test_senha_sem_maiuscula():
    senha, esperado = "abcdefg1", False
    resultado = validar_senha(senha)
    registrar("test_senha_sem_maiuscula", senha, esperado, resultado)
    assert resultado == esperado

def test_senha_sem_numero():
    senha, esperado = "Abcdefgh", False
    resultado = validar_senha(senha)
    registrar("test_senha_sem_numero", senha, esperado, resultado)
    assert resultado == esperado

def test_senha_curta_sem_maiuscula_sem_numero():
    senha, esperado = "abc", False
    resultado = validar_senha(senha)
    registrar("test_senha_curta_sem_maiuscula_sem_numero", senha, esperado, resultado)
    assert resultado == esperado


# Senhas válidas
def test_senha_valida_minima():
    senha, esperado = "Abcdef1g", True
    resultado = validar_senha(senha)
    registrar("test_senha_valida_minima", senha, esperado, resultado)
    assert resultado == esperado

def test_senha_valida_longa():
    senha, esperado = "Senha123Segura", True
    resultado = validar_senha(senha)
    registrar("test_senha_valida_longa", senha, esperado, resultado)
    assert resultado == esperado

def test_senha_valida_multiplos_numeros():
    senha, esperado = "Abc12345", True
    resultado = validar_senha(senha)
    registrar("test_senha_valida_multiplos_numeros", senha, esperado, resultado)
    assert resultado == esperado

def test_senha_segura():
    senha, esperado = "C0ntr@senha$Segura2026", True
    resultado = validar_senha(senha)
    registrar("test_senha_segura", senha, esperado, resultado)
    assert resultado == esperado
