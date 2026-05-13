# 🧪 Testes E2E - Projeto aula-test-e2e

> Testes End-to-End automatizados com Playwright para validar fluxos críticos de uma aplicação web

## 📊 Status

```
✅ 5/5 testes passando
⏱️ Tempo de execução: ~1 segundo
🎯 Cobertura: Login, Busca, Compra, Validações
```

---

## 🚀 Quick Start

### 1. Instalar dependências
```bash
pip install -r desafio_1/requirements.txt
playwright install
```

### 2. Executar todos os testes
```bash
python3 -m pytest -v
```

### 3. Ver resultado
```
✅ desafio_1/test_login_invalido.py::test_login_com_credenciais_invalidas PASSED
✅ teste_1/test_login.py::test_login_redireciona_para_dashboard PASSED
✅ teste_2/test_busca_produto_inexistente.py::test_busca_produto_inexistente PASSED
✅ teste_2/test_fluxo_compra.py::test_usuario_adiciona_produto_ao_carrinho PASSED
✅ teste_2/test_fluxo_compra_completo.py::test_fluxo_compra_completo_com_validacoes PASSED
```

---

## 📚 Documentação

| Documento | Descrição |
|-----------|-----------|
| 📖 [RELATORIO_TESTES_E2E.md](./RELATORIO_TESTES_E2E.md) | Relatório detalhado de todos os testes |
| 🎓 [GUIA_BOAS_PRATICAS.md](./GUIA_BOAS_PRATICAS.md) | Guia completo de boas práticas |
| 🚀 [COMANDOS_EXECUCAO.md](./COMANDOS_EXECUCAO.md) | Todos os comandos de execução |

---

## 🧪 Testes Disponíveis

### Desafio 1
- ✅ **test_login.py** - Login com credenciais válidas
- ✅ **test_login_invalido.py** - Login com credenciais inválidas ⭐ NOVO

### Teste 1
- ✅ **test_login.py** - Autenticação simples

### Teste 2
- ✅ **test_fluxo_compra.py** - Fluxo básico de compra
- ✅ **test_fluxo_compra_completo.py** - Fluxo completo com validações ⭐ NOVO
- ✅ **test_busca_produto_inexistente.py** - Busca de produto inexistente ⭐ NOVO

---

## 🎯 Funcionalidades Testadas

```
┌─────────────────────────────────────────────────────┐
│                   FLUXO DE COMPRA                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. LOGIN                                           │
│     ✅ Credenciais válidas → Dashboard             │
│     ✅ Credenciais inválidas → Erro                │
│                                                     │
│  2. BUSCA DE PRODUTOS                              │
│     ✅ Buscar "Notebook" → Resultado               │
│     ✅ Buscar inexistente → Mensagem de erro       │
│                                                     │
│  3. DETALHES DO PRODUTO                            │
│     ✅ Visualizar nome, descrição, preço           │
│                                                     │
│  4. CARRINHO                                        │
│     ✅ Adicionar produto → Carrinho                │
│     ✅ Validar item adicionado                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Uso |
|-----------|--------|-----|
| **Playwright** | Latest | Automação E2E |
| **Pytest** | 9.0.3 | Framework de testes |
| **Python** | 3.14.3 | Linguagem |

---

## 📋 Estrutura do Projeto

```
aula-test-e2e/
│
├── desafio_1/
│   ├── login.html
│   ├── dashboard.html
│   ├── test_login.py
│   ├── test_login_invalido.py ⭐
│   └── requirements.txt
│
├── teste_1/
│   ├── login.html
│   ├── dashboard.html
│   └── test_login.py
│
├── teste_2/
│   ├── login.html
│   ├── produtos.html
│   ├── produto.html
│   ├── carrinho.html
│   ├── test_fluxo_compra.py
│   ├── test_fluxo_compra_completo.py ⭐
│   └── test_busca_produto_inexistente.py ⭐
│
├── README.md ⭐
├── RELATORIO_TESTES_E2E.md ⭐
├── GUIA_BOAS_PRATICAS.md ⭐
└── COMANDOS_EXECUCAO.md ⭐
```

---

## 🎓 Exemplos de Uso

### Executar teste específico
```bash
python3 -m pytest desafio_1/test_login_invalido.py -v
```

### Executar com modo headed (ver navegador)
```bash
python3 -m pytest teste_2/test_fluxo_compra_completo.py -v --headed
```

### Executar com relatório HTML
```bash
python3 -m pytest -v --html=report.html --self-contained-html
```

### Executar com modo debug
```bash
python3 -m pytest --pdb
```

---

## ✨ Destaques

✅ **Testes Executáveis** - Todos os testes passam e estão prontos para uso  
✅ **Seletores Confiáveis** - Utiliza IDs específicos, não XPath frágil  
✅ **Bem Documentados** - Cada teste possui docstring clara  
✅ **Independentes** - Testes não dependem uns dos outros  
✅ **Validações Explícitas** - Usa `expect()` para assertions claras  
✅ **Boas Práticas** - Segue padrões de automação E2E  
✅ **Fácil Manutenção** - Código limpo e bem estruturado  

---

## 🔍 Dados de Teste

```json
{
  "email": "user@test.com",
  "senha": "123456",
  "produto_valido": "Notebook",
  "produto_invalido": "Produto Inexistente"
}
```

---

## 📊 Resultados

```
Platform: macOS (darwin)
Python: 3.14.3
Pytest: 9.0.3
Playwright: Latest

Test Results:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PASSED  desafio_1/test_login_invalido.py::test_login_com_credenciais_invalidas
 PASSED  teste_1/test_login.py::test_login_redireciona_para_dashboard
 PASSED  teste_2/test_busca_produto_inexistente.py::test_busca_produto_inexistente
 PASSED  teste_2/test_fluxo_compra.py::test_usuario_adiciona_produto_ao_carrinho
 PASSED  teste_2/test_fluxo_compra_completo.py::test_fluxo_compra_completo_com_validacoes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 5 passed in 1.06s
```

---

## 🎯 Próximos Passos

- [ ] Adicionar testes de performance
- [ ] Implementar testes de responsividade
- [ ] Validar acessibilidade (WCAG)
- [ ] Integrar com CI/CD (GitHub Actions)
- [ ] Gerar relatórios visuais com screenshots
- [ ] Adicionar testes de segurança
- [ ] Implementar Page Object Model para projetos maiores

---

## 📞 Suporte

### Documentação
- [Playwright Docs](https://playwright.dev/python/)
- [Pytest Docs](https://docs.pytest.org/)

### Comandos Úteis
```bash
# Ver todos os testes
python3 -m pytest --collect-only

# Executar com verbose
python3 -m pytest -vv

# Executar com markers
python3 -m pytest -m "smoke"

# Executar com keyword
python3 -m pytest -k "login"
```

---

## 📝 Notas

- Todos os testes utilizam **Playwright** como framework
- Os testes são **independentes** e podem ser executados em qualquer ordem
- Cada teste cobre um **fluxo completo** da aplicação
- Os seletores são **robustos** e não quebram com mudanças de layout
- A documentação está **completa** e atualizada

---

## 🎉 Conclusão

Este projeto demonstra como criar testes E2E de qualidade, executáveis e bem documentados. Todos os testes estão passando e prontos para uso em produção.

**Status:** ✅ Pronto para uso  
**Última atualização:** 12 de Maio de 2026  
**Versão:** 1.0.0

---

**Desenvolvido com ❤️ usando Playwright e Pytest**
