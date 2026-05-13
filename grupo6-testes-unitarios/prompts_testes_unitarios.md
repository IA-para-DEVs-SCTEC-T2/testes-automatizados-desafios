# Prompts Utilizados para Geração de Testes Unitários

## 1. Geração inicial dos testes

> "Gere testes com pytest para a função validar_senha.py. Gere teste com cenários positivos, negativos e limites (edge cases)."

Esse prompt gerou a primeira versão do arquivo `test_validar_senha.py`, com 19 testes organizados em três classes:
- `TestSenhaValida` — cenários positivos
- `TestSenhaInvalida` — cenários negativos
- `TestEdgeCases` — casos limite

---

## 2. Validação das regras de negócio

> "As regras de negócio são essas:
> - Senha com menos de 8 caracteres = Inválida
> - Senha sem letra maiúscula = Inválida
> - Senha sem número = Inválida
> - Senha com 8+ caracteres, pelo menos 1 maiúscula e pelo menos 1 número = Válida
>
> A função está correta?"

Esse prompt revelou dois bugs na implementação original:
- `senha.islower()` não detecta corretamente a ausência de maiúscula quando a senha não contém letras
- `senha.isalpha()` não detecta corretamente a ausência de número quando a senha contém caracteres especiais

---

## 3. Correção da função e atualização dos testes

> "Sim"

Confirmação para corrigir a função e atualizar os testes. A função foi reescrita com verificações corretas:
- `not any(c.isupper() for c in senha)` — detecta ausência de maiúscula
- `not any(c.isdigit() for c in senha)` — detecta ausência de número

Os testes foram atualizados para 22 casos, cobrindo os novos cenários expostos pelos bugs (ex: senha só com símbolos, senha só com números).

---

## 4. Execução dos testes

> "Execute os testes com pytest"

Execução final confirmando **22/22 testes passando** em 0.04s.

---

## Resumo do fluxo

```
Gerar testes → Validar regras de negócio → Corrigir função e testes → Executar testes
```

| Etapa | Resultado |
|---|---|
| Geração inicial | 19 testes criados |
| Revisão das regras | 2 bugs identificados na função |
| Correção | Função e testes reescritos |
| Execução final | ✅ 22/22 testes passando |
