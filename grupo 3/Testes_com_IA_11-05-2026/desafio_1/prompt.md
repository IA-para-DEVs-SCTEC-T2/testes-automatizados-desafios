# Prompt de Resposta - Análise de Testes de Validação de Senha

## Prompt do Usuário

Tenha em vista que:

**Regras de negócio:**
- Senha com menos de 8 caracteres = Inválida
- Senha sem letra maiúscula = Inválida
- Senha sem número = Inválida
- Senha com 8+ caracteres, pelo menos 1 maiúscula e pelo menos 1 número = Válida

**Responda:**
- Quais regras tornam a senha inválida?
- Quais cenários precisam ser protegidos pelos testes?

---

## Resposta

Baseado nas regras de negócio apresentadas, vou analisar:

### **Regras que tornam a senha inválida:**

1. **Menos de 8 caracteres** - qualquer senha com 7 ou menos caracteres é inválida
2. **Ausência de letra maiúscula** - senha sem pelo menos uma letra maiúscula é inválida
3. **Ausência de número** - senha sem pelo menos um dígito numérico é inválida

### **Cenários que precisam ser protegidos pelos testes:**

#### ✅ **Cenários já cobertos:**
- ✅ Senha muito curta (< 8 caracteres)
- ✅ Senha sem maiúscula
- ✅ Senha sem número
- ✅ Senha válida mínima (8 caracteres, maiúscula e número)
- ✅ Senha válida longa

#### ⚠️ **Cenários que FALTAM ser testados:**

1. **Senha com exatamente 8 caracteres válida** - testar o limite mínimo
2. **Senha com 7 caracteres mas com maiúscula e número** - deve ser inválida (testa prioridade da regra de tamanho)
3. **Senha vazia** - caso extremo
4. **Senha só com números** - sem letras
5. **Senha só com maiúsculas** - sem números
6. **Senha com caracteres especiais** - validar se são permitidos
7. **Senha com espaços** - validar comportamento
8. **Senha com múltiplas maiúsculas** - garantir que funciona
9. **Senha no limite (7 caracteres)** - testar o boundary exato da regra

### **Observação importante:**

Olhando o código atual de `validar_senha()`, há um **bug potencial**:

```python
if senha.islower():  # Retorna True se TODAS as letras são minúsculas
    return False
```

Isso significa que uma senha como `"12345678"` (só números) passaria neste teste, pois `islower()` retorna `False` para strings sem letras. O teste deveria verificar explicitamente a presença de pelo menos uma maiúscula.
