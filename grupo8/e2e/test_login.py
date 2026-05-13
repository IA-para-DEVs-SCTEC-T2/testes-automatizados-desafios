import re
import pytest
from playwright.sync_api import Page, expect
from pathlib import Path


BASE_URL = Path(__file__).parent.resolve().as_uri()
LOGIN_URL = f"{BASE_URL}/login.html"
DASHBOARD_URL = f"{BASE_URL}/dashboard.html"


# ---------------------------------------------------------------------------
# Testes existentes
# ---------------------------------------------------------------------------

def test_login_sucesso_redireciona_para_dashboard(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url(re.compile(r"dashboard\.html"))
    expect(page.locator("#btn-logout")).to_be_visible()


def test_login_falha_exibe_mensagem_credenciais_invalidas(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "user2@test.com")
    page.fill("#senha", "abcdef")
    page.click("#btn-login")

    expect(page).to_have_url(re.compile(r"login\.html"))
    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")


# ---------------------------------------------------------------------------
# Testes de UI/estado da página de login
# ---------------------------------------------------------------------------

def test_campos_email_e_senha_visiveis_e_habilitados(page: Page):
    page.goto(LOGIN_URL)

    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#email")).to_be_enabled()
    expect(page.locator("#senha")).to_be_visible()
    expect(page.locator("#senha")).to_be_enabled()


def test_mensagem_erro_vazia_ao_carregar_pagina(page: Page):
    page.goto(LOGIN_URL)

    expect(page.locator("#mensagem")).to_have_text("")


def test_login_com_campos_vazios_nao_redireciona(page: Page):
    page.goto(LOGIN_URL)

    page.click("#btn-login")

    expect(page).to_have_url(re.compile(r"login\.html"))
    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")


# ---------------------------------------------------------------------------
# Testes de conteúdo
# ---------------------------------------------------------------------------

def test_titulo_pagina_login(page: Page):
    page.goto(LOGIN_URL)

    expect(page).to_have_title("Login")


def test_titulo_pagina_dashboard(page: Page):
    page.goto(DASHBOARD_URL)

    expect(page).to_have_title("Dashboard")


def test_mensagem_boas_vindas_no_dashboard(page: Page):
    page.goto(LOGIN_URL)

    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url(re.compile(r"dashboard\.html"))
    expect(page.locator("#welcome-message")).to_have_text("Usuário autenticado com sucesso.")


# ---------------------------------------------------------------------------
# Testes de fluxo
# ---------------------------------------------------------------------------

def test_login_falha_depois_sucesso_redireciona_corretamente(page: Page):
    page.goto(LOGIN_URL)

    # Primeira tentativa com credenciais inválidas
    page.fill("#email", "user2@test.com")
    page.fill("#senha", "abcdef")
    page.click("#btn-login")

    expect(page.locator("#mensagem")).to_have_text("Credenciais inválidas")

    # Segunda tentativa com credenciais válidas
    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url(re.compile(r"dashboard\.html"))
    expect(page.locator("#btn-logout")).to_be_visible()
