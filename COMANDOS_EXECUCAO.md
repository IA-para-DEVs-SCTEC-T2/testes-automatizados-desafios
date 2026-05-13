# 🚀 Comandos de Execução dos Testes E2E

## Pré-requisitos
```bash
pip install -r desafio_1/requirements.txt
playwright install
```

---

## Execução Individual dos Testes

### Desafio 1 - Login com Credenciais Válidas
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest desafio_1/test_login.py -v
```

### Desafio 1 - Login com Credenciais Inválidas (NOVO)
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest desafio_1/test_login_invalido.py -v
```

### Teste 1 - Login Simples
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest teste_1/test_login.py -v
```

### Teste 2 - Fluxo de Compra Original
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest teste_2/test_fluxo_compra.py -v
```

### Teste 2 - Fluxo de Compra Completo (NOVO)
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest teste_2/test_fluxo_compra_completo.py -v
```

### Teste 2 - Busca de Produto Inexistente (NOVO)
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest teste_2/test_busca_produto_inexistente.py -v
```

---

## Execução em Lote

### Executar todos os testes do Desafio 1
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest desafio_1/ -v
```

### Executar todos os testes do Teste 2
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest teste_2/ -v
```

### Executar TODOS os testes do projeto
```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest -v
```

---

## Execução com Relatório HTML

```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest -v --html=report.html --self-contained-html
```

---

## Execução com Modo Debug (Headed)

Para ver o navegador em ação:

```bash
cd /Users/gabrieldasilva/Desktop/aula-test-e2e
pytest teste_2/test_fluxo_compra_completo.py -v --headed
```

---

## Resumo dos Testes Gerados

| Teste | Arquivo | Descrição |
|-------|---------|-----------|
| ✅ Login Válido | `desafio_1/test_login.py` | Valida login com credenciais corretas |
| ✅ Login Inválido | `desafio_1/test_login_invalido.py` | Valida erro ao fazer login com credenciais erradas |
| ✅ Login Simples | `teste_1/test_login.py` | Teste básico de autenticação |
| ✅ Fluxo Compra | `teste_2/test_fluxo_compra.py` | Fluxo básico de compra |
| ✅ Fluxo Compra Completo | `teste_2/test_fluxo_compra_completo.py` | Fluxo completo com todas as validações |
| ✅ Busca Inexistente | `teste_2/test_busca_produto_inexistente.py` | Valida busca de produto que não existe |

---

## Notas Importantes

- Os testes utilizam **Playwright** como framework
- Todos os testes são **executáveis** e **independentes**
- Os seletores utilizados são **confiáveis** (IDs específicos)
- Cada teste cobre um **fluxo completo** com validações claras
- Os testes seguem **boas práticas** de automação E2E
