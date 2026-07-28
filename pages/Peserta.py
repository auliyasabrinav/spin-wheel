import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Peserta", layout="wide")

st.title("👥 DATA PESERTA")

DATA_PATH = "data/participants.csv"

# --------------------
# Membaca Data
# --------------------
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
else:
    df = pd.DataFrame(columns=["id", "nama", "status"])
    df.to_csv(DATA_PATH, index=False)

# --------------------
# Upload CSV
# --------------------
st.subheader("📂 Upload Peserta")

uploaded_file = st.file_uploader(
    "Upload file CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df.to_csv(DATA_PATH, index=False)

    st.success("Data peserta berhasil diupload.")

    st.rerun()

# --------------------
# Statistik
# --------------------

st.metric("Jumlah Peserta", len(df))

st.divider()

# --------------------
# Tabel
# --------------------

st.subheader("Daftar Peserta")

st.dataframe(
    df,
    use_container_width=True
)
