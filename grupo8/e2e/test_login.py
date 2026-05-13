import re
import pytest
from playwright.sync_api import Page, expect
from pathlib import Path


BASE_URL = Path(__file__).parent.resolve().as_uri()
LOGIN_URL = f"{BASE_URL}/login.html"


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
