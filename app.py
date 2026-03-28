import streamlit as st
import pandas as pd

# Konfigurasi Tampilan Dashboard
st.set_page_config(page_title="Penyu Monitor", layout="wide", page_icon="🐢")

# Judul Utama Dashboard
st.title("🐢 Dashboard Konservasi Penyu Resort")
st.markdown("---")

# Data Dummy (Nanti bisa kita hubungkan ke Google Sheets kamu)
data = pd.DataFrame({
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei'],
    'Jumlah Telur': [450, 600, 520, 700, 850],
    'Jumlah Sarang': [5, 7, 6, 8, 10]
})

# 1. Bagian Atas: Scorecard (Angka Ringkasan)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Telur Diamankan", value="3.120 Butir", delta="+15%")
with col2:
    st.metric(label="Total Sarang Ditemukan", value="36 Sarang", delta="+2")
with col3:
    st.metric(label="Tingkat Kelulusan (Tukik)", value="88%", delta="Stabil")

st.markdown("---")

# 2. Bagian Tengah: Grafik Batang
st.subheader("📊 Tren Penemuan Telur Per Bulan (2025)")
st.bar_chart(data=data, x='Bulan', y='Jumlah Telur', color="#2E8B57") # Warna hijau konservasi

# 3. Bagian Bawah: Tabel Data Terbaru
st.subheader("📋 Laporan Terakhir dari Lapangan")
st.table(data)

# Tombol Tambahan
if st.button('Unduh Laporan PDF (Contoh)'):
    st.success("Laporan sedang disiapkan... (Fitur ini akan aktif setelah sistem terhubung)")

# Footer
st.sidebar.info("Aplikasi ini dibuat oleh Petugas Resort untuk monitoring populasi penyu secara real-time.")
