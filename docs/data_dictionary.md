# Data Dictionary: Media Transition Efficiency Audit

## 1. Raw Layer (Staging Data)
Data mentah hasil ekstraksi dari sistem iklan dan pelaporan manual tim Account Executive.

### Table: `stg_marketing_spend.csv`
Catatan harian pengeluaran biaya iklan.

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| Date | Date | Tanggal pengeluaran biaya iklan. |
| CampaignID | String | ID unik kampanye (Foreign Key ke ref_campaigns). |
| Spend_IDR | Float | Total biaya iklan yang dikeluarkan (dalam Rupiah). |
| Impressions | Integer | Jumlah total tampilan iklan yang tercapai. |

### Table: `stg_marketing_results.csv`
Catatan performa harian yang diinput secara manual.

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| Date | Date | Tanggal pencatatan hasil performa. |
| CampaignID | String | ID unik kampanye (Foreign Key ke ref_campaigns). |
| Conversions | Float | Jumlah aksi/transaksi (Terdapat 219 baris Null pada 2024). |
| Revenue_IDR | Float | Total pendapatan yang dihasilkan (dalam Rupiah). |

---

## 2. Reference Layer (Master Data)
Tabel referensi yang digunakan untuk kategorisasi dan validasi audit.

### Table: `ref_campaigns.csv`
Master data pengelompokan kampanye.

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| CampaignID | String | ID unik kampanye (Primary Key). |
| Channel | String | Kategori media utama (TV, Radio, Digital, Event). |
| Sub_Channel | String | Platform spesifik (misal: Meta, TikTok, RCTI, Prambors). |

### Table: `ref_business_events.csv`
Log kejadian bisnis internal dan eksternal.

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| Date | Date | Tanggal kejadian berlangsung (Primary Key). |
| Event_Type | String | Jenis event (misal: Lebaran_Season, Training_Completed). |

---

## 3. Processed Layer (Final Mart & Aggregates)
Data hasil integrasi dan ringkasan performa untuk kebutuhan pelaporan strategis.

### Table: `master_marketing_data.csv`
Hasil penggabungan dari seluruh tabel fakta dan dimensi secara harian.

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| **ROAS** | Float | Rasio efektivitas iklan (Revenue_IDR / Spend_IDR). |
| **is_imputed** | Boolean | Penanda apakah data konversi merupakan hasil perbaikan/estimasi. |
| **Year** | Integer | Ekstraksi tahun dari kolom tanggal. |
| **Event_Type** | String | Label kejadian bisnis yang terasosiasi dengan tanggal tersebut. |

---

### Table: `performance_summary.csv`
Ringkasan performa tahunan per kanal media untuk analisis tren.

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| **Year** | Integer | Tahun periode analisis (2024 atau 2025). |
| **Channel** | String | Kategori kanal media. |
| **Spend_IDR** | Float | Akumulasi biaya iklan dalam satu tahun. |
| **Revenue_IDR** | Float | Akumulasi pendapatan dalam satu tahun. |
| **ROAS** | Float | Rata-rata tertimbang ROAS per kanal per tahun. |

---

### Table: `event_impact_analysis.csv`
Analisis efektivitas berdasarkan kejadian bisnis (Seasonality vs Operation).

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| **Event_Type** | String | Jenis kejadian (misal: Lebaran_Season, Training_Completed, Normal Day). |
| **Spend_IDR** | Float | Total biaya iklan selama durasi kejadian berlangsung. |
| **Revenue_IDR** | Float | Total pendapatan selama durasi kejadian berlangsung. |
| **Days_Count** | Integer | Jumlah hari durasi kejadian untuk normalisasi data. |
| **ROAS** | Float | Efisiensi kanal selama periode kejadian tertentu. |