#!/usr/bin/env python3
"""Build excel-app: gabung src parts + inline SheetJS -> index.html.

Urutan: src/01_head.html + src/02_body.html + src/03_script.html +
src/04_grid.html + src/05_io.html
Bagian 03 berisi token --XLSX-- yang diganti isi xlsx.full.min.js.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENDOR = r"C:\Users\alfan.andrianto\Documents\tracking-klaim-ui\vendor\xlsx.full.min.js"

def main():
    parts = ['01_head.html', '02_body.html', '03_script.html', '04_grid.html', '05_io.html']
    out = '\n'.join(open(os.path.join(ROOT, 'src', p), encoding='utf-8').read() for p in parts)
    if '--XLSX--' not in out:
        raise SystemExit('Token --XLSX-- tidak ditemukan')
    lib = open(VENDOR, encoding='utf-8').read()
    out = out.replace('--XLSX--', lib)
    dest = os.path.join(ROOT, 'index.html')
    open(dest, 'w', encoding='utf-8').write(out)
    print(f'OK -> index.html ({len(out)} bytes)')

if __name__ == '__main__':
    main()
