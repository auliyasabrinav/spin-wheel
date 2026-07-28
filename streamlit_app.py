import streamlit as st

st.set_page_config(
    page_title="Spin Wheel Doorprize",
    page_icon="🎉",
    layout="wide"
)

st.title("🎉 SPIN WHEELaa DOORPRIZE")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Peserta", 0)

with col2:
    st.metric("Prize", 0)

with col3:
    st.metric("Sudah Menang", 0)

with col4:
    st.metric("Sisa Peserta", 0)

st.success("Selamat datang di aplikasi Spin Wheel Doorprize.")
