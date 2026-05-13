from pathlib import Path
from playwright.sync_api import Page, expect


def test_busca_produto_inexistente(page: Page):
    """
    Teste E2E: Validar comportamento ao buscar produto que não existe
    
    Fluxo:
    1. Fazer login com credenciais válidas
    2. Validar redirecionamento para página de produtos
    3. Buscar produto inexistente
    4. Validar mensagem de "nenhum produto encontrado"
    5. Validar que não há resultados visíveis
    """
    base_path = Path(__file__).parent
    
    login_path = base_path / "login.html"
    produtos_path = base_path / "produtos.html"
    
    # Etapa 1: Fazer login
    page.goto(login_path.as_uri())
    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")
    
    # Etapa 2: Validar redirecionamento para produtos
    expect(page).to_have_url(produtos_path.as_uri())
    
    # Etapa 3: Buscar produto inexistente
    page.fill("#input-busca", "Produto Inexistente")
    page.click("#btn-buscar")
    
    # Etapa 4: Validar mensagem de "nenhum produto encontrado"
    expect(page.locator("#resultado-busca")).to_have_text("Nenhum produto encontrado.")
    
    # Etapa 5: Validar que não há botão de produto
    expect(page.locator("#produto-notebook")).not_to_be_visible()
