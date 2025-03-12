import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Data
file_path = os.path.join(os.path.dirname(__file__), "all_data.csv")
df = pd.read_csv(file_path)
file_path_day = os.path.join(os.path.dirname(__file__), "day.csv")
df_day = pd.read_csv(file_path_day)

# Konversi kolom tanggal jika ada
if "dteday" in df_day.columns:
    df_day["dteday"] = pd.to_datetime(df_day["dteday"])
    start_date = df_day["dteday"].min()
    end_date = df_day["dteday"].max()
else:
    start_date, end_date = "Tidak Diketahui", "Tidak Diketahui"

# Sidebar untuk menampilkan rentang tanggal dan filter
st.sidebar.header("Informasi Dataset")
st.sidebar.write(f"**Tanggal Awal:** {start_date}")
st.sidebar.write(f"**Tanggal Akhir:** {end_date}")

# Opsi filter
filter_option = st.sidebar.radio("Pilih Distribusi:", ["Per Hari", "Per Jam"])

# Pisahkan Data Harian dan Jam
hari_list = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
df_harian = df[df["Kategori"].isin(hari_list)]
df_harian.set_index("Kategori", inplace=True)

df_jam = df[df["Kategori"].str.contains("Jam")]
df_jam["Jam"] = df_jam["Kategori"].str.extract("(\\d+)").astype(int)
df_jam.set_index("Jam", inplace=True)

# Streamlit Dashboard
st.title("Dashboard Casual User Bike Sharing (2011-2012)")

if filter_option == "Per Hari":
    st.subheader("Distribusi Casual User per Hari")
    fig1, ax1 = plt.subplots()
    ax1.pie(df_harian["Jumlah Casual Users"], labels=df_harian.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    ax1.set_title("Distribusi Casual User per Hari")
    st.pyplot(fig1)
    
elif filter_option == "Per Jam":
    st.subheader("Jumlah Casual User per Jam")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.bar(df_jam.index, df_jam["Jumlah Casual Users"], color='lightcoral')
    ax2.set_xlabel("Jam")
    ax2.set_ylabel("Jumlah Pengguna Kasual")
    ax2.set_title("Jumlah Casual User Berdasarkan Jam dalam Sehari")
    ax2.set_xticks(range(0, 24))
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig2)

st.write("Copyright : Stefanus Betanius Prakoso")