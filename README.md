# Optimasi Budget Iklan: Meningkatkan Keuntungan melalui Data
*Strategi Penghematan Biaya & Peningkatan Efisiensi Pemasaran*

## ⚠️ Disclaimer
Laporan ini berfokus pada **efisiensi biaya iklan (ROAS)** dan **keakuratan data operasional**. Analisis ini dirancang sebagai kerangka kerja strategis untuk mengoptimalkan alokasi budget agar menghasilkan keuntungan maksimal bagi perusahaan.

---

## 1. Ringkasan Hasil (Value Utama)
Proyek ini memberikan solusi nyata untuk memaksimalkan setiap rupiah yang dikeluarkan perusahaan dalam iklan:
* **Potensi Keuntungan:** Rekomendasi pemindahan budget berpotensi meningkatkan pendapatan sebesar **Rp 174,6 Miliar**.
* **Efisiensi Iklan:** Meningkatkan efektivitas iklan digital hingga **3,5x lipat** dibanding tahun sebelumnya melalui audit performa.
* **Keputusan yang Tepat:** Memperbaiki sistem pencatatan laporan yang sebelumnya eror (219 insiden) menjadi **100% akurat** untuk mencegah salah ambil keputusan bisnis.
* **Performa Nyata (2025):** Mencapai tingkat pengembalian modal iklan (**ROAS**) sebesar **23.89x**.

---

## 2. Masalah & Solusi Bisnis
* **Masalah:** Data iklan berantakan dan sulit dibaca, menyebabkan manajemen sulit mengetahui kanal mana yang benar-benar menghasilkan uang dan mana yang membuang biaya.
* **Solusi:** Saya membangun **Dashboard Otomatis (Looker Studio)** yang memantau performa pengeluaran perusahaan secara *real-time*. Ini memungkinkan pimpinan mengambil keputusan berdasarkan fakta, bukan asumsi.

![Executive Dashboard](./reports/figures/looker_dashboard_final.png)

---

## 3. Cara Kerja Sistem (Infrastruktur Sederhana)
Meskipun menggunakan teknologi canggih, tujuannya adalah mempermudah operasional harian:
* **Sistem Otomatisasi (scripts/ & sql/):** Menggantikan proses manual yang lambat dan rawan eror (Excel), sehingga laporan selalu siap secara otomatis.
* **Panduan Strategis (docs/):** Berisi penjelasan cara mempertahankan dan meningkatkan keuntungan secara berkelanjutan.
* **Visualisasi (reports/):** Grafik sederhana yang menunjukkan di mana uang perusahaan bekerja paling keras dan di mana pemborosan terjadi.

---

## 4. Struktur Proyek
Organisasi file disusun secara profesional untuk memastikan keberlanjutan sistem:

```text
├── data/            # Data Mentah & Data Olahan
├── docs/            # Panduan Strategi & Kamus Istilah Bisnis
├── reports/figures/ # Visualisasi Dashboard & Grafik Performa
├── scripts/         # Sistem Otomatisasi Laporan (Python)
├── sql/             # Logika Penarikan Data (Database)
└── README.md        # Ringkasan Eksekutif
