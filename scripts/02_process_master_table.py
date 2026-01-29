import pandas as pd
import os


# Load Data
df_results = pd.read_csv('./data/raw/stg_marketing_results.csv')
df_spend = pd.read_csv('./data/raw/stg_marketing_spend.csv')

# 1. Load Master Campaingn
# Buat apa? Mengambil "Kamus Data". Data transaksi (spend) biasanya cuma punya
df_campaigns = pd.read_csv('./data/reference/ref_campaigns.csv')


# 2. gabungkan spend dengan results
# Buat apa? Menyatukan dua tabel fakta utama: Uang Keluar (Spend) dan Uang Masuk (Result).
df_master = pd.merge(df_spend, df_results, on=['Date', 'CampaignID'], how='left')

# 3. gabungkan dengan ref_campaigns untuk mendapat info 'Channel' & 'sub_channel'
# Buat apa? "VLOOKUP" masal. Kita tempelkan label Channel (misal: 'Facebook Ads') ke tabel utama berdasarkan CampaignID yang cocok.
df_master = pd.merge(df_master, df_campaigns, on='CampaignID', how='left')

# 4. DATA CLEANING: handle baris yang kosong
# Buat apa? Membersihkan sampah hasil Join.
# Jika hasil Join menghasilkan NaN pada Revenue, isi dengan 0. biar bisa dihitung
df_master['Revenue_IDR'] = df_master['Revenue_IDR'].fillna(0)
df_master['Conversions'] = df_master['Conversions'].fillna(0)

# 5. Simpan Master Table
os.makedirs('./data/processed/', exist_ok=True)
df_master.to_csv('./data/processed/master_marketing_data.csv', index=False)

print("---Step 1.2: Master Table Created and Saved---")
print(f"Total Rows in Master Table: {len(df_master)}")
print(df_master[['Date', 'Channel', 'Spend_IDR', 'Revenue_IDR']].head())