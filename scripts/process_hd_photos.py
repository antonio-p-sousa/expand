# -*- coding: utf-8 -*-
"""
Pipeline das fotos HD finais (quando o cliente entregar a pasta).

Espera ficheiros nomeados NNN-a.jpg, NNN-b.jpg, ... (número da garrafa + letra do ângulo),
conforme nomenclatura combinada no doc de requisitos de 23/07. Aceita também "NNN a.jpg",
"NNNa.jpg" e variantes com espaços.

O que faz:
  1. Corrige orientação EXIF, otimiza para web (1600px, JPEG progressivo q82)
  2. Escreve em assets/produtos-hd/kultu-NNN-X.jpg
  3. Gera shopify/images_update.csv para importação Shopify (Handle + Image Src/Position)
     — a importação por CSV com o mesmo Handle ADICIONA/substitui imagens dos produtos existentes.
  4. Relatório: garrafas sem foto, fotos sem garrafa (fora de 1-160), contagens por ângulo.

Uso:
  py -X utf8 scripts/process_hd_photos.py "C:\\caminho\\para\\pasta_fotos_hd"

Nota: para as imagens importarem via CSV o repo tem de estar público no GitHub
(URLs raw). Alternativa: upload manual no admin.
"""
import os, re, sys, csv
from PIL import Image, ImageOps

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = 'https://raw.githubusercontent.com/antonio-p-sousa/expand/main/assets/produtos-hd/'
PATTERN = re.compile(r'^\s*(\d{1,3})\s*[-_ ]?\s*([a-dA-D])?\s*\.(jpe?g|png)$')

def main(src):
    outdir = os.path.join(REPO, 'assets', 'produtos-hd')
    os.makedirs(outdir, exist_ok=True)
    found = {}          # n -> [(letra, ficheiro_out)]
    ignorados = []
    for f in sorted(os.listdir(src)):
        m = PATTERN.match(f)
        if not m:
            ignorados.append(f)
            continue
        n = int(m.group(1))
        letra = (m.group(2) or 'a').lower()
        if not 1 <= n <= 160:
            ignorados.append(f + ' (número fora de 1-160)')
            continue
        im = Image.open(os.path.join(src, f))
        im = ImageOps.exif_transpose(im).convert('RGB')
        im.thumbnail((1600, 1600))
        name = f'kultu-{n:03d}-{letra}.jpg'
        im.save(os.path.join(outdir, name), 'JPEG', quality=82, optimize=True, progressive=True)
        found.setdefault(n, []).append((letra, name))

    # CSV de atualização de imagens (Handle repetido = múltiplas imagens)
    out_csv = os.path.join(REPO, 'shopify', 'images_update.csv')
    with open(out_csv, 'w', newline='', encoding='utf-8-sig') as fh:
        w = csv.writer(fh)
        w.writerow(['Handle', 'Image Src', 'Image Position', 'Image Alt Text'])
        for n in sorted(found):
            for pos, (letra, name) in enumerate(sorted(found[n]), 1):
                w.writerow([f'kultu-{n:03d}', RAW + name, pos,
                            f'Garrafa KULTU N.º {n} — vista {letra}'])

    sem_foto = [n for n in range(1, 161) if n not in found]
    total = sum(len(v) for v in found.values())
    print(f'{total} fotos processadas para {len(found)} garrafas')
    print(f'CSV: {out_csv}')
    if sem_foto:
        print(f'ATENÇÃO — {len(sem_foto)} garrafas sem foto HD: {sem_foto}')
    if ignorados:
        print(f'Ignorados ({len(ignorados)}): {ignorados[:20]}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Uso: py scripts/process_hd_photos.py <pasta_fotos_hd>')
    main(sys.argv[1])
