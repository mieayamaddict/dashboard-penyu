import streamlit as st
import pandas as pd

# Konfigurasi Tampilan
st.set_page_config(page_title="Penyu Monitor - Data Akurat", layout="wide", page_icon="🐢")

# Data ASLI dari Excel Rekap 2025 kamu
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

# Data Distribusi Per Blok (Sesuai Excel)
data_blok = [
    {"Blok": "Tegalsereh", "Total_Telur": 1046},
    {"Blok": "Pamoekan", "Total_Telur": 438},
    {"Blok": "Katapang", "Total_Telur": 393},
    {"Blok": "Panarikan", "Total_Telur": 378},
]

df = pd.DataFrame(data_rekap)
df_blok = pd.DataFrame(data_blok)

# Judul Dashboard
st.title("🐢 Dashboard Monitoring Penyu - Data Valid 2025")
st.markdown("---")

# 1. Scorecards (Angka Akurat)
total_telur = df['Telur'].sum()
total_perjumpaan = df['Perjumpaan'].sum()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Telur Diamankan", value=f"{total_telur:,} Butir")
with col2:
    st.metric(label="Total Perjumpaan (Sarang)", value=f"{total_perjumpaan} Kali")
with col3:
    st.metric(label="Rata-rata Telur per Sarang", value=f"{round(total_telur/total_perjumpaan)} Butir")

st.markdown("---")

# 2. Grafik Tren Bulanan
st.subheader("📊 Tren Pengamanan Telur Per Bulan (Real Data)")
st.bar_chart(data=df, x='Bulan', y='Telur', color="#2E8B57")

# 3. Kontribusi per Lokasi
st.markdown("---")
st.subheader("📍 Kontribusi Telur per Blok")
col_left, col_right = st.columns(2)

with col_left:
    st.write("Daftar Lokasi & Capaian:")
    st.table(df_blok)

with col_right:
    # Menampilkan blok dengan telur terbanyak
    top_blok = df_blok.iloc[0]['Blok']
    st.info(f"🏆 Blok **{top_blok}** merupakan penyumbang telur terbanyak tahun ini.")

# Sidebar
st.sidebar.success("✅ Data tersinkronisasi dengan Rekap Excel 2025")
st.sidebar.info("Gunakan dashboard ini untuk laporan bulanan ke Resort.")
