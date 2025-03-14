import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df_all = pd.read_csv("https://raw.githubusercontent.com/steffbp123/Aplikasi-Login/refs/heads/main/Bike%20Sharing%20Dataset/Dashboard/all_data%20(1).csv")

# Konversi kolom tanggal
df_all["dteday"] = pd.to_datetime(df_all["dteday"])

# Sidebar untuk filter rentang tanggal
st.sidebar.header("Filter Rentang Tanggal")
start_date = st.sidebar.date_input("Tanggal Awal", df_all["dteday"].min())
end_date = st.sidebar.date_input("Tanggal Akhir", df_all["dteday"].max())

# Filter data berdasarkan rentang tanggal
df_filtered = df_all[(df_all["dteday"] >= pd.Timestamp(start_date)) & (df_all["dteday"] <= pd.Timestamp(end_date))]

# Data untuk Pie Chart
day_counts = df_filtered.groupby("weekday")["casual"].sum()

# Data untuk Bar Chart
hourly_counts = df_filtered.groupby("hr")["casual"].sum()

# Layout Dashboard
st.title("Dashboard Casual User Bike Sharing")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Pie Chart
ax1.pie(day_counts, labels=day_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
ax1.set_title("Distribusi Casual User per Hari")

# Bar Chart
ax2.bar(hourly_counts.index, hourly_counts.values, color='lightcoral')
ax2.set_xlabel("Jam")
ax2.set_ylabel("Jumlah Casual Users")
ax2.set_title("Jumlah Casual User Berdasarkan Jam")
ax2.set_xticks(range(0, 24))
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Tampilkan Chart di Streamlit
st.pyplot(fig)

st.caption("Copyright : Stefanus Betanius Prakoso")
