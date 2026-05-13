# Testes E2E — Grupo 8

Este projeto contém testes end-to-end (E2E) para validar o fluxo de login de uma aplicação web estática, utilizando **Playwright com Python** e **pytest**.

---

## Pré-requisitos

- Python 3.8 ou superior
- pip

---

## Diretório de trabalho

Todos os comandos abaixo devem ser executados a partir do diretório `grupo8/e2e`. Navegue até ele antes de prosseguir:

```bash
cd grupo8/e2e
```

---

## Instalação

**1. Instale as dependências Python:**

```bash
pip install pytest pytest-playwright
```

**2. Instale os navegadores do Playwright:**

```bash
playwright install
```

---

## Estrutura do Projeto

```
grupo8/e2e/
├── login.html          # Tela de login da aplicação
├── dashboard.html      # Tela de dashboard (pós-login)
├── test_login.py       # Arquivo de testes E2E
├── prompt.md           # Prompts utilizados para geração dos testes
├── requirements.txt    # Dependências do projeto
├── resultado.txt       # Resultado dos testes
└── README.md           # Este arquivo
```

---

## Executando os Testes

> ⚠️ Certifique-se de estar no diretório `grupo8/e2e` antes de rodar qualquer comando.

Para rodar todos os testes:

```bash
pytest test_login.py
```

Para rodar em um navegador específico (padrão é Chromium):

```bash
pytest test_login.py --browser chromium
pytest test_login.py --browser firefox
pytest test_login.py --browser webkit
```

Para rodar com saída detalhada:

```bash
pytest test_login.py -v
```

Para rodar em modo headed (com janela do navegador visível):

```bash
pytest test_login.py --headed
```

---

## Cenários de Teste

### Teste 1 — Login com sucesso

**Descrição:** Valida que um usuário com credenciais válidas é redirecionado para o dashboard.

| Campo | Valor |
|-------|-------|
| Email | `user@test.com` |
| Senha | `123456` |

**Validações:**
- A URL deve conter `dashboard.html`
- O botão de logout (`#btn-logout`) deve estar visível

---

### Teste 2 — Login com falha

**Descrição:** Valida que credenciais inválidas exibem mensagem de erro e mantêm o usuário na tela de login.

| Campo | Valor |
|-------|-------|
| Email | `user2@test.com` |
| Senha | `abcdef` |

**Validações:**
- A URL deve permanecer em `login.html`
- A mensagem `"Credenciais inválidas"` deve ser exibida no elemento `#mensagem`

---

### Teste 3 — Campos visíveis e habilitados ao carregar

**Descrição:** Valida que os campos de email e senha estão visíveis e habilitados quando a página de login é carregada.

**Validações:**
- `#email` deve estar visível e habilitado
- `#senha` deve estar visível e habilitado

---

### Teste 4 — Mensagem de erro vazia ao carregar

**Descrição:** Valida que nenhuma mensagem de erro é exibida antes de qualquer interação do usuário.

**Validações:**
- `#mensagem` deve estar vazio ao carregar a página

---

### Teste 5 — Login com campos vazios

**Descrição:** Valida que clicar em "Entrar" sem preencher os campos não redireciona o usuário.

**Validações:**
- A URL deve permanecer em `login.html`
- A mensagem `"Credenciais inválidas"` deve ser exibida

---

### Teste 6 — Título da página de login

**Descrição:** Valida que o título da aba do navegador na tela de login é `"Login"`.

---

### Teste 7 — Título da página de dashboard

**Descrição:** Valida que o título da aba do navegador na tela de dashboard é `"Dashboard"`.

---

### Teste 8 — Mensagem de boas-vindas no dashboard

**Descrição:** Valida que após login bem-sucedido a mensagem de boas-vindas é exibida corretamente.

**Validações:**
- `#welcome-message` deve exibir `"Usuário autenticado com sucesso."`

---

### Teste 9 — Falha seguida de sucesso redireciona corretamente

**Descrição:** Valida que após uma tentativa de login inválida, o usuário consegue fazer login com credenciais corretas na mesma sessão.

**Validações:**
- Após credenciais inválidas, `#mensagem` exibe o erro
- Após credenciais válidas, a URL muda para `dashboard.html` e `#btn-logout` fica visível

---

## Resultado Esperado

```
test_login.py::test_login_sucesso_redireciona_para_dashboard[chromium] PASSED
test_login.py::test_login_falha_exibe_mensagem_credenciais_invalidas[chromium] PASSED
test_login.py::test_campos_email_e_senha_visiveis_e_habilitados[chromium] PASSED
test_login.py::test_mensagem_erro_vazia_ao_carregar_pagina[chromium] PASSED
test_login.py::test_login_com_campos_vazios_nao_redireciona[chromium] PASSED
test_login.py::test_titulo_pagina_login[chromium] PASSED
test_login.py::test_titulo_pagina_dashboard[chromium] PASSED
test_login.py::test_mensagem_boas_vindas_no_dashboard[chromium] PASSED
test_login.py::test_login_falha_depois_sucesso_redireciona_corretamente[chromium] PASSED

9 passed
```
