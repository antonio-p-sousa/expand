# KULTU by Shazequin — kultu.pt

Loja Shopify monoproduto para a edição limitada **KULTU by Shazequin**: garrafas-caveira de absinto pintadas à mão pela artista Shazequin. Cada garrafa é uma peça única — SKU único, stock 1, preço fixo.

**Cliente:** Aromas da Tarde Unipessoal Lda · **Projeto:** ExpandTarget (Loop Future) · **Go-Live alvo:** 31/07/2026

## Estrutura do repositório

| Pasta | Conteúdo |
|---|---|
| `assets/garrafas/` | 109 fotos otimizadas para web (1600px, JPEG progressivo), agrupadas por garrafa (`kultu-GG-NN.jpg`). `mapa_fotos.csv` mapeia grupos → fotos originais, com notas de validação. |
| `assets/artista/` | Seleção de 12 fotos do atelier/obras da Shazequin (para páginas A Artista / O Processo). |
| `assets/logos/` | Logos Kultu e KULTU by Shazequin. |
| `content/` | Conteúdo final por página, PT/EN, pronto a colar no Shopify. |
| `content/politicas/` | Rascunhos das políticas legais (privacidade, T&C, envios/devoluções). |
| `shopify/` | `products_import.csv` (39 garrafas), definição de metafields, código Liquid (age gate + numeração). |
| `prototype/` | Protótipo HTML navegável (homepage, produto, lenda, artista) com assets reais — para aprovação de design. Abrir `prototype/index.html` no browser. |
| `docs/` | Guia de operação do catálogo para o cliente. |

## Estado / pendentes do cliente

- [x] ~~Ficha técnica~~ — **70 cl, 80% vol.** (mapa do site v2 do cliente, 14/07)
- [x] ~~Copy das páginas~~ — **copy fechado pelo cliente** (14/07): homepage, produto, A Lenda, A Artista — já integrado em `content/` e no protótipo. EN pendente até fechar o PT.
- [ ] **Lista final de garrafas à venda** — nomes, numeração manual e preço (o CSV usa nomes provisórios e preço placeholder)
- [ ] Validar agrupamento das fotos (`assets/garrafas/mapa_fotos.csv` — 2 grupos marcados VALIDAR)
- [ ] Confirmar se as fotos de 2019 correspondem ao stock atual
- [ ] Foto da artista a trabalhar (pedido do próprio cliente para a página Sobre)
- [ ] Acessos: loja Shopify, domínio kultu.pt, faturação AT
- [ ] Envios: transportadora, prazos, custos, assinatura 18+ na entrega
- [ ] Decisão MB WAY (não bloqueia lançamento)
- [ ] Revisão jurídica das páginas legais antes de publicar (indicação do cliente)

> Age gate: usar o **age verifier nativo do Savor**; recusa deve redirecionar para **fora do site**. A section Liquid custom fica como alternativa.

## Materiais fonte

Os originais (fotos RAW-size, vídeos `KULTU FINAL HD.mp4` e `Chapter I.mp4`, textos .docx) estão na pasta do projeto, fora do repo:
`...\Projetos\Expand\drive-download-20260713T164343Z-2-001\`

> Nota de marca: o uso da marca "Shazequin" está autorizado por acordo escrito para a promoção e venda desta edição (ver docx na pasta Shazequin). Marca "Kultu" registada — Marca Nacional N.º 530779.
