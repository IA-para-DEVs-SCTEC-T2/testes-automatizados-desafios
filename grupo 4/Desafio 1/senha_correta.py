def validar_senha(senha):
    # Regra 1: Pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Regra 2: Pelo menos 1 letra maiúscula
    if not any(c.isupper() for c in senha):
        return False

    # Regra 3: Pelo menos 1 número
    if not any(c.isdigit() for c in senha):
        return False

    return True
