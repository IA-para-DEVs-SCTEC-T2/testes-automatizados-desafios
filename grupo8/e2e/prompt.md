# Prompts Utilizados

## Prompt 1 — Geração do teste E2E

Considere o projeto no repositório atual. Eu gostaria de implementar um teste E2E usando Playwright com Python para validar o fluxo de login e acesso à tela de dashboard.

**Contexto:** A aplicação possui uma tela login.html com os campos:
- `#email`
- `#senha`
- `#btn-login`

Após login válido, o usuário deve ser redirecionado para dashboard.html.

**Cenário 1 - Sucesso:**
O usuário acessa a tela de login, informa email e senha válidos, clica no botão Entrar e deve acessar o Dashboard.

Dados de entrada:
- Email: user@test.com
- Senha: 123456

Validações esperadas:
- A URL deve conter dashboard.html
- O botão "Sair" identificado por `#btn-logout` deve estar visível

**Cenário 2 - Falha:**
O usuário acessa a tela de login, informa email e senha inválidos, clica no botão Entrar e deve visualizar a mensagem de erro "Credenciais inválidas" na tela no elemento "mensagem".

Dados de entrada:
- Email: user2@test.com
- Senha: abcdef

Validações esperadas:
- A URL deve ser mantida como login.html
- A mensagem "Credenciais inválidas" deve ser exibida no elemento de mensagem

Requisitos:
- Use pytest com Playwright em Python
- Crie um nome claro para o teste
- Use `expect()` do Playwright para validar URL e elementos da página
- Não gere explicações, apenas o código do teste

---

## Prompt 2 — Correção de falha nos testes

Esse foi o resultado. Ambos falharam. O que está errado?

```
FAILURES
___ test_login_sucesso_redireciona_para_dashboard[chromium] ___
desafio_1/test_login.py:17: in test_login_sucesso_redireciona_para_dashboard
    expect(page).to_have_url(lambda url: "dashboard.html" in url)
playwright._impl._errors.Error: value must be a string or regular expression

___ test_login_falha_exibe_mensagem_credenciais_invalidas[chromium] ___
desafio_1/test_login.py:28: in test_login_falha_exibe_mensagem_credenciais_invalidas
    expect(page).to_have_url(lambda url: "login.html" in url)
playwright._impl._errors.Error: value must be a string or regular expression

2 failed in 0.80s
```
