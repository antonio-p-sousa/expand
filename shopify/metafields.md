# Shopify — configuração do catálogo

## Metafields de produto (Definições → Dados personalizados → Produtos)

| Nome | Namespace/key | Tipo | Uso |
|---|---|---|---|
| Número da edição | `custom.numero_da_edicao` | Texto (linha única) | Numeração manual da garrafa (ex.: `0047/1990`). Mostrado em destaque na página de produto pelo snippet `kultu-edicao`. |
| Lenda da caveira | `custom.lenda` | Texto (multi-linha) | Descrição longa/narrativa da peça, separada do body para poder ter layout próprio. |

## Regras de catálogo

- **1 garrafa = 1 produto** — sem variantes; `Default Title` como única opção.
- **SKU**: `KULTU-NNN` (sequencial interno; a numeração artística vai no metafield).
- **Stock**: quantidade 1, tracking Shopify, política `deny` (nunca vender sem stock).
- **Preço**: fixo e igual em toda a edição — definir uma vez e replicar.
- **IVA**: produtos `Taxable`; taxa normal PT (23%) via configuração de impostos da loja.
- **Coleções**:
  - `Kultu Absinto` — automática: `Type = Absinto` E `Disponibilidade = Em stock`... *(nota: coleções automáticas não filtram por stock — usar coleção manual OU automática por tag)*. Recomendado: coleção automática com tag `disponivel`; ao vender, a app de fluxo (Shopify Flow) troca a tag para `esgotado`.
  - `Esgotado / Arquivo` — automática por tag `esgotado`. Template de produto com compra desativada e badge "Peça de coleção — vendida".
- **Automação Flow** (gratuita no Shopify): trigger *Product out of stock* → remover tag `disponivel`, adicionar `esgotado`. Sem Flow, procedimento manual documentado em `docs/operacao-catalogo.md`.

## Importação do CSV (`products_import.csv`)

1. O CSV cria os 39 produtos em **draft** com nomes provisórios (descrição visual) e preço `0.00`.
2. Antes de importar: preencher com a lista final do cliente — Título (`KULTU N.º ___ — Nome`), metafield número, lenda, preço.
3. `Image Src` aponta para o GitHub raw (`raw.githubusercontent.com/antonio-p-sousa/expand/main/...`). **O repo tem de estar público no momento da importação** (ou temporariamente); alternativa: importar sem imagens e carregar em bulk no admin (as imagens estão em `assets/garrafas/`, nomeadas por produto).
4. Depois de validar 2-3 produtos, mudar Status para `active` em bulk.

## Age gate

Ver `liquid/sections/age-gate.liquid` — instalar no tema Savor (Online Store → Themes → Edit code → Sections) e adicionar ao `theme.liquid` logo após `<body>`: `{% section 'age-gate' %}`.
