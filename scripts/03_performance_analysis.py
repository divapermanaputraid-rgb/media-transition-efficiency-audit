import pandas as pd
import os

def performance_analysis():
    # LOAD MASTER TABLE
    input_path = './data/processed/master_marketing_data.csv'
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} does not exist.jalan dulu script 02_process_master_table.py")
        return
        
    df_master = pd.read_csv(input_path)

    # 1. persiapkan data
    df_master['Date'] = pd.to_datetime(df_master['Date'])
    df_master['Year'] = df_master['Date'].dt.year

    # 2. Agregasi: kelompokan data pertahun dan channel
    performance_summary = df_master.groupby(['Year', 'Channel']).agg({
        'Spend_IDR': 'sum',
        'Revenue_IDR': 'sum',
    }).reset_index()


    # 3. kalkulasi ROAS
    # ROAS = Revenue / Spend
    performance_summary['ROAS'] = performance_summary.apply(
        lambda row: row['Revenue_IDR'] / row['Spend_IDR'] if row['Spend_IDR'] > 0 else 0, 
        axis=1
    )
    # 4. Simpan hasil analisis

    output_dir = './data/processed'
    os.makedirs(output_dir, exist_ok=True)
    performance_summary.to_csv(f'{output_dir}/performance_summary.csv', index=False)

    print("--- Step 2.1 & 2.2 Selesai ---")
    print(performance_summary.sort_values(by=['Year', 'ROAS'], ascending=[True, False]))

if __name__ == "__main__":
        performance_analysis()  