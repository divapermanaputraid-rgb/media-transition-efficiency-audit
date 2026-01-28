import pandas as pd
df_results = pd.read_csv('./data/raw/stg_marketing_results.csv')
df_spend = pd.read_csv('./data/raw/stg_marketing_spend.csv')

print("---Info Tabel Results---")
df_results.info()

# Menghitung Jumlah data kosong di tiap kolom
null_report_results = df_results.isnull().sum()
print(null_report_results)

# menampilkan 10 baris pertama yang datanya kosong
missing_data=df_results[df_results['Conversions'].isnull()]
print(missing_data.head(10))

# gabungkan data results dan spend yang bolong
missing_impact = pd.merge(missing_data, df_spend, on=['Date', 'CampaignID'])
total_untracked_spend = missing_impact['Spend_IDR'].sum()

print(f"Total Budget Iklan Yang tidak terukur hasilnya: Rp {total_untracked_spend:,.0f}")

