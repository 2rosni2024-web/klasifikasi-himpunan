# Sistem Klasifikasi Data dengan Himpunan

Aplikasi web untuk mengelompokkan mahasiswa berdasarkan bidang minat (Pemrograman, Desain, Jaringan) menggunakan konsep himpunan. Proyek PJBL-2, Kelompok E (Grup E-Ilkom).

**Link web:** https://2rosni2024-web.github.io/klasifikasi-himpunan/

## Kategori

- **A** = minat Pemrograman
- **B** = minat Desain
- **C** = minat Jaringan
- **U** = seluruh mahasiswa pada dataset

## Fitur

- Dua dataset contoh: 12 mahasiswa (M01-M12) dan 10 peserta (P01-P10)
- Input data lewat form dan unggah file CSV
- Operasi himpunan: union (X ∪ Y), irisan (X ∩ Y), selisih (X − Y), dan komplemen (X')
- Diagram Venn otomatis (SVG) untuk tiga himpunan, dengan daerah hasil operasi berwarna kuning
- Prinsip Inklusi-Eksklusi untuk dua dan tiga himpunan, dibandingkan dengan hitungan langsung
- Pengujian otomatis pada dua dataset (14 uji)

## Format CSV

Kolom: `id,nama,angkatan,minat`. Pisahkan beberapa minat dengan tanda `|`.

```
id,nama,angkatan,minat
M01,Rina,2024,A|B
M02,Budi,2024,A
M12,Lina,2025,
```

## Struktur repository

| File | Keterangan |
|------|------------|
| `index.html` | Aplikasi web (HTML, CSS, JavaScript) |
| `uji_himpunan.py` | Pengujian dengan `set` Python pada dua dataset |
| `README.md` | Dokumentasi proyek |

## Menjalankan pengujian Python

```
python uji_himpunan.py
```

Hasil akhir yang diharapkan: `SEMUA UJI LULUS`.

## Teknologi

- HTML, CSS, JavaScript (objek `Set`)
- Diagram Venn: SVG buatan sendiri
- Pengujian: JavaScript (di web) dan Python (`set`)
- Kontrol versi dan hosting: GitHub dan GitHub Pages

## Anggota Kelompok E

| No | Nama | NIM | Peran |
|----|------|-----|-------|
| 1 | Zulfikril Munawar | 25210271 | Tidak bekerja P4,P5 & P6 |
| 2 | Winda Sayka Nadilla | 25210291 | Tidak bekerja P4,P5 & P6 |
| 3 | Fatimah | 25210278 | Tidak bekerja P4, P5 & P6 |
| 4 | Mutia Rahmi | 25210244 | Tidak bekerja P4,P5 & P6 |
| 5 | Rosni | 25210230 | FULL P4,P5 & P6 MANDIRI |
