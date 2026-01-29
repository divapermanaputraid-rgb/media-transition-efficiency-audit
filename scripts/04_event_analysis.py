import pandas as pd
import os

""" Kita sudah tahu Digital menang telak. 
    Sekarang pertanyaannya: Apakah Digital menang karena memang efisien, atau karena terbantu musim Lebaran?"""

def events_analysis():
    print("--- mulai analysis event & audit data ---")

    # 1. LOAD DATA
    input_path = './data/processed/master_marketing_data.csv'
    events_path = './data/reference/ref_business_events.csv'

    if not os.path.exists(input_path):
        print("error: file master data tidak ditemukan,")
        return
    
    # Cek keberadaan file events
    if not os.path.exists(events_path):
        print("error: file business events tidak ditemukan,")
        return
    
    df_master = pd.read_csv(input_path)
    df_events = pd.read_csv(events_path)

    # Konversi ke datetime
    df_master['Date'] = pd.to_datetime(df_master['Date'])
    df_events['Date'] = pd.to_datetime(df_events['Date'])

    # 2. GABUNGKAN DENGAN BUSSINES EVENTS
    df_final = pd.merge(df_master, df_events, on='Date', how='left')

    # isi NaN di kolom Event_Type dengan 'Normal Day'
    df_final['Event_Type'] = df_final['Event_Type'].fillna('Normal Day')

    # ---------------------------------------------------------
    # BAGIAN A: AUDIT PERBAIKAN (Sesuai Instruksi Anda)
    # ---------------------------------------------------------
    # Tujuannya: Membuktikan apakah training tim pada 20 Maret mengurangi error input.
    # Catatan: Karena di script 02 kita sudah fillna(0), kita cek data Raw atau
    # asumsikan kita mencari 'Zero Conversion' sebagai indikator data tidak terisi/missing.

    training_date = pd.to_datetime('2024-03-20')

    # bagi dataset menjadi 2 era
    df_pre = df_final[df_final['Date'] < training_date]
    df_post = df_final[df_final['Date'] >= training_date]

    # hitung presentase hari dengan 0 Conversions
    zero_conv_pre = len(df_pre[df_pre['Conversions'] == 0])
    zero_conv_post = len(df_post[df_post['Conversions'] == 0])

    print(f"--- Evaluasi Training AE (Cutoff: {training_date.date()}) ---")
    print(f"era pre-training: {zero_conv_pre} insiden '0 Conversions' dari {len(df_pre)} baris data")
    print(f"era post-training: {zero_conv_post} insiden '0 Conversions' dari {len(df_post)} baris data")

    if len(df_post) > 0 and zero_conv_post == 0:
        print(">> KESIMPULAN: Training BERHASIL. Tidak ada lagi data konversi kosong/nol setelah tanggal 20 Maret.")
    else:
        print(">> KESIMPULAN: Masih ada data nol, perlu investigasi lanjut apakah ini lupa input atau memang tidak ada sales.")

    # ---------------------------------------------------------
    # BAGIAN B: ANALISIS DAMPAK EVENT (Menjawab Pertanyaan Lebaran)
    # ---------------------------------------------------------
    # Mengelompokkan performa berdasarkan Jenis Event

    event_impact = df_final.groupby('Event_Type').agg({
        'Spend_IDR': 'sum',
        'Revenue_IDR': 'sum',
        'Date': 'count'  # hitung jumlah hari
    }).reset_index()

    # Hitung ROAS per Event
    event_impact['ROAS'] = event_impact['Revenue_IDR'] / event_impact['Spend_IDR']

    # rename kolom
    event_impact = event_impact.rename(columns={'Date': 'Days_Count'})

    print("\n--- Impact Analysis: Lebaran Vs Normal Day ---")
    print(event_impact.sort_values(by='ROAS', ascending=False))

    # export hasil analysis event untuk visualisasi lebih lanjut
    event_impact.to_csv('./data/processed/event_impact_analysis.csv', index=False)

if __name__ == "__main__":
    events_analysis()
