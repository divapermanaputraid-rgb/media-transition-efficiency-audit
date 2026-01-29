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

## 3. Processed Layer (Final Mart)
Data hasil integrasi dan transformasi yang siap digunakan untuk analisis strategis.

### Table: `master_marketing_data.csv`
Hasil penggabungan dari seluruh tabel fakta dan dimensi.

| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| ROAS | Float | Rasio efektivitas iklan (Revenue_IDR / Spend_IDR). |
| is_imputed | Boolean | Penanda apakah data konversi merupakan hasil perbaikan/estimasi. |
| Year | Integer | Ekstraksi tahun dari kolom tanggal untuk analisis tren tahunan. |
| Event_Type | String | Label kejadian bisnis yang terasosiasi dengan tanggal tersebut. |