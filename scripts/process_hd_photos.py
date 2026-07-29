# -*- coding: utf-8 -*-
"""
Pipeline das fotos HD finais entregues pelo cliente (28/07/2026).

Entrada: pasta do cliente com ficheiros `NA.jpg` / `NB.jpg` (N = número da edição
SEM zeros à esquerda, ex. 1A.jpg, 101B.jpg). Algumas peças têm também C e D.
Aceita extensão em maiúsculas (.JPG) e variantes com separador/espaços.

O que faz:
  1. Otimiza para web: corrige orientação EXIF, converte para RGB, reduz para no
     máximo 1600px no lado maior, JPEG progressivo q82 optimize, sem EXIF/ICC
     (os originais são todos sRGB IEC61966-2.1, o default da web).
  2. Escreve em assets/produtos-hd/kultu-NNN-x.jpg (NNN 3 dígitos, sufixo minúsculo).
  3. Atualiza shopify/products_import.csv IN-PLACE no formato multi-imagem Shopify:
     a linha do produto leva a imagem principal (Image Position 1) e cada imagem
     adicional vai numa linha extra que repete só o Handle + Image Src/Position/Alt.
     Peças sem foto nova mantêm a foto antiga de assets/produtos/ (fallback).
  4. Relatório: contagens, tamanhos antes/depois, peças sem foto nova, anomalias.

Uso:
  py -X utf8 scripts/process_hd_photos.py "C:\\caminho\\para\\pasta_fotos_hd"

Nota: para as imagens importarem via CSV o repo tem de estar público no GitHub
(URLs raw). Alternativa: upload manual no admin.
"""
import csv
import os
import re
import sys

from PIL import Image, ImageOps

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_BASE = 'https://raw.githubusercontent.com/antonio-p-sousa/expand/main/assets/'
RAW_HD = RAW_BASE + 'produtos-hd/'
RAW_OLD = RAW_BASE + 'produtos/'

PATTERN = re.compile(r'^\s*(\d{1,3})\s*[-_ ]?\s*([a-d])?\s*\.(?:jpe?g|png)$', re.IGNORECASE)
HANDLE_PATTERN = re.compile(r'^kultu-(\d{3})$')

MAX_SIDE = 1600
JPEG_QUALITY = 82
MIN_EDITION, MAX_EDITION = 1, 160


def dir_size(path):
    if not os.path.isdir(path):
        return 0
    return sum(os.path.getsize(os.path.join(path, f)) for f in os.listdir(path))


def mb(n):
    return f'{n / 1024 / 1024:.1f} MB'


def process_photos(src, outdir):
    """Otimiza as fotos da pasta `src` para `outdir`. Devolve (found, ignorados, anomalias)."""
    os.makedirs(outdir, exist_ok=True)
    found = {}          # n -> [(letra, nome_ficheiro_out)]
    ignorados = []
    anomalias = []

    for f in sorted(os.listdir(src)):
        m = PATTERN.match(f)
        if not m:
            ignorados.append(f)
            continue

        n = int(m.group(1))
        letra = (m.group(2) or 'a').lower()
        if not MIN_EDITION <= n <= MAX_EDITION:
            ignorados.append(f'{f} (número fora de {MIN_EDITION}-{MAX_EDITION})')
            continue

        name = f'kultu-{n:03d}-{letra}.jpg'
        if any(letra == l for l, _ in found.get(n, [])):
            anomalias.append(f'{f}: colisão de nome com {name} (ficheiro duplicado?)')
            continue

        try:
            with Image.open(os.path.join(src, f)) as raw:
                im = ImageOps.exif_transpose(raw).convert('RGB')
        except Exception as exc:  # ficheiro corrompido / formato inesperado
            anomalias.append(f'{f}: ilegível ({exc!r})')
            continue

        largura, altura = im.size
        if largura != altura:
            anomalias.append(f'{f}: não é quadrada ({largura}x{altura})')

        im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        # frombytes descarta info (EXIF/ICC); originais já são sRGB
        limpa = Image.frombytes(im.mode, im.size, im.tobytes())
        limpa.save(os.path.join(outdir, name), 'JPEG',
                   quality=JPEG_QUALITY, optimize=True, progressive=True)
        found.setdefault(n, []).append((letra, name))

    for n in found:
        found[n].sort()
    return found, ignorados, anomalias


def alt_text(n, pos):
    base = (f'Garrafa KULTU by Shazequin N.º {n} — absinto de edição limitada, '
            'caveira pintada à mão')
    return base if pos == 1 else f'{base} (vista {pos})'


def update_csv(csv_path, found):
    """Reescreve o CSV com as imagens novas. Devolve (linhas_produto, linhas_extra, sem_foto)."""
    with open(csv_path, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))

    header, data = rows[0], rows[1:]
    idx = {name: i for i, name in enumerate(header)}
    if 'Image Position' not in idx:
        header.insert(idx['Image Src'] + 1, 'Image Position')
        for r in data:
            r.insert(idx['Image Src'] + 1, '')
        idx = {name: i for i, name in enumerate(header)}

    novas, extra, sem_foto = [], 0, []
    for r in data:
        if not r or not r[idx['Handle']]:
            continue
        # ignora linhas de imagem extra de uma execução anterior (idempotência)
        if not r[idx['Title']]:
            continue

        m = HANDLE_PATTERN.match(r[idx['Handle']])
        n = int(m.group(1)) if m else None
        fotos = found.get(n, [])

        if fotos:
            r[idx['Image Src']] = RAW_HD + fotos[0][1]
            r[idx['Image Position']] = '1'
            r[idx['Image Alt Text']] = alt_text(n, 1)
        else:
            sem_foto.append(n)
            r[idx['Image Src']] = RAW_OLD + f'kultu-{n:03d}.jpg'
            r[idx['Image Position']] = '1'
        novas.append(r)

        for pos, (_letra, nome) in enumerate(fotos[1:], start=2):
            linha = [''] * len(header)
            linha[idx['Handle']] = r[idx['Handle']]
            linha[idx['Image Src']] = RAW_HD + nome
            linha[idx['Image Position']] = str(pos)
            linha[idx['Image Alt Text']] = alt_text(n, pos)
            novas.append(linha)
            extra += 1

    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        w.writerow(header)
        w.writerows(novas)

    return len(novas) - extra, extra, sorted(sem_foto)


def validate(csv_path):
    """Validações finais. Devolve lista de erros (vazia = tudo ok)."""
    with open(csv_path, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    header, data = rows[0], rows[1:]
    idx = {name: i for i, name in enumerate(header)}

    erros = []
    produtos, imagens = [], {}
    for r in data:
        h = r[idx['Handle']]
        imagens.setdefault(h, 0)
        if r[idx['Image Src']]:
            imagens[h] += 1
        if r[idx['Title']]:
            produtos.append(h)
            if r[idx['Variant Price']] != '399.00':
                erros.append(f'{h}: preço {r[idx["Variant Price"]]!r} != 399.00')
        elif r[idx['Variant Price']] or r[idx['Variant SKU']]:
            erros.append(f'{h}: linha extra com dados de variante preenchidos')

    if len(produtos) != 160:
        erros.append(f'{len(produtos)} linhas de produto (esperado 160)')
    if len(set(produtos)) != len(produtos):
        erros.append('handles de produto duplicados')
    sem_img = [h for h, c in imagens.items() if c == 0]
    if sem_img:
        erros.append(f'produtos sem imagem: {sem_img}')
    return erros, len(produtos), len(set(produtos)), len(data)


def main(src):
    outdir = os.path.join(REPO, 'assets', 'produtos-hd')
    csv_path = os.path.join(REPO, 'shopify', 'products_import.csv')

    antes = sum(os.path.getsize(os.path.join(src, f)) for f in os.listdir(src))
    found, ignorados, anomalias = process_photos(src, outdir)
    depois = dir_size(outdir)

    total = sum(len(v) for v in found.values())
    print(f'{total} fotos processadas para {len(found)} peças')
    print(f'Tamanho: {mb(antes)} -> {mb(depois)} '
          f'({100 - depois * 100 / antes:.0f}% menos)')

    produtos, extra, sem_foto = update_csv(csv_path, found)
    print(f'CSV: {produtos} linhas de produto + {extra} linhas de imagem extra')

    if sem_foto:
        print(f'SEM FOTO NOVA ({len(sem_foto)}) — mantêm assets/produtos/: {sem_foto}')
    if anomalias:
        print(f'Anomalias ({len(anomalias)}): ' + '; '.join(anomalias))
    if ignorados:
        print(f'Ignorados ({len(ignorados)}): {ignorados[:20]}')

    erros, n_prod, n_uniq, n_linhas = validate(csv_path)
    print(f'Validação: {n_linhas} linhas de dados, {n_prod} produtos ({n_uniq} handles distintos)')
    print('Validação OK' if not erros else 'ERROS:\n  ' + '\n  '.join(erros))
    return 1 if erros else 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Uso: py scripts/process_hd_photos.py <pasta_fotos_hd>')
    sys.exit(main(sys.argv[1]))
