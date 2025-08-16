# Perintah CLI Flaskkit

Flaskkit menyediakan serangkaian perintah *command-line interface* (CLI) untuk membantu Anda mengelola proyek Flask Anda.

## `flaskkit start`

Perintah ini digunakan untuk membuat proyek Flaskkit baru.

### Penggunaan

```bash
flaskkit start <NAMA_PROYEK> [--yes|-y]
```

### Argumen

* **NAMA\_PROYEK** (opsional): Nama direktori proyek yang akan dibuat. Jika tidak disediakan, nama defaultnya adalah `flask_kit`.
* **-y, --yes** (opsional): Jika flag ini digunakan, Flaskkit akan secara otomatis menginstal semua dependensi Python (dari `requirements.txt`) dan Node.js/npm (untuk Tailwind CSS) setelah proyek dibuat. Jika tidak digunakan, Anda harus menginstalnya secara manual nanti.

### Contoh

Membuat proyek baru bernama `my_flask_app` dan menginstal dependensi secara otomatis:

```bash
flaskkit start my_flask_app -y
```

## `flaskkit run`

Perintah ini digunakan untuk menjalankan berbagai tugas pembantu (*helper tasks*) di dalam proyek Flaskkit Anda.

### Penggunaan

```bash
flaskkit run <TASK> [--path|-p PATH_PROYEK]
```

### Argumen

* **<TASK>** (wajib): Tugas yang ingin Anda jalankan. Pilihan yang tersedia adalah:

  * `build:css`: Mengompilasi file CSS Tailwind dari `input.css` ke `style.css` dan melakukan minification.
  * `build:key`: Menghasilkan `SECRET_KEY` acak yang baru dan memperbarui file `.env` proyek Anda. Ini penting untuk keamanan aplikasi Flask Anda di lingkungan produksi.
* **--path, -p** (opsional): Jalur ke direktori proyek Flaskkit Anda. Defaultnya adalah direktori kerja saat ini (`.`).

### Contoh

Mengompilasi ulang CSS di proyek saat ini:

```bash
flaskkit run build:css
```

Menghasilkan `SECRET_KEY` baru untuk proyek di folder `my_flask_app`:

```bash
flaskkit run build:key -p my_flask_app
```
