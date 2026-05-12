import pytest
from validar_senha import validar_senha


# ──────────────────────────────────────────────
# Cenários Positivos — senha válida
# ──────────────────────────────────────────────

class TestSenhaValida:
    def test_senha_com_maiuscula_e_numero(self):
        """8 caracteres, maiúscula e número — válida."""
        assert validar_senha("Senha123") is True

    def test_senha_com_maiuscula_numero_e_especial(self):
        """Maiúscula, número e caractere especial — válida."""
        assert validar_senha("Senha@12") is True

    def test_senha_longa_valida(self):
        """Senha longa com maiúscula e número — válida."""
        assert validar_senha("SuperSenha2024!") is True

    def test_senha_apenas_maiusculas_e_numeros(self):
        """Só maiúsculas e números — válida."""
        assert validar_senha("SENHA123") is True

    def test_senha_com_maiuscula_no_final(self):
        """Maiúscula no final da senha — válida."""
        assert validar_senha("senha12A") is True

    def test_senha_com_numero_no_inicio(self):
        """Número no início da senha — válida."""
        assert validar_senha("1senhA23") is True


# ──────────────────────────────────────────────
# Cenários Negativos — senha inválida
# ──────────────────────────────────────────────

class TestSenhaInvalida:
    def test_senha_muito_curta(self):
        """Menos de 8 caracteres — inválida."""
        assert validar_senha("Ab1") is False

    def test_senha_sem_maiuscula(self):
        """Sem letra maiúscula — inválida."""
        assert validar_senha("senha123") is False

    def test_senha_sem_numero(self):
        """Sem número — inválida."""
        assert validar_senha("SenhaAbc") is False

    def test_senha_sem_maiuscula_e_sem_numero(self):
        """Sem maiúscula e sem número — inválida."""
        assert validar_senha("senhafraca") is False

    def test_senha_vazia(self):
        """Senha vazia — inválida."""
        assert validar_senha("") is False

    def test_senha_so_numeros(self):
        """Só números, sem maiúscula — inválida."""
        assert validar_senha("12345678") is False

    def test_senha_so_caracteres_especiais(self):
        """Só caracteres especiais, sem maiúscula e sem número — inválida."""
        assert validar_senha("!@#$%^&*") is False

    def test_senha_maiuscula_sem_numero(self):
        """Maiúscula presente mas sem número — inválida."""
        assert validar_senha("Senha@@@") is False


# ──────────────────────────────────────────────
# Edge Cases — casos limite
# ──────────────────────────────────────────────

class TestEdgeCases:
    def test_senha_exatamente_8_caracteres_valida(self):
        """Exatamente 8 caracteres com maiúscula e número — válida (limite inferior válido)."""
        assert validar_senha("Senha12!") is True

    def test_senha_exatamente_7_caracteres_invalida(self):
        """Exatamente 7 caracteres — inválida (abaixo do limite)."""
        assert validar_senha("Senha1!") is False

    def test_senha_exatamente_8_caracteres_sem_numero(self):
        """Exatamente 8 caracteres sem número — inválida."""
        assert validar_senha("SenhaAbc") is False

    def test_senha_exatamente_8_caracteres_sem_maiuscula(self):
        """Exatamente 8 caracteres sem maiúscula — inválida."""
        assert validar_senha("senha123") is False

    def test_senha_um_unico_numero(self):
        """Apenas um número, mas com maiúscula e 8+ chars — válida."""
        assert validar_senha("Senhaaaa1") is True

    def test_senha_uma_unica_maiuscula(self):
        """Apenas uma maiúscula, mas com número e 8+ chars — válida."""
        assert validar_senha("A1234567") is True

    def test_senha_unicode_maiuscula_e_numero(self):
        """Caractere unicode maiúsculo com número — válida."""
        assert validar_senha("Ação1234") is True

    def test_senha_com_espacos(self):
        """Espaços não invalidam — válida se tiver maiúscula, número e 8+ chars."""
        assert validar_senha("Senha 12") is True
