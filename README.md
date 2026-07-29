# KULTU by Shazequin — kultu.pt

Loja Shopify monoproduto para a edição limitada **KULTU by Shazequin**: garrafas-caveira de absinto pintadas à mão pela artista Shazequin. Cada garrafa é uma peça única — SKU único, stock 1, preço fixo.

**Cliente:** Aromas da Tarde Unipessoal Lda · **Projeto:** ExpandTarget (Loop Future) · **Go-Live alvo:** 31/07/2026

## Estrutura do repositório

| Pasta | Conteúdo |
|---|---|
| `assets/produtos/` | **As 160 garrafas finais da loja** (23/07): 1 foto por garrafa, `kultu-NNN.jpg`, em que **NNN = numeração da edição** (nome do ficheiro original do cliente). Otimizadas 1600px. Fotos em expositor de madeira, fundo claro. |
| `assets/garrafas/` | Curadoria das fotos artísticas de 2019 (fundo preto), 39 grupos — úteis para hero/editorial e eventualmente galerias extra, mas **sem mapeamento para a numeração final** (pedir ao cliente se quiser associar). `mapa_fotos.csv` mapeia grupos → fotos originais. |
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
- [x] ~~Lista final de garrafas~~ — **160 garrafas recebidas (23/07)**, numeradas 1-160 pelas fotos; CSV regenerado com os 160 produtos (`shopify/products_import.csv`)
- [x] ~~Acesso Shopify~~ — enviado pelo cliente (23/07)
- [x] ~~Domínio~~ — www.kultu.pt registado (23/07)
- [x] ~~**Preço da edição**~~ — **399 € (PVP, IVA 23% incl.)**, email do cliente 29/07. CSV atualizado nos 160 produtos.
- [x] ~~Fotografias finais HD~~ — **recebidas 28/07**: estúdio, fundo branco, quadradas, **2 vistas por peça** (`assets/produtos-hd/`, 145 peças). Substituem as fotos de telemóvel em `assets/produtos/` (mantidas como fallback).
- [ ] **15 peças sem foto nova** — nºs 9, 56, 60, 80, 107, 108, 111, 118, 129, 137, 138, 140, 148, 150, 159. Foram vendidas/retiradas ou as fotos ficaram por enviar? **Perguntar ao cliente.** (Mantêm a foto antiga entretanto.)
- [ ] **Peça 147** — as fotos novas vieram de outra sessão (fundo preto, vertical) e destoam da grelha; pedir foto em fundo branco.
- [ ] Nomes das garrafas (opcional — títulos atuais: "KULTU N.º NNN"; cliente pode acrescentar nomes)
- [ ] Lendas por garrafa (opcional, metafield preparado)
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
