import streamlit as st
import pandas as pd

# Konfigurasi Tampilan
st.set_page_config(page_title="Penyu Monitor - Real Data", layout="wide", page_icon="🐢")

# Load Data dari file CSV yang kamu upload (Pastikan file CSV ada di GitHub)
# Tips: Biar gampang, kita buat data manual di dalam kode berdasarkan rekap kamu
data_rekap = [
    {"Blok": "Tegalsereh", "Bulan": "Januari", "Telur": 76, "Perjumpaan": 2},
    {"Blok": "Katapang", "Bulan": "Februari", "Telur": 68, "Perjumpaan": 2},
    {"Blok": "Panarikan", "Bulan": "Maret", "Telur": 66, "Perjumpaan": 1},
    {"Blok": "Tegalsereh", "Bulan": "April", "Telur": 76, "Perjumpaan": 1},
    {"Blok": "Pamoekan", "Bulan": "Mei", "Telur": 211, "Perjumpaan": 3},
    {"Blok": "Tegalsereh", "Bulan": "Juni", "Telur": 198, "Perjumpaan": 3},
    {"Blok": "Tegalsereh", "Bulan": "Juli", "Telur": 480, "Perjumpaan": 5},
    {"Blok": "Tegalsereh", "Bulan": "Agustus", "Telur": 282, "Perjumpaan": 2},
    {"Blok": "Pamoekan", "Bulan": "September", "Telur": 85, "Perjumpaan": 1},
    {"Blok": "Katapang", "Bulan": "Oktober", "Telur": 0, "Perjumpaan": 0},
    {"Blok": "Panarikan", "Bulan": "November", "Telur": 93, "Perjumpaan": 1},
    {"Blok": "Desember", "Bulan": "Desember", "Telur": 0, "Perjumpaan": 0},
]

df = pd.DataFrame(data_rekap)

# Judul Dashboard
st.title("🐢 Monitoring Penyu Resort - Rekap 2025")
st.markdown(f"**Update terakhir:** Maret 2026")
st.markdown("---")

# 1. Scorecards (Data Asli dari Rekap)
total_telur = df['Telur'].sum()
total_perjumpaan = df['Perjumpaan'].sum()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Telur Diamankan", value=f"{total_telur:,} Butir")
with col2:
    st.metric(label="Total Perjumpaan Penyu", value=f"{total_perjumpaan} Kali")
with col3:
    st.metric(label="Rata-rata Telur/Sarang", value=f"{round(total_telur/total_perjumpaan if total_perjumpaan > 0 else 0)} Butir")

st.markdown("---")

# 2. Grafik Tren Bulanan
st.subheader("📊 Tren Pengamanan Telur Per Bulan")
st.bar_chart(data=df, x='Bulan', y='Telur', color="#2E8B57")

# 3. Distribusi per Blok (Pie Chart)
st.subheader("📍 Distribusi Telur per Blok Lokasi")
df_blok = df.groupby('Blok')['Telur'].sum().reset_index()
st.write("Tabel Kontribusi per Lokasi:")
st.dataframe(df_blok, use_container_width=True)

# 4. Sidebar Filter
st.sidebar.header("Filter Lokasi")
blok_pilihan = st.sidebar.multiselect("Pilih Blok:", options=df['Blok'].unique(), default=df['Blok'].unique())

# Filter data berdasarkan sidebar
df_filtered = df[df['Blok'].isin(blok_pilihan)]
st.sidebar.markdown("---")
st.sidebar.write(f"Menampilkan data untuk {len(blok_pilihan)} lokasi.")
