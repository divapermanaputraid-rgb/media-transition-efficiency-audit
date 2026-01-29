import pandas as pd
import os

def run_advanced_simulation():
    print("--- SIMULASI LANJUTAN: HYBRID ALLOCATION (DIGITAL + EVENT) ---")

    # 1. LOAD DATA
    file_path = './data/processed/performance_summary.csv'
    if not os.path.exists(file_path):
        print("Error: File summary tidak ditemukan.")
        return
        
    df = pd.read_csv(file_path)
    df_2025 = df[df['Year'] == 2025].copy()

    if df_2025.empty:
        print("Error: Data tahun 2025 tidak ditemukan.")
        return

    # 2. DATA RETRIEVAL (Mengambil data per channel)
    try:
        tv_perf = df_2025[df_2025['Channel'] == 'TV'].iloc[0]
        radio_perf = df_2025[df_2025['Channel'] == 'Radio'].iloc[0]
        digital_perf = df_2025[df_2025['Channel'] == 'Digital'].iloc[0]
        # Pastikan channel 'Event' ada di data Anda. 
        # Jika namanya beda (misal 'Activation' atau 'Offline'), sesuaikan string di bawah.
        event_perf = df_2025[df_2025['Channel'] == 'Event'].iloc[0] 
    except IndexError:
        print("Error: Salah satu channel (TV, Radio, Digital, atau Event) tidak ditemukan.")
        print("Channel tersedia:", df_2025['Channel'].unique())
        return

    # 3. SETTING SKENARIO
    # Total Budget Tradisional (Sumber Dana)
    trad_spend = tv_perf['Spend_IDR'] + radio_perf['Spend_IDR']
    
    # Rata-rata ROAS Tradisional (Efisiensi yang akan hilang)
    # Kita hitung weighted average atau simple average. Di sini simple average dari 2 channel.
    avg_trad_roas = (tv_perf['ROAS'] + radio_perf['ROAS']) / 2

    # REALOKASI 20% DARI TRADISIONAL
    total_shifted_budget = trad_spend * 0.20
    
    # STRATEGI SPLIT: 50:50 dari dana yang dipindah
    # Artinya: 10% budget TV/Radio lari ke Digital, 10% lari ke Event
    budget_to_digital = total_shifted_budget * 0.50
    budget_to_event = total_shifted_budget * 0.50

    # 4. KALKULASI DAMPAK (THE IMPACT CALCULATION)
    
    # Revenue Hilang (Opportunity Cost dari TV/Radio)
    revenue_loss = total_shifted_budget * avg_trad_roas
    
    # Revenue Baru (Gain)
    gain_from_digital = budget_to_digital * digital_perf['ROAS']
    gain_from_event   = budget_to_event * event_perf['ROAS'] # Ini adalah "The Multiplier"
    
    total_gain = gain_from_digital + gain_from_event
    net_impact = total_gain - revenue_loss

    # 5. PERBANDINGAN FINAL
    total_spend_company = df_2025['Spend_IDR'].sum() # Spend tetap sama
    total_revenue_old   = df_2025['Revenue_IDR'].sum()
    total_revenue_new   = total_revenue_old + net_impact

    roas_old = total_revenue_old / total_spend_company
    roas_new = total_revenue_new / total_spend_company
    
    improvement_pct = ((roas_new - roas_old) / roas_old) * 100

    # 6. REPORTING
    print("\n" + "="*45)
    print("HASIL SIMULASI: STRATEGI HYBRID (DIGITAL + EVENT)")
    print("="*45)
    print(f"Sumber Dana (TV+Radio) 20%  : Rp {total_shifted_budget:,.0f}")
    print(f" - Alokasi ke Digital (10%) : Rp {budget_to_digital:,.0f}")
    print(f" - Alokasi ke Event (10%)   : Rp {budget_to_event:,.0f}")
    print("-" * 45)
    print(f"Revenue Hilang (Trad)       : -Rp {revenue_loss:,.0f}")
    print(f"Revenue Masuk (Digital)     : +Rp {gain_from_digital:,.0f}")
    print(f"Revenue Masuk (Event)       : +Rp {gain_from_event:,.0f} (BOOM!)")
    print(f"NET PROFIT TAMBAHAN         : +Rp {net_impact:,.0f}")
    print("-" * 45)
    print(f"ROAS Awal                   : {roas_old:.2f}x")
    print(f"ROAS Baru                   : {roas_new:.2f}x")
    print(f">> KENAIKAN ROAS TOTAL      : {improvement_pct:.2f}%")
    print("="*45)

if __name__ == "__main__":
    run_advanced_simulation()