import pytest
from Desafio 1.senha import validar_senha

# Testes baseados nas regras de negócio do desafio

def test_deve_rejeitar_senha_com_menos_de_oito_caracteres():
    """Motivo: A regra diz que senhas com menos de 8 caracteres são inválidas."""
    assert validar_senha("Ab12345") == False

def test_deve_rejeitar_senha_sem_letra_maiuscula():
    """Motivo: A regra diz que senhas sem letra maiúscula são inválidas."""
    assert validar_senha("abcdefg1") == False

def test_deve_rejeitar_senha_sem_numero():
    """Motivo: A regra diz que senhas sem número são inválidas."""
    assert validar_senha("Abcdefgh") == False

def test_deve_aceitar_senha_valida_no_limite_de_oito_caracteres():
    """Motivo: Validar o limite mínimo de 8 caracteres com todas as regras atendidas."""
    assert validar_senha("Abcdefg1") == True

def test_deve_rejeitar_senha_com_sete_caracteres_caso_borda():
    """Motivo: Caso de borda. 7 caracteres atendendo outras regras deve ser inválida."""
    assert validar_senha("Abcdef1") == False

def test_deve_rejeitar_senha_vazia_caso_borda():
    """Motivo: Caso de borda extremo. String vazia deve ser inválida."""
    assert validar_senha("") == False

def test_deve_rejeitar_senha_com_apenas_numeros():
    """
    Motivo: Verificar se a ausência de maiúsculas é detectada em senhas numéricas.
    NOTA: Este teste vai FALHAR com o código atual da imagem devido a um bug na lógica.
    """
    assert validar_senha("12345678") == False

def test_deve_aceitar_senha_com_caracteres_especiais():
    """Motivo: Garantir que caracteres especiais não quebrem a validação se as regras forem atendidas."""
    assert validar_senha("Abcdef1!") == True
