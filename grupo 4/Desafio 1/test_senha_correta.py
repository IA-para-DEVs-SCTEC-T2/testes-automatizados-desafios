import pytest
from Desafio 1.senha_correta import validar_senha

# Testes Unitários

def test_senha_curta():
    assert validar_senha("Ab1") == False

def test_senha_no_limite_curta():
    assert validar_senha("Ab12345") == False # 7 caracteres

def test_senha_no_limite_valida():
    assert validar_senha("Ab123456") == True # 8 caracteres

def test_senha_sem_maiuscula():
    assert validar_senha("abcdefg1") == False

def test_senha_sem_numero():
    assert validar_senha("Abcdefgh") == False

def test_senha_valida():
    assert validar_senha("Abcdefg1") == True

def test_senha_apenas_numeros():
    assert validar_senha("12345678") == False

def test_senha_com_espaco():
    assert validar_senha("Abcdef 1") == True

def test_senha_com_caracteres_especiais():
    # Deve falhar porque não tem número
    assert validar_senha("Abcdefg!") == False

def test_senha_com_caracteres_especiais_e_numero():
    # Deve passar: 8+ chars, maiúscula, número
    assert validar_senha("Abcdef1!") == True

def test_senha_vazia():
    assert validar_senha("") == False
