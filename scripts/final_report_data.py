import pandas as pd

def create_final_looker_data():
    # 1. Load data hasil integrasi (Script 02)
    df_master = pd.read_csv('./data/processed/master_marketing_data.csv')
    
    # 2. Load data event (Reference)
    df_events = pd.read_csv('./data/reference/ref_business_events.csv')
    
    # 3. Join berdasarkan Tanggal
    # Kita pakai 'left' agar data yang tidak ada event-nya tetap muncul
    df_final = pd.merge(df_master, df_events, on='Date', how='left')
    
    # 4. Fillna untuk hari biasa
    df_final['Event_Type'] = df_final['Event_Type'].fillna('Normal Day')
    
    # 5. Export untuk Looker Studio
    df_final.to_csv('./data/processed/final_looker_data.csv', index=False)
    print("File 'final_looker_data.csv' siap! Gunakan file ini untuk Looker Studio.")

if __name__ == "__main__":
    create_final_looker_data()