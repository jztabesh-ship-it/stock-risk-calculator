import streamlit as st

def calculate_risk_score(tavarrom, q_tobin, s_per_s, shakhes_saham, arz, roa, z_altman, pe):
    return (
        0.117 * tavarrom +
        0.069 * q_tobin +
        0.068 * s_per_s +
        0.067 * shakhes_saham +
        0.064 * arz +
        0.059 * roa +
        0.059 * z_altman +
        0.055 * pe +
        0.051
    )

st.set_page_config(page_title="Stock Risk Calculator", page_icon="📊", layout="centered")
st.title("📊 محاسبه‌گر ریسک سهام")

st.markdown("مقادیر هر شاخص رو وارد کن تا **Risk Score** محاسبه شود:")

tavarrom = st.number_input("📌 نرخ تورم", value=0.0)
q_tobin = st.number_input("📌 Q_Tobin", value=0.0)
s_per_s = st.number_input("📌 s_per_s", value=0.0)
shakhes_saham = st.number_input("📌 شاخص سهام", value=0.0)
arz = st.number_input("📌 نرخ ارز", value=0.0)
roa = st.number_input("📌 ROA", value=0.0)
z_altman = st.number_input("📌 Z-Altman", value=0.0)
pe = st.number_input("📌 P/E", value=0.0)

if st.button("محاسبه ریسک"):
    score = calculate_risk_score(tavarrom, q_tobin, s_per_s, shakhes_saham, arz, roa, z_altman, pe)
    st.success(f"✅ Risk Score: {score:.3f}")

