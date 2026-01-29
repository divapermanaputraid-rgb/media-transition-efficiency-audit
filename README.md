# Media Transition & Efficiency Audit  
*Cross-Channel Performance & Data Integrity Case Study*

## ⚠️ Disclaimer
Analisis dalam proyek ini berfokus pada **efisiensi performa kanal (ROAS)** dan **integritas operasional data**. Karena keterbatasan akses pada data biaya internal (seperti *media fee, operational cost,* atau *margin produk*), laporan ini **tidak mencakup perhitungan profitabilitas bersih (net revenue/profit)**. 

Proyek ini diposisikan sebagai **kerangka analitis (analytical framework)** untuk mendukung diskusi strategis dan optimasi alokasi budget lintas tim.

## 1. Project Overview
Proyek ini merupakan audit performa kampanye marketing selama masa transisi dari media tradisional (TV/Radio) ke kanal Digital dan Event di agensi DMN.

Fokus analisis meliputi:
- Integrasi data lintas kanal
- Audit kebocoran data akibat pelaporan manual
- Simulasi dampak realokasi budget berbasis performa

Tujuan utama proyek ini adalah membangun dasar pengambilan keputusan yang lebih akurat dan terukur dalam proses transisi media.

---

## 2. Business Question
**Bagaimana integrasi data dan audit performa lintas kanal dapat meningkatkan ROAS hingga ±20% sekaligus menghilangkan missing data yang disebabkan oleh pelaporan manual?**

---

## 3. Key Audit Findings (Evidence-Based)

### A. Integritas Data & Operasional
- **Data Leakage:**  
Ditemukan 219 insiden missing data pada kolom konversi sepanjang tahun 2024, yang terjadi pada proses pelaporan yang masih mengandalkan input manual lintas tim operasional.
  
- **Impact of Process Standardization:**  
  Audit pasca-pelatihan internal (cutoff 20 Maret 2025) menunjukkan penurunan signifikan jumlah missing data.  
  Temuan ini mengindikasikan bahwa **standarisasi proses dan otomasi pelaporan** berperan langsung dalam menurunkan risiko human error.

---

### B. Analisis Performa Lintas Kanal (ROAS)

| Era | Media Tradisional (TV/Radio) | Media Digital |
|---|---|---|
| 2024 (Baseline) | 1.1x ROAS | 1.2x ROAS |
| 2025 (Transition) | 1.1x ROAS | 3.5x ROAS |

**Insight:**  
Walaupun porsi budget media tradisional masih dominan, efisiensi kanal digital meningkat secara signifikan (~190%) saat alokasi mulai bergeser.  
Hal ini menunjukkan bahwa pertumbuhan performa digital bersifat struktural, bukan kebetulan.

---

### C. Seasonality vs Strategy
- **Normal Day ROAS:** 23.0x  
- **Lebaran Season ROAS:** 15.2x  

**Kesimpulan Analitis:**  
Performa digital tidak hanya terdorong oleh momentum musiman. Bahkan di luar periode puncak, kanal digital menunjukkan efisiensi yang lebih tinggi, mengindikasikan potensi pertumbuhan yang berkelanjutan.

---

## 4. Problem Statement (Revised)
Berdasarkan hasil audit, terdapat dua tantangan utama:

1. **Inefisiensi Alokasi Budget**  
   Budget masih tertahan pada media tradisional dengan ROAS stagnan (±1.1x), sementara kanal digital dengan efisiensi lebih tinggi belum mendapatkan porsi optimal.

2. **Integritas Data**  
   Kebocoran data pada 2024 menyebabkan evaluasi performa dan keputusan strategis dilakukan dengan basis data yang tidak lengkap.

---

## 5. Strategic Considerations (Data-Informed)
Temuan dalam proyek ini membuka beberapa pertimbangan strategis:

- **Realokasi Bertahap:**  
  Simulasi menunjukkan bahwa pengalihan ±15–20% budget dari TV/Radio ke Digital berpotensi mendorong kenaikan ROAS total hingga ±20%.

- **Otomasi Pelaporan:**  
  Transisi dari pelaporan manual ke automated data pipeline berpotensi menghilangkan missing data secara struktural, bukan sekadar korektif.

- **Cross-Channel Activation:**  
  Kanal Event menunjukkan ROAS tertinggi dan berpotensi dimanfaatkan sebagai trigger untuk retargeting melalui kanal digital.

> Catatan: Poin di atas diposisikan sebagai **input analitis**, bukan keputusan bisnis final.

---
## 6. Project Structure
- `scripts/01_initial_audit.py`: Identifikasi awal data bolong & pembersihan.
- `scripts/02_process_master_table.py`: Integrasi data Spend, Results, dan Campaigns.
- `scripts/03_performance_analysis.py`: Kalkulasi ROAS tahunan dan per kanal.
- `scripts/04_event_analysis.py`: Koreksi performa dengan Business Events & audit pasca-training.

