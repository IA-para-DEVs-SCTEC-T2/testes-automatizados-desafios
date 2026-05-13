from pathlib import Path
from playwright.sync_api import Page, expect


def test_login_com_credenciais_invalidas(page: Page):
    """
    Teste E2E: Validar mensagem de erro ao fazer login com credenciais inválidas
    
    Fluxo:
    1. Navegar para página de login
    2. Preencher email inválido
    3. Preencher senha inválida
    4. Clicar em "Entrar"
    5. Validar mensagem de erro
    6. Validar que não redireciona para dashboard
    """
    base = Path(__file__).parent
    login_url = (base / "login.html").as_uri()
    
    # Etapa 1: Navegar para login
    page.goto(login_url)
    
    # Etapa 2-3: Preencher credenciais inválidas
    page.fill("#email", "invalido@test.com")
    page.fill("#senha", "senhaerrada")
    
    # Etapa 4: Clicar em "Entrar"
    page.click("#btn-login")
    
    # Etapa 5: Validar mensagem de erro
    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")
    
    # Etapa 6: Validar que continua na página de login
    expect(page).to_have_url(login_url)
