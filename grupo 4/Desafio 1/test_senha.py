import pytest
from Desafio 1.senha import validar_senha

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
    # Este teste vai FALHAR com o código da imagem
    assert validar_senha("12345678") == False

def test_senha_com_espaco():
    # O código da imagem aceita espaços?
    # "Abcdef 1" -> len 8, islower False, isalpha False -> Returns True
    assert validar_senha("Abcdef 1") == True

def test_senha_com_caracteres_especiais():
    # "Abcdefg!" -> len 8, islower False, isalpha False -> Returns True
    # Mas não tem número! Então deveria ser inválida.
    # O código da imagem vai retornar True porque isalpha() é False (devido ao !)
    # Mas a regra diz: "Sem número = Inválida".
    # Então este teste vai FALHAR com o código da imagem se esperarmos False.
    assert validar_senha("Abcdefg!") == False

def test_senha_vazia():
    assert validar_senha("") == False
