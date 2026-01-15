import streamlit as st

st.set_page_config(page_title="Tabuada Inteligente", layout="centered")

st.title("📘 Tabuada Inteligente")

numero = st.number_input(
    "Digite um número para ver a tabuada:",
    min_value=0,
    max_value=1000,
    step=1
)

st.divider()

for i in range(1, 11):
    st.write(f"{numero} x {i} = {numero * i}")
