import pandas as pd
import os

def run_budget_simulation():
    print("--- mulai simulasi realokasi budget (scenario: shift 20% to digital)---")
    # 1. LOAD DATA
    # butuh data performa per channel TAHUN 2025
    file_path = './data/processed/performance_summary.csv'
    if not os.path.exists(file_path):
        print("error: file performance summary tidak ditemukan, jalan dulu script 03_performance_analysis.py")
        return
    
    df = pd.read_csv(file_path)
    
    # 2. FILTER BASELINE TAHUN 2025
    df_2025 = df[df['Year'] == 2025].copy()

    # Validasi ada data 2025
    if df_2025.empty:
        print("error: tidak ada data untuk tahun 2025.")
        return
    
    # 3. IDENTIFIKASI PERFORMANCE GAP
    # ambil satu baris data untuk masing-masing channel
    try:
        # Menggunakan .iloc[0] untuk mengambil Row pertama (Series) dari hasil filter
        tv_perf = df_2025[df_2025['Channel'] == 'TV'].iloc[0]
        radio_perf = df_2025[df_2025['Channel'] == 'Radio'].iloc[0]
        digital_perf = df_2025[df_2025['Channel'] == 'Digital'].iloc[0]
    except IndexError:
        print("Error: Salah satu channel (TV/Radio/Digital) tidak ditemukan di data 2025.")
        print("Channel yang tersedia:", df_2025['Channel'].unique())
        return
    
    # 4. SIMULASI REALOKASI BUDGET
    # Skenario: Ambil 20% budget dari kanal tradisional, pindahkan ke Digital
    reallocation_rate = 0.20  # 20%

    # budget yang dipindah = (TV Spend + Radio Spend) * 20%
    budget_to_shift = (tv_perf['Spend_IDR'] + radio_perf['Spend_IDR']) * reallocation_rate

    # hitung revenue yang hilang dari TV & Radio
    # gunakan rata-rata ROAS mereka. (Uang keluar dari sini, berarti revenue hilang)
    avg_roas_traditional = (tv_perf['ROAS'] + radio_perf['ROAS']) / 2
    revenue_lost = budget_to_shift * avg_roas_traditional

    # hitung Revenue yang didapat dari digital
    # (uang yang masuk ke sini di kalikan dengan ROAS digital)
    revenue_gain = budget_to_shift * digital_perf['ROAS']

    # 5. PERBANDINGAN SEBELUM DAN SESUDAH (The Impact)
    # total spend tetap sama (tidak ada penambahan budget)
    total_spend = df_2025['Spend_IDR'].sum()

    # revenue
    total_revenue_baseline = df_2025['Revenue_IDR'].sum()
    total_revenue_simulated = total_revenue_baseline - revenue_lost + revenue_gain

    # ROAS calculation
    roas_baseline = total_revenue_baseline / total_spend
    roas_simulated = total_revenue_simulated / total_spend

    # Growth percentage
    improvment_pct = ((roas_simulated - roas_baseline) / roas_baseline) * 100
    net_revenue_impact = revenue_gain - revenue_lost

    # 6. PRINT HASIL SIMULASI
    print("\n" + "-"*40)
    print("HASIL SIMULASI STRAGEGIS (2025 BASELINE)")
    print("="*40)
    print(f"Total Budget Marketing       : Rp {total_spend:,.0f}")
    print(f"Total Direalokasi            : Rp {budget_to_shift:,.0f}")
    print("-"*40)
    print(f"Revenue Hilang (tradisional) : Rp {revenue_lost:,.0f}")
    print(f"Revenue Mendapat (digital)   : Rp {revenue_gain:,.0f}")
    print(f"NET REVENUE IMPACT           : Rp {net_revenue_impact:,.0f}")
    print("-"*40)
    print(f"ROAS Awal                    : {roas_baseline:.2f}")
    print(f"ROAS Simulasi                : {roas_simulated:.2f}")
    print(f">> POTENSI KENAIKAN ROAS     : {improvment_pct:.2f} %")
    print("-"*40)

if __name__ == "__main__":
    run_budget_simulation()