# Transition & Efficiency Audit  
*Cross-Channel Performance & Data Integrity Case Study*
## Optimasi Budget Iklan: Meningkatkan Keuntungan melalui Data
*Strategi Penghematan Biaya & Peningkatan Efisiensi Pemasaran*

## ⚠️ Disclaimer
Laporan ini berfokus pada **transparansi biaya iklan (ROAS)** dan **validitas data operasional**. Analisis ini dirancang sebagai kerangka kerja strategis untuk mengalokasikan budget secara objektif guna menghasilkan keuntungan maksimal bagi perusahaan.

---

## 1. Ringkasan Hasil (Value Utama)
Proyek ini memberikan solusi nyata untuk memaksimalkan setiap rupiah yang dikeluarkan perusahaan:
* **Potensi Keuntungan:** Rekomendasi realokasi budget berpotensi meningkatkan pendapatan sebesar **Rp 174,6 Miliar**.
* **Efisiensi Iklan:** Optimasi pada kanal digital berhasil meningkatkan efektivitas hingga **3,5x lipat** melalui eliminasi kanal yang tidak produktif.
* **Keandalan Data:** Sinkronisasi laporan yang sebelumnya memiliki 219 insiden selisih data menjadi **rekonsiliasi 1:1 (nol selisih)** antara sistem internal dan laporan akhir.
* **Performa Strategis (2025):** Mencapai tingkat pengembalian modal iklan (**ROAS**) sebesar **23.89x**.

---

## 2. Masalah & Solusi Bisnis
* **Masalah:** Fragmentasi data iklan menyebabkan manajemen sulit membedakan kanal yang menguntungkan dan kanal yang membuang biaya (pemborosan budget).
* **Solusi:** Implementasi **Dashboard Otomatis (Looker Studio)** yang mengintegrasikan seluruh data pengeluaran secara *real-time*. Memberikan visibilitas penuh bagi pimpinan untuk mengambil keputusan berbasis performa nyata.

![Executive Dashboard](./reports/figures/looker_dashboard_final.png.png)

---

## 3. Infrastruktur & Keberlanjutan Sistem
Sistem ini dibangun dengan standar profesional agar tetap mudah dioperasikan dalam jangka panjang:
* **Otomatisasi Laporan (scripts/ & sql/):** Menghilangkan ketergantungan pada input manual yang rawan kesalahan, memastikan data selalu siap saji.
* **Pusat Strategi (docs/):** Dokumentasi lengkap mengenai logika perhitungan (Business Rules) agar strategi tetap konsisten.
* **Analisis Visual (reports/):** Visualisasi yang memudahkan identifikasi pemborosan budget secara instan.

---

## 4. Struktur Proyek
Organisasi file disusun untuk memudahkan audit dan pemeliharaan sistem:

```text
├── data/            # Data Mentah & Hasil Pengolahan
├── docs/            # Panduan Strategi & Kamus Istilah Bisnis
├── reports/figures/ # Visualisasi Dashboard & Grafik Performa
├── scripts/         # Mesin Otomatisasi Data
├── sql/             # Logika Database (Query)
└── README.md        # Ringkasan Eksekutif