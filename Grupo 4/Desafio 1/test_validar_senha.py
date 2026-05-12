import pytest
from validar_senha import validar_senha


# 1. Senha com menos de 8 caracteres - inválida
def test_senha_curta():
    assert validar_senha("Abc123") == False


# 2. Senha apenas com letras minúsculas - inválida
def test_senha_so_minusculas():
    assert validar_senha("abcdefgh") == False


# 3. Senha sem números - inválida
def test_senha_sem_numero():
    assert validar_senha("AbcDefgh") == False


# 4. Senha sem letras maiúsculas - inválida
def test_senha_sem_maiuscula():
    assert validar_senha("abcd1234") == False


# 5. Senha válida com 8 caracteres, maiúscula e número
def test_senha_valida():
    assert validar_senha("Senha123") == True


# 6. Limite: exatamente 7 caracteres (inválida)
def test_senha_7_caracteres():
    assert validar_senha("Abc1234") == False


# 7. Limite: exatamente 8 caracteres válidos
def test_senha_8_caracteres():
    assert validar_senha("Abcd1234") == True


# 8. Senha vazia - inválida
def test_senha_vazia():
    assert validar_senha("") == False


# 9. Senha com caracteres especiais - válida
def test_senha_com_especiais():
    assert validar_senha("Senha@123") == True
