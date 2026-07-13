# Guia de operação do catálogo — KULTU

> Para o cliente (Aromas da Tarde). Como gerir garrafas, encomendas e expedição no dia-a-dia, sem apoio técnico.

## Adicionar uma nova garrafa

1. **Fotos**: mínimo 2 (frente + detalhe), fundo preto, seguindo o padrão das existentes.
2. Shopify Admin → Produtos → **Adicionar produto**.
3. Preencher seguindo o template (`content/produto-template.md`):
   - Título: `KULTU N.º [número] — [Nome da peça]`
   - Descrição: curta + lenda + ficha técnica + aviso legal (duplicar de um produto existente e editar)
   - Metafields: **Número da edição** e **Lenda da caveira**
   - Preço: o preço fixo da edição
   - Inventário: **quantidade 1**, "Track quantity" ativo, NÃO permitir venda sem stock
   - SKU: `KULTU-NNN` (seguinte na sequência)
   - Tag: `disponivel`
4. Estado: **Ativo** → a garrafa entra automaticamente na coleção Kultu Absinto.

## Quando uma garrafa é vendida

- O stock passa a 0 automaticamente — a peça deixa de ser comprável.
- Com o Shopify Flow configurado, a tag muda de `disponivel` para `esgotado` e a peça passa para a coleção **Esgotado/Arquivo**.
- Sem Flow (manual): Produtos → abrir a garrafa vendida → remover tag `disponivel`, adicionar `esgotado`.
- **Nunca apagar** produtos vendidos — o arquivo reforça a exclusividade da edição.

## Expedir uma encomenda

1. Notificação de venda chega por email.
2. Admin → Encomendas → abrir a encomenda; confirmar pagamento **Pago** e a fatura emitida (automática).
3. Embalar seguindo o procedimento de embalagem protetora (peça única — sem substituição!).
4. Marcar como **Enviada** com o código de seguimento → o comprador recebe email de tracking.
5. Lembrete: a transportadora não entrega a menores de 18.

## O que NUNCA fazer

- Alterar a quantidade de stock para mais de 1
- Reutilizar um SKU ou número de edição
- Vender fora do site sem dar baixa imediata do produto (risco de venda dupla)
- Apagar produtos vendidos
