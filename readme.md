# Liga Simulasi

Proyek ini adalah simulator liga yang memungkinkan pengguna untuk menjalankan simulasi liga olahraga dengan tim yang memiliki kekuatan berbeda-beda dan bad matchups.

## Fitur

- **Tim dengan Kekuatan yang Dapat Disesuaikan**: Setiap tim memiliki kekuatan yang dapat diatur, yang mempengaruhi probabilitas kemenangannya.
- **Bad Matchups**: Tim dapat memiliki bad matchups terhadap tim lain, yang mempengaruhi hasil pertandingan.
- **Simulasi Liga**: Menjalankan simulasi liga dengan hasil yang berbeda berdasarkan kekuatan tim dan bad matchups.
- **Analisis Hasil**: Mengumpulkan statistik dari simulasi untuk analisis lebih lanjut.

## Struktur Proyek

```
simulator/
│
├── models/
│ ├── team.py # Mendefinisikan tim dan kekuatannya
│ ├── match_resolver.py # Menghitung probabilitas kemenangan
│ ├── league.py # Mengelola liga dan pertandingan
│ └── simulator_manager.py # Menjalankan dan menganalisis simulasi
│
└── main.py # Titik masuk utama untuk menjalankan simulasi
```

## Cara Menggunakan

1. **Instalasi**: Pastikan Anda memiliki Python versi 3.6 atau lebih baru terinstal.
2. **Menjalankan Simulasi**: Jalankan `main.py` untuk memulai simulasi. Anda dapat menyesuaikan tim, jumlah simulasi, dan parameter lainnya di dalam file ini.

    ```bash
    python main.py
    ```

3. **Analisis Hasil**: Setelah simulasi selesai, hasilnya akan ditampilkan di terminal. Anda dapat melihat frekuensi kemenangan setiap tim dan analisis lebih lanjut.

## Kustomisasi

- **Menambahkan Tim**: Edit `main.py` untuk menambah atau mengubah tim dalam simulasi.
- **Mengubah Kekuatan dan Bad Matchups**: Kekuatan dan bad matchups tim dapat diubah di `team.py`.
- **Kustomisasi Simulasi**: Jumlah simulasi dan logika simulasi dapat disesuaikan di `simulator_manager.py`.

## Kontribusi

Kontribusi terhadap proyek ini sangat diterima. Silakan fork repositori ini dan kirimkan pull request Anda.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
