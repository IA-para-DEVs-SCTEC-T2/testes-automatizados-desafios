from pathlib import Path
from playwright.sync_api import Page, expect


def test_fluxo_compra_completo_com_validacoes(page: Page):
    """
    Teste E2E: Validar fluxo completo de compra com todas as validações
    
    Fluxo:
    1. Fazer login com credenciais válidas
    2. Validar redirecionamento para página de produtos
    3. Buscar produto específico
    4. Validar resultado da busca
    5. Clicar no produto
    6. Validar página de detalhes
    7. Validar informações do produto
    8. Adicionar ao carrinho
    9. Validar redirecionamento para carrinho
    10. Validar item no carrinho
    """
    base_path = Path(__file__).parent
    
    login_path = base_path / "login.html"
    produtos_path = base_path / "produtos.html"
    produto_path = base_path / "produto.html"
    carrinho_path = base_path / "carrinho.html"
    
    # Etapa 1: Fazer login
    page.goto(login_path.as_uri())
    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")
    
    # Etapa 2: Validar redirecionamento para produtos
    expect(page).to_have_url(produtos_path.as_uri())
    
    # Etapa 3: Buscar produto
    page.fill("#input-busca", "Notebook")
    page.click("#btn-buscar")
    
    # Etapa 4: Validar resultado da busca
    expect(page.locator("#produto-notebook")).to_be_visible()
    
    # Etapa 5: Clicar no produto
    page.click("#produto-notebook")
    
    # Etapa 6: Validar página de detalhes
    expect(page).to_have_url(produto_path.as_uri())
    
    # Etapa 7: Validar informações do produto
    expect(page.locator("#produto-nome")).to_have_text("Notebook")
    expect(page.locator("#produto-descricao")).to_have_text("Notebook para estudos, trabalho e navegação.")
    expect(page.locator("#produto-preco")).to_have_text("R$ 3500,00")
    
    # Etapa 8: Adicionar ao carrinho
    page.click("#btn-add-cart")
    
    # Etapa 9: Validar redirecionamento para carrinho
    expect(page).to_have_url(carrinho_path.as_uri())
    
    # Etapa 10: Validar item no carrinho
    expect(page.locator("#item-carrinho")).to_have_text("Notebook")
    expect(page.locator("#btn-finalizar-compra")).to_be_visible()
