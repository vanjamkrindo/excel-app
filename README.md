# Excel — Aplikasi Spreadsheet (tahap HTML)

Aplikasi spreadsheet ala Microsoft Excel: **satu file HTML offline** yang bisa
membaca dan menulis file `.xlsx`. Tahap pertama dari rencana "Excel versi Android APK" —
setelah ini dibungkus jadi APK via WebView/Capacitor.

## Cara pakai
Buka `index.html` di Chrome/Edge (bisa langsung double-click). Semua jalan offline,
tanpa internet.

- **Buka** (ikon folder) → pilih file `.xlsx/.xls/.csv`
- **Simpan** (ikon disket) → unduh file `.xlsx`
- **Buku baru** (ikon kertas) → mulai lembar kosong
- **Mode gelap** (ikon bulan) di pojok kanan atas
- Klik sel untuk pilih; ketik langsung di **formula bar**; panah untuk pindah sel;
  `Delete` untuk hapus.
- Rumus: mulai dengan `=` — dukung `+ - * / ^`, tanda kurung, dan fungsi
  `SUM, AVERAGE, MIN, MAX, COUNT, ABS, ROUND, SQRT` serta referensi/range
  seperti `A1`, `B2:B4`.

## Bangun ulang
```
python tools/build.py
```
Menyalin `src/` (5 bagian, urutan: 01_head → 02_body → 03_script → 04_grid → 05_io)
dan meng-inline `xlsx.full.min.js` dari `tracking-klaim-ui/vendor`.

## Status terverifikasi
- Grid render + navigasi sel ✓
- Rumus dievaluasi benar (contoh: `=B2*C2`→60000, `=SUM(...)`→30000) ✓
- **Save** menghasilkan `.xlsx` valid dengan rumus tersimpan (`=SUM(B1:B3)` dire-read
  dengan `.f` intact) ✓
- **Open** memuat semua sel pada file `.xlsx` riil ✓
- Tanpa referensi eksternal (script/link/webfont di luar file) ✓

## Batasan yang jujur
- Aplikasi ini **membaca sheet pertama** saja, dan **penuh** 26 kolom (A–Z).
- Rumus terbatas pada fungsi dasar di atas; rumus Excel kompleks lain ditulis sebagai
  teks biasa saat dibuka (nilainya diambil dari cache file).
- Tidak ada multi-sheet, formatting intensif, atau chart.

## Menjadi APK Android (langkah berikutnya)
Rute paling ringan tanpa SDK penuh:
1. **Capacitor** (`@capacitor/core` + `@capacitor/cli` + `@capacitor/android`) →
   `npx cap init`, salin `index.html` ke `www/`, `npx cap add android`, `npx cap sync`.
2. Buka `android/` di **Android Studio** → Build → Generate Signed APK.
   (Butuh install Android Studio + Android SDK sekali.)

Alternatif tanpa Android Studio sama sekali: sisipkan halaman ini di file
`index.html` + `assets/www` pada webview via **BuddyBuild**/**PWA** → pakai tool online
seperti **PWABuilder** untuk menghasilkan APK dari PWA.
