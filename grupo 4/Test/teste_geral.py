import sys
import os

# Adicionando os caminhos para importar os módulos
path_atual = os.path.dirname(__file__)
path_d1 = os.path.abspath(os.path.join(path_atual, '..', 'Desafio 1'))
path_d2 = os.path.abspath(os.path.join(path_atual, '..', 'Desafio 2'))
path_d3 = os.path.abspath(os.path.join(path_atual, '..', 'Desafio 3'))

# Teste do Desafio 1
print("=== TESTE GERAL: DESAFIO 1 (Validação de Senha) ===")
try:
    sys.path.append(path_d1)
    import senha as senha_orig
    import senha_correta as senha_corr
    sys.path.remove(path_d1)

    test_cases_d1 = [
        ("Ab1", False, "Curta"),
        ("Ab123456", True, "Válida"),
        ("abcdefg1", False, "Sem maiúscula"),
        ("Abcdefgh", False, "Sem número"),
        ("12345678", False, "Apenas números"),
    ]

    print(f"{'Senha':<15} | {'Esperado':<8} | {'Original':<8} | {'Corrigida':<8} | {'Status'}")
    print("-" * 60)
    for s, esp, desc in test_cases_d1:
        res_orig = senha_orig.validar_senha(s)
        res_corr = senha_corr.validar_senha(s)
        status = "OK" if res_corr == esp else "FAIL"
        print(f"{s:<15} | {esp!s:<8} | {res_orig!s:<8} | {res_corr!s:<8} | {status} ({desc})")
except Exception as e:
    print(f"Erro ao testar Desafio 1: {e}")

print("\n" + "="*50 + "\n")

# Teste do Desafio 2
print("=== TESTE GERAL: DESAFIO 2 (Cálculo de Desconto) ===")
try:
    sys.path.append(path_d2)
    import desconto
    sys.path.remove(path_d2)

    test_cases_d2 = [
        (100, True, 85.0, "VIP Compra Baixa"),
        (400, True, 340.0, "VIP Compra Alta"),
        (400, False, 360.0, "Comum Compra Alta"),
        (100, False, 100.0, "Comum Compra Baixa"),
        (300, False, 270.0, "Borda 300"),
    ]

    print(f"{'Valor':<6} | {'VIP':<5} | {'Esperado':<8} | {'Resultado':<8} | {'Status'}")
    print("-" * 50)
    for val, vip, esp, desc in test_cases_d2:
        res = desconto.calcular_desconto(val, vip)
        status = "OK" if res == esp else "FAIL"
        print(f"{val:<6} | {vip!s:<5} | {esp:<8.1f} | {res:<8.1f} | {status} ({desc})")
except Exception as e:
    print(f"Erro ao testar Desafio 2: {e}")

print("\n" + "="*50 + "\n")

# Teste do Desafio 3
print("=== TESTE GERAL: DESAFIO 3 (Classificação de Chamados) ===")
try:
    sys.path.append(path_d3)
    import chamados
    sys.path.remove(path_d3)

    test_cases_d3 = [
        ("sem_sinal", False, "alta", "Sem Sinal Comum"),
        ("cobranca", True, "alta", "Cobrança Premium"),
        ("cobranca", False, "media", "Cobrança Comum"),
        ("internet_lenta", False, "baixa", "Outro Caso"),
    ]

    print(f"{'Problema':<15} | {'Premium':<7} | {'Esperado':<8} | {'Resultado':<8} | {'Status'}")
    print("-" * 65)
    for prob, prem, esp, desc in test_cases_d3:
        res = chamados.classificar_chamado(prob, prem)
        status = "OK" if res == esp else "FAIL"
        print(f"{prob:<15} | {prem!s:<7} | {esp:<8} | {res:<8} | {status} ({desc})")
except Exception as e:
    print(f"Erro ao testar Desafio 3: {e}")
