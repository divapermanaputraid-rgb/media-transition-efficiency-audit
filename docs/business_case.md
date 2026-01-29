# Bussiness Case: Standarisasi & Optimalisasi Metrik Marketing
## 1. Latar Belakang
Perusahaan sedang bertransisi dari media tradisional (TV & Radio) ke kanal Digital dan Event.  
Namun, evaluasi performa lintas kanal masih terfragmentasi dan banyak bergantung pada laporan manual.

Akibatnya, perbandingan performa antar-kanal tidak konsisten dan keputusan alokasi anggaran berisiko tidak optimal.

Proyek ini bertujuan membangun fondasi data yang memungkinkan evaluasi performa marketing secara terintegrasi dan adil di seluruh kanal.

---

## 2. Masalah Utama

### A. Inefisiensi Proses Pelaporan
Proses pengumpulan dan konsolidasi data performa masih banyak melibatkan input manual lintas fungsi operasional.

**Dampak:**
- Tinggi risiko human error
- Waktu tim habis untuk pekerjaan administratif
- Insight sering terlambat atau tidak konsisten

**Peluang:**
Dengan otomatisasi pipeline data, proses pelaporan dapat distandardisasi sehingga tim operasional dapat lebih fokus pada aktivitas bernilai strategis (perencanaan kampanye, klien, dan optimasi performa).

---

### B. Tidak Ada Standar Metrik Lintas Kanal
Setiap kanal memiliki definisi performa yang berbeda:
- TV & Radio: reach dan estimasi exposure
- Digital & Event: klik, engagement, konversi

**Dampak:**
- Sulit membandingkan efektivitas antar-kanal
- Keputusan budget sering berbasis asumsi, bukan data setara

**Kebutuhan:**
Satu metrik terstandarisasi sebagai *Single Source of Truth* untuk evaluasi performa marketing.

---

### C. Risiko Opportunity Cost
Ketidakjelasan ROAS per kanal menyebabkan:
- Budget tetap mengalir ke kanal berperforma rendah
- Kanal dengan potensi tinggi tidak mendapat alokasi optimal

Tanpa audit data yang terintegrasi, potensi efisiensi biaya tidak teridentifikasi.

---

### D. Kegagalan Deteksi Halo Effect
Tanpa integrasi data, perusahaan tidak bisa melihat bagaimana iklan TV/Radio nasional sebenarnya mendorong kenaikan Organic Search di kanal digital.

Hal ini membuat kanal tradisional seringkali terlihat "berperforma rendah" padahal mereka adalah pemicu trafik utama.

## 3. Tujuan Proyek
1. Mengintegrasikan data pengeluaran (`marketing_spend`) dan hasil (`marketing_results`) dalam satu skema data.
2. Menyediakan dashboard performa yang otomatis dan konsisten.
3. Mendukung keputusan realokasi budget berbasis data, bukan intuisi.

---

## 4. Dampak Bisnis yang Diharapkan
- **Efisiensi Operasional:** Pengurangan signifikan pekerjaan manual lintas tim.
- **Kualitas Insight:** Evaluasi performa lintas kanal yang konsisten dan dapat diaudit.
- **Optimasi Anggaran:** Deteksi dini kanal dengan ROAS rendah untuk realokasi budget yang lebih tepat.