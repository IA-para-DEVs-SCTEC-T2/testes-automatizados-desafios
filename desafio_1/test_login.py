from pathlib import Path
from playwright.sync_api import Page, expect


BASE = Path(__file__).parent
LOGIN_URL = (BASE / "login.html").as_uri()
DASHBOARD_URL = (BASE / "dashboard.html").as_uri()


def test_login_valido_redireciona_para_dashboard(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url(DASHBOARD_URL)
    expect(page.locator("#btn-logout")).to_be_visible()


def test_login_invalido_exibe_mensagem_de_erro(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "invalido@test.com")
    page.fill("#senha", "senhaerrada")
    page.click("#btn-login")

    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")
    expect(page).not_to_have_url(DASHBOARD_URL)


def test_login_email_correto_senha_errada_exibe_mensagem_de_erro(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "user@test.com")
    page.fill("#senha", "senhaerrada")
    page.click("#btn-login")

    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")
    expect(page).not_to_have_url(DASHBOARD_URL)


def test_login_email_errado_senha_correta_exibe_mensagem_de_erro(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "errado@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")
    expect(page).not_to_have_url(DASHBOARD_URL)


def test_login_campos_vazios_exibe_mensagem_de_erro(page: Page):
    page.goto(LOGIN_URL)

    page.click("#btn-login")

    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")
    expect(page).not_to_have_url(DASHBOARD_URL)


def test_logout_exibe_botao_sair_no_dashboard(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url(DASHBOARD_URL)
    expect(page.locator("#btn-logout")).to_be_visible()
    expect(page.locator("#welcome-message")).to_have_text("Usuário autenticado com sucesso.")
