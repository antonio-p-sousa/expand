# Avisos legais — venda de bebidas alcoólicas

> Base legal PT: DL n.º 106/2015 (proibição de venda/disponibilização de bebidas alcoólicas a menores de 18 anos, incl. venda à distância). Rever com apoio jurídico antes do Go-Live.

## Age gate (entrada do site) — redação fechada pelo cliente (14/07)

- Texto: **Este site vende bebidas alcoólicas. Para continuar, confirme que tem 18 anos ou mais.**
- Botões: `Tenho 18 anos ou mais` / `Não tenho 18 anos`
- Recusa → **redirecionar para fora do site** (ex.: google.com) — nunca para uma página de erro dentro da loja *(indicação explícita do cliente)*.
- Nota Savor: o tema traz **age verifier nativo** — usar o nativo por defeito; a section Liquid custom (`shopify/liquid/sections/age-gate.liquid`) fica como alternativa se o nativo não cobrir a redação/comportamento.

## Avisos permanentes — redação fechada pelo cliente

- Rodapé (todas as páginas): **Aprecie com responsabilidade. Venda proibida a menores de 18 anos.**
  *(Nota do cliente: "Beba com moderação" é compromisso de autorregulação do setor, não imposição legal direta — a redação escolhida é "Aprecie com responsabilidade".)*
- Ficha de produto: **Confirmação de idade obrigatória antes da compra. Venda proibida a menores de 18 anos. Consuma com responsabilidade.**
- Checkout: nota de confirmação de idade — *Ao concluir a compra confirma que tem 18 anos ou mais. A entrega pode exigir comprovação de idade.*

## Confirmação na entrega

Incluir nas condições de envio: a transportadora pode exigir documento de identificação na entrega; encomendas não são entregues a menores.
