# Fotografias HD dos produtos KULTU

Fotos finais de estúdio das garrafas-caveira, para usar na loja.

## Origem

Pasta entregue pelo cliente a **28/07/2026**:
`2026.07.28 - Fotos Produtos Colocar Site - KULTU by shazequin`

Nomenclatura na origem: `NA.jpg` / `NB.jpg`, em que `N` é o número da edição **sem
zeros à esquerda** (ex.: `1A.jpg`, `101B.jpg`). A letra é o ângulo. Algumas peças
trazem também `C` e `D`. A numeração é a mesma das fotos antigas
(`1A.jpg` = `assets/produtos/kultu-001.jpg`).

## Convenção de nomes neste repo

```
kultu-NNN-x.jpg
        │   └── ângulo: a, b, c, d (minúsculas) → Image Position 1, 2, 3, 4
        └────── número da edição com 3 dígitos (001–160)
```

## Processamento

Feito por `scripts/process_hd_photos.py` (a pasta de origem não é modificada):

- orientação EXIF corrigida, convertido para RGB
- máximo **1600 px** no lado maior (não faz upscale)
- JPEG progressivo, **qualidade 82**, `optimize=True`
- metadados removidos (EXIF e perfil ICC — os originais são todos
  sRGB IEC61966-2.1, que é o default assumido pelos browsers)

Resultado: **297 ficheiros** para **145 peças**, 172,7 MB → 40,3 MB (−77%).

As dimensões finais mais comuns são 1500×1500, 1200×1200 e 1400×1400, herdadas
do original.

## Peças SEM foto nova (15)

Estas mantêm no CSV a foto antiga de `assets/produtos/kultu-NNN.jpg`
(por isso essa pasta **não pode ser apagada** — é o fallback):

```
9, 56, 60, 80, 107, 108, 111, 118, 129, 137, 138, 140, 148, 150, 159
```

## Nota sobre a peça 147

`147A` / `147B` vêm de uma sessão fotográfica diferente das restantes: fundo
**preto**, formato vertical 4788×7174 (redimensionado para 1068×1600), em vez do
fundo branco quadrado de estúdio usado nas outras 144 peças. Fica visualmente
inconsistente na grelha da loja — vale a pena pedir ao cliente a foto em fundo
branco.
