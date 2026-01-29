import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visuals():
    print("---visualisasi Data---")

    # 1. SETUP FOLDER & STYLE
    output_dir = './reports/figures'
    os.makedirs(output_dir, exist_ok=True)

    # atur tema visual
    sns.set_theme(style="whitegrid")

    # 2. LOAD DATA
    path_perf = './data/processed/performance_summary.csv'
    path_events = './data/processed/event_impact_analysis.csv'

    if not os.path.exists(path_perf) or not os.path.exists(path_events):
        print("Error: File data tidak ditemukan. Pastikan script sebelumnya sudah dijalankan.")
        return
    
    df_perf = pd.read_csv(path_perf)
    df_events = pd.read_csv(path_events)

    # --- CHART 1: ROAS TRANSITION (media efficiency) ---
    plt.figure(figsize=(10,6))

    # filter perbandingan tv/radio vs digital
    target_channels = ['TV', 'Radio', 'Digital']
    df_filtered = df_perf[df_perf['Channel'].isin(target_channels)]

    # buat barplot
    ax1 = sns.barplot(
        data=df_filtered,
        x='Channel',
        y='ROAS',
        hue='Year',
        palette='viridis'
    )
    plt.title('Transformasi Efisiensi: Digital vs Traditional (2023-2025)', fontsize=14, pad=20, weight='bold')
    plt.xlabel('Marketing Channel', fontsize=12)
    plt.ylabel('Return on Ad Spend (x)', fontsize=12)
    
    #tambah label angka di atas bar
    for container in ax1.containers:
        ax1.bar_label(container, fmt='%.1f', padding=3)
    
    plt.savefig(f'{output_dir}/01_roas_transition.png', dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Chart 1 saved to {output_dir}/01_roas_transition.png")
    plt.close()

    # --- CHART 2: THE LEVERAGE (event impact) ---
    plt.figure(figsize=(12,7))

    # urutkan data ROAS tinggi ke rendah
    df_events_sorted = df_events.sort_values(by='ROAS', ascending=False).head(8)

    # horizontal barplot
    ax2 = sns.barplot(
        data=df_events_sorted,
        x='ROAS',
        y='Event_Type',
        palette='magma'
    )

    plt.title('The Growth Engine: Dampak Event terhadap ROAS', fontsize=14, pad=20, weight='bold')
    plt.xlabel('ROAS Multiplier (x)', fontsize=12)
    plt.ylabel('') # Hilangkan label Y biar bersih

    # tambah label angka di samping bar
    for container in ax2.containers:
        ax2.bar_label(container, fmt='%.1f', padding=5)

    plt.savefig(f'{output_dir}/02_event_impact.png', dpi=300, bbox_inches='tight')
    print(f"[SUCCESS] Chart 2 saved to {output_dir}/02_event_impact.png")
    plt.close()

    print("\n--- Semua visualisasi selesai dibuat ---")

if __name__ == "__main__":
    create_visuals()