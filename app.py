import streamlit as st
import pandas as pd

# Konfigurasi Tampilan
st.set_page_config(page_title="Penyu Monitor - Urutan Benar", layout="wide", page_icon="🐢")

# 1. Data ASLI dari Excel Rekap 2025 kamu
data_rekap = [
    {"Bulan": "Januari", "Telur": 76, "Perjumpaan": 2},
    {"Bulan": "Februari", "Telur": 68, "Perjumpaan": 2},
    {"Bulan": "Maret", "Telur": 66, "Perjumpaan": 1},
    {"Bulan": "April", "Telur": 76, "Perjumpaan": 1},
    {"Bulan": "Mei", "Telur": 203, "Perjumpaan": 3},
    {"Bulan": "Juni", "Telur": 198, "Perjumpaan": 3},
    {"Bulan": "Juli", "Telur": 678, "Perjumpaan": 7},
    {"Bulan": "Agustus", "Telur": 239, "Perjumpaan": 3},
    {"Bulan": "September", "Telur": 216, "Perjumpaan": 3},
    {"Bulan": "Oktober", "Telur": 139, "Perjumpaan": 2},
    {"Bulan": "November", "Telur": 157, "Perjumpaan": 2},
    {"Bulan": "Desember", "Telur": 139, "Perjumpaan": 2},
]

df = pd.DataFrame(data_rekap)

# --- TRIK AGAR URUT JANUARI - DESEMBER ---
list_bulan = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni", 
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]
# Mengubah kolom Bulan menjadi tipe 'Categorical' dengan urutan yang sudah ditentukan
df['Bulan'] = pd.Categorical(df['Bulan'], categories=list_bulan, ordered=True)
# Urutkan dataframe berdasarkan kategori tersebut
df = df.sort_values('Bulan')
# ------------------------------------------

# Judul Dashboard
st.title("🐢 Dashboard Monitoring Penyu - Urutan Kalender")
st.markdown("---")

# Scorecards
total_telur = df['Telur'].sum()
total_perjumpaan = df['Perjumpaan'].sum()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Telur Diamankan", value=f"{total_telur:,} Butir")
with col2:
    st.metric(label="Total Perjumpaan", value=f"{total_perjumpaan} Kali")
with col3:
    st.metric(label="Rata-rata Telur", value=f"{round(total_telur/total_perjumpaan)} Butir")

st.markdown("---")

# 2. Grafik Tren Bulanan (Sekarang Pasti Urut!)
st.subheader("📊 Tren Pengamanan Telur Per Bulan")
# Kita set index ke 'Bulan' agar Streamlit mengikuti urutan kategori yang kita buat
st.bar_chart(data=df.set_index('Bulan')['Telur'], color="#2E8B57")

st.sidebar.success("✅ Urutan grafik sudah sesuai kalender!")
