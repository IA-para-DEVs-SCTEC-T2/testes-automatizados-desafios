# 📖 Guia de Boas Práticas - Testes E2E com Playwright

## 🎯 Princípios Fundamentais

### 1. **Seletores Confiáveis**

❌ **Evitar:**
```python
# XPath frágil - quebra com mudanças de layout
page.click("//div[@class='container']/button[2]")

# Classes genéricas
page.click(".btn")
```

✅ **Preferir:**
```python
# IDs específicos
page.click("#btn-login")

# Data attributes
page.click("[data-testid='submit-button']")

# Combinações robustas
page.click("button:has-text('Entrar')")
```

---

### 2. **Estrutura de Testes**

Cada teste deve seguir o padrão **AAA (Arrange, Act, Assert)**:

```python
def test_exemplo(page: Page):
    """Descrição clara do que o teste valida"""
    
    # ARRANGE - Preparar o ambiente
    base = Path(__file__).parent
    page.goto((base / "login.html").as_uri())
    
    # ACT - Executar ações
    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")
    
    # ASSERT - Validar resultados
    expect(page).to_have_url((base / "dashboard.html").as_uri())
    expect(page.locator("#welcome")).to_be_visible()
```

---

### 3. **Validações Explícitas**

❌ **Evitar:**
```python
# Validação implícita - não deixa claro o que está sendo testado
page.click("#btn-login")
page.wait_for_timeout(2000)  # Esperar "mágico"
```

✅ **Preferir:**
```python
# Validações explícitas com expect
page.click("#btn-login")
expect(page).to_have_url("dashboard.html")
expect(page.locator("#welcome")).to_be_visible()
```

---

### 4. **Independência de Testes**

❌ **Evitar:**
```python
# Teste 1 depende do Teste 2
def test_login():
    # ...
    
def test_dashboard():
    # Assume que login foi executado antes
    page.goto("dashboard.html")
```

✅ **Preferir:**
```python
# Cada teste é independente
def test_login():
    page.goto("login.html")
    # ... fazer login ...
    
def test_dashboard():
    page.goto("login.html")
    # ... fazer login ...
    page.goto("dashboard.html")
```

---

### 5. **Dados de Teste**

❌ **Evitar:**
```python
# Dados espalhados no código
page.fill("#email", "user@test.com")
page.fill("#senha", "123456")
```

✅ **Preferir:**
```python
# Dados centralizados
TEST_DATA = {
    "email": "user@test.com",
    "senha": "123456"
}

page.fill("#email", TEST_DATA["email"])
page.fill("#senha", TEST_DATA["senha"])
```

---

## 🏗️ Estrutura de Projeto Recomendada

```
projeto/
├── tests/
│   ├── e2e/
│   │   ├── test_login.py
│   │   ├── test_checkout.py
│   │   └── test_search.py
│   ├── fixtures/
│   │   ├── conftest.py
│   │   └── test_data.py
│   └── pages/
│       ├── login_page.py
│       ├── dashboard_page.py
│       └── base_page.py
├── conftest.py
└── pytest.ini
```

---

## 🔧 Padrão Page Object Model (POM)

Para projetos maiores, use o padrão POM para melhor manutenibilidade:

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = "#email"
        self.senha_input = "#senha"
        self.login_button = "#btn-login"
        self.error_message = "#mensagem"
    
    def navigate(self):
        self.page.goto("login.html")
    
    def fill_credentials(self, email: str, senha: str):
        self.page.fill(self.email_input, email)
        self.page.fill(self.senha_input, senha)
    
    def click_login(self):
        self.page.click(self.login_button)
    
    def get_error_message(self):
        return self.page.locator(self.error_message).text_content()

# test_login.py
def test_login_invalido(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.fill_credentials("invalido@test.com", "senhaerrada")
    login_page.click_login()
    
    assert login_page.get_error_message() == "Credenciais inválidas"
```

---

## ⏱️ Timeouts e Waits

❌ **Evitar:**
```python
# Esperas fixas - lentas e não confiáveis
page.wait_for_timeout(5000)
```

✅ **Preferir:**
```python
# Esperas inteligentes
expect(page.locator("#resultado")).to_be_visible()
page.wait_for_load_state("networkidle")
```

---

## 🐛 Tratamento de Erros

```python
def test_com_tratamento_erro(page: Page):
    try:
        page.goto("login.html")
        page.fill("#email", "user@test.com")
        page.fill("#senha", "123456")
        page.click("#btn-login")
        
        expect(page).to_have_url("dashboard.html")
    except Exception as e:
        print(f"Erro no teste: {e}")
        page.screenshot(path="erro.png")
        raise
```

---

## 📸 Screenshots e Vídeos

```python
# conftest.py
@pytest.fixture(autouse=True)
def screenshot_on_failure(page: Page, request):
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")
```

---

## 🔍 Debugging

### Modo Debug
```bash
python3 -m pytest --pdb  # Para no primeiro erro
```

### Modo Headed (Ver o navegador)
```bash
python3 -m pytest --headed
```

### Modo Slow Motion
```bash
python3 -m pytest --slowmo=1000  # 1 segundo entre ações
```

### Trace
```python
# Ativar trace
page.context.tracing.start(screenshots=True, snapshots=True)

# ... executar teste ...

# Salvar trace
page.context.tracing.stop(path="trace.zip")
```

---

## 📊 Relatórios

### HTML Report
```bash
python3 -m pytest --html=report.html --self-contained-html
```

### JUnit XML (para CI/CD)
```bash
python3 -m pytest --junit-xml=results.xml
```

### Coverage
```bash
python3 -m pytest --cov=src --cov-report=html
```

---

## 🚀 Integração com CI/CD

### GitHub Actions
```yaml
name: E2E Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.14'
      - run: pip install -r requirements.txt
      - run: playwright install
      - run: pytest -v
```

---

## ✅ Checklist para Novos Testes

- [ ] Teste tem nome descritivo
- [ ] Teste possui docstring explicando seu propósito
- [ ] Teste segue padrão AAA (Arrange, Act, Assert)
- [ ] Seletores são confiáveis (IDs ou data-testid)
- [ ] Teste é independente de outros testes
- [ ] Validações são explícitas com `expect()`
- [ ] Dados de teste estão centralizados
- [ ] Teste não usa `wait_for_timeout()` sem motivo
- [ ] Teste trata possíveis erros
- [ ] Teste foi executado e passou localmente

---

## 🎓 Recursos Adicionais

- [Documentação Playwright](https://playwright.dev/python/)
- [Documentação Pytest](https://docs.pytest.org/)
- [Best Practices E2E Testing](https://testingjavascript.com/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

---

## 💡 Dicas Finais

1. **Mantenha testes simples** - Um teste, uma funcionalidade
2. **Use nomes descritivos** - `test_login_com_credenciais_invalidas` é melhor que `test_1`
3. **Documente o porquê** - Não apenas o quê
4. **Revise regularmente** - Testes precisam manutenção como código
5. **Automatize tudo** - Execução, relatórios, deploy
6. **Monitore flakiness** - Testes instáveis são piores que nenhum teste
7. **Colabore** - Compartilhe conhecimento com o time

---

**Última atualização:** 12 de Maio de 2026
