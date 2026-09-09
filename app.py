import streamlit as st
from datetime import datetime, timezone
from risk_engine.score import calculate_global_risk
from data_sources.market import get_demo_market_data

st.set_page_config(page_title="Global Energy War Dashboard", page_icon="🌍", layout="wide")
st.title("🌍 Global Energy War Dashboard")
st.caption("Global Energy Supply Chain & Geopolitical Risk Monitor — V1")

data = get_demo_market_data()
risk = calculate_global_risk(data)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Energy Risk", f"{risk['total']:.0f}/100", risk["regime"])
c2.metric("Brent", f"${data['brent']:.2f}", f"{data['brent_1d']:+.1f}%")
c3.metric("Hormuz Risk", f"{data['hormuz_risk']:.0f}/100")
c4.metric("Bab el-Mandeb", f"{data['bab_risk']:.0f}/100")

st.divider()
left, right = st.columns(2)
with left:
    st.subheader("⚠️ Risk pillars")
    for k, v in risk["pillars"].items():
        st.progress(int(v), text=f"{k}: {v:.0f}/100")
with right:
    st.subheader("🔗 Transmission chain")
    st.markdown("""
    **Geopolitical shock** → **Chokepoint disruption** →
    **Physical supply / shipping stress** → **Oil & LNG prices** →
    **Inflation** → **Central-bank pressure** → **Bonds / equities / Canada**
    """)

st.divider()
st.subheader("🚨 Current alerts")
alerts = []
if data["brent"] >= 100: alerts.append("🔴 Brent is at/above $100.")
if data["hormuz_risk"] >= 80: alerts.append("🔴 Hormuz risk is severe.")
if data["bab_risk"] >= 75: alerts.append("🔴 Bab el-Mandeb risk is high.")
if risk["total"] >= 70: alerts.append("🟥 Global energy stress is in the severe regime.")
for a in alerts or ["🟢 No V1 threshold alerts."]:
    st.write(a)

st.caption(f"Dashboard timestamp: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
