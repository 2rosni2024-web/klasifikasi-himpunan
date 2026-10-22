"""Pengujian Sistem Klasifikasi Data dengan Himpunan (PJBL-2, Pertemuan 6).

Menghitung operasi himpunan memakai set Python, lalu membandingkannya
dengan hasil yang tampil di web (index.html) dan menguji Prinsip Inklusi-Eksklusi.
Cara menjalankan:  python uji_himpunan.py
"""

DATASET_1 = [
    ("M01", "Rina", 2024, "A,B"), ("M02", "Budi", 2024, "A"),
    ("M03", "Sari", 2025, "B,C"), ("M04", "Dedi", 2024, "C"),
    ("M05", "Eka", 2025, "A,B,C"), ("M06", "Fajar", 2025, "A"),
    ("M07", "Gita", 2024, "B"), ("M08", "Hadi", 2025, "A,C"),
    ("M09", "Indah", 2024, "B"), ("M10", "Joko", 2025, "C"),
    ("M11", "Kiki", 2024, "A,B"), ("M12", "Lina", 2025, ""),
]
DATASET_2 = [
    ("P01", "Ayu", 2023, "A"), ("P02", "Bima", 2023, "A,C"),
    ("P03", "Citra", 2024, "B"), ("P04", "Dewa", 2024, "B,C"),
    ("P05", "Eko", 2023, "A,B,C"), ("P06", "Fira", 2024, "C"),
    ("P07", "Gani", 2023, "A,B"), ("P08", "Hani", 2024, ""),
    ("P09", "Imam", 2023, "C"), ("P10", "Jihan", 2024, "A"),
]
# Hasil yang diharapkan dari tabel Milestone untuk Dataset 1
HARAPAN_1 = {"|A|": 6, "|B|": 6, "|C|": 5, "|A∪B|": 9, "|A∩B|": 3, "|A−B|": 3, "|A'|": 6}


def bentuk_himpunan(data):
    semesta = {r[0] for r in data}
    kategori = {k: {r[0] for r in data if k in r[3].split(",")} for k in "ABC"}
    return semesta, kategori["A"], kategori["B"], kategori["C"]


def inklusi_eksklusi(A, B, C):
    return (len(A) + len(B) + len(C)
            - len(A & B) - len(A & C) - len(B & C) + len(A & B & C))


def uji(nama, data):
    U, A, B, C = bentuk_himpunan(data)
    print(f"\n=== {nama} ({len(data)} data) ===")
    print("A ∪ B =", sorted(A | B), "->", len(A | B))
    print("A ∩ B =", sorted(A & B), "->", len(A & B))
    print("A − B =", sorted(A - B), "->", len(A - B))
    print("A'    =", sorted(U - A), "->", len(U - A))
    pie2 = len(A) + len(B) - len(A & B)
    pie3 = inklusi_eksklusi(A, B, C)
    print(f"PIE 2 himpunan: |A∪B| = {len(A)} + {len(B)} - {len(A & B)} = {pie2}")
    print(f"PIE 3 himpunan: |A∪B∪C| = {pie3} (langsung: {len(A | B | C)})")
    hasil = [
        ("PIE 2 himpunan sama dengan |A∪B| langsung", pie2 == len(A | B)),
        ("PIE 3 himpunan sama dengan |A∪B∪C| langsung", pie3 == len(A | B | C)),
        ("|A| + |A'| = |U|", len(A) + len(U - A) == len(U)),
    ]
    return U, A, B, C, hasil


def main():
    semua_lulus = True
    for nama, data in (("Dataset 1", DATASET_1), ("Dataset 2", DATASET_2)):
        U, A, B, C, hasil = uji(nama, data)
        if data is DATASET_1:
            nyata = {"|A|": len(A), "|B|": len(B), "|C|": len(C), "|A∪B|": len(A | B),
                     "|A∩B|": len(A & B), "|A−B|": len(A - B), "|A'|": len(U - A)}
            for k, v in HARAPAN_1.items():
                hasil.append((f"Sesuai Milestone {k} = {v}", nyata[k] == v))
        for judul, ok in hasil:
            print(("LULUS  " if ok else "GAGAL  ") + judul)
            semua_lulus &= ok
    print("\nSEMUA UJI LULUS" if semua_lulus else "\nADA UJI YANG GAGAL")


if __name__ == "__main__":
    main()
