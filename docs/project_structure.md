# Struktur Proyek Flaskkit

Flaskkit dirancang untuk memberikan struktur proyek yang bersih dan terorganisir, mempromosikan pemisahan kekhawatiran (*separation of concerns*) dan memudahkan pemeliharaan serta skalabilitas. Berikut adalah gambaran umum struktur direktori dan file yang dibuat oleh Flaskkit:

```
.
├── app/
│   ├── __init__.py         # Inisialisasi aplikasi Flask dan pendaftaran blueprint
│   ├── extensions.py       # Tempat untuk menginisialisasi ekstensi Flask (misal: SQLAlchemy)
│   ├── blueprints.py       # Definisi Blueprint untuk modul aplikasi
│   ├── controllers/        # Logika utama untuk menangani permintaan dan mengembalikan respons (sering disebut views)
│   │   └── counter_controller.py
│   ├── routes/             # Definisi rute dan penghubung ke controller yang sesuai
│   │   └── counter_routes.py
│   ├── services/           # Logika bisnis yang dapat digunakan kembali, terpisah dari controllers
│   ├── models/             # Definisi model database (jika menggunakan ORM seperti SQLAlchemy)
│   ├── templates/          # File template Jinja2 untuk UI
│   │   ├── base.html
│   │   └── counter.html
│   └── static/             # Aset statis seperti CSS, JavaScript, gambar
│       ├── css/
│       │   ├── input.css   # Input CSS Tailwind
│       │   └── style.css   # Output CSS Tailwind yang dikompilasi
│       └── js/
│           ├── counter.js  # Contoh JavaScript untuk fungsionalitas UI
│           └── effects.js  # Contoh JavaScript untuk efek visual
├── config/
│   ├── __init__.py         # File inisialisasi paket Python
│   └── default.py          # Konfigurasi aplikasi default
├── main.py                 # Titik masuk utama aplikasi Flask
├── requirements.txt        # Dependensi Python yang diperlukan
├── .env                    # Variabel lingkungan untuk konfigurasi lokal
├── package.json            # Konfigurasi proyek Node.js/npm, termasuk skrip build Tailwind
├── tailwind.config.js      # Konfigurasi Tailwind CSS
└── postcss.config.js       # Konfigurasi PostCSS untuk Tailwind CSS dan Autoprefixer
```

### Penjelasan Komponen Utama

* **`app/`**: Ini adalah inti aplikasi Flask Anda.

  * **`__init__.py`**: Mengandung fungsi `create_app()` yang menginisialisasi aplikasi Flask, memuat konfigurasi, menginisialisasi ekstensi, dan mendaftarkan *blueprint*.
  * **`extensions.py`**: Tempat yang direkomendasikan untuk menginisialisasi objek ekstensi Flask (`db = SQLAlchemy()`).
  * **`blueprints.py`**: Mendefinisikan *blueprint* Flask, yang memungkinkan Anda mengorganisir aplikasi menjadi komponen-komponen yang lebih kecil dan modular.
  * **`controllers/`**: Berisi fungsi yang menerima permintaan HTTP dan mengembalikan respons. Mereka bertanggung jawab untuk berinteraksi dengan layanan dan model.
  * **`routes/`**: Mendefinisikan URL endpoint dan memetakannya ke fungsi *controller* yang sesuai.
  * **`services/`**: Ideal untuk menempatkan logika bisnis yang kompleks yang tidak secara langsung terkait dengan penanganan permintaan HTTP atau interaksi database. Ini membantu menjaga *controller* tetap ramping.
  * **`models/`**: Berisi definisi model basis data Anda, mewakili tabel-tabel dalam database dan hubungan antar mereka.
  * **`templates/`**: Direktori ini menyimpan semua file HTML (template Jinja2) yang akan dirender oleh aplikasi Anda.
  * **`static/`**: Menyimpan semua aset statis yang disajikan langsung oleh web server (CSS, JavaScript, gambar, dll.).
* **`config/`**: Direktori ini menyimpan berbagai konfigurasi aplikasi Anda.

  * **`default.py`**: Berisi kelas konfigurasi default dengan pengaturan seperti `DEBUG`, `SECRET_KEY`, dan `SQLALCHEMY_DATABASE_URI`.
* **`main.py`**: File entry point utama untuk menjalankan aplikasi Flask Anda.
* **`requirements.txt`**: Daftar semua paket Python yang dibutuhkan oleh proyek, yang dapat diinstal menggunakan `pip`.
* **`.env`**: File untuk menyimpan variabel lingkungan sensitif atau konfigurasi khusus lingkungan (misal: kunci API, kredensial database).
* **`package.json`**: File manifest untuk proyek Node.js Anda, mengelola dependensi frontend (seperti Tailwind CSS) dan skrip build.
* **`tailwind.config.js` & `postcss.config.js`**: File konfigurasi untuk Tailwind CSS dan PostCSS, memungkinkan penyesuaian styling frontend.

Struktur ini dirancang untuk memberikan fondasi yang kuat untuk proyek Flask apa pun, dari aplikasi kecil hingga skala besar.
