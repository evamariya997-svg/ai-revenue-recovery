import streamlit as st
import pandas as pd

st.set_page_config(page_title="DhanWapas")
st.title("💸 DhanWapas - Revenue Recovery Agent")
st.caption("For Razorpay AI Builder Internship 2026 | Track 3: AI Revenue Recovery")

col1, col2, col3 = st.columns(3)
col1.metric("Failed Txns", "15", "₹45,200")
col2.metric("Recovered by AI", "₹12,800", "+28%")
col3.metric("Success Rate", "28%")

st.divider()

# Mock Data
txns = [
    {"id": "pay_RZP001", "name": "Aman K", "amount": 1499, "reason": "bank_timeout", "status": "Failed"},
    {"id": "pay_RZP002", "name": "Priya S", "amount": 2999, "reason": "insufficient_funds", "status": "Failed"},
    {"id": "pay_RZP003", "name": "Rahul M", "amount": 999, "reason": "card_declined", "status": "Recovered"},
]

df = pd.DataFrame(txns)
st.dataframe(df, use_container_width=True)

st.subheader("🤖 AI Agent Action")
selected = st.selectbox("Select Transaction to Recover", ["pay_RZP001", "pay_RZP002"])

if st.button("Generate AI Recovery"):
    if selected == "pay_RZP001":
        st.success("AI Reasoning: Failure = bank_timeout. Strategy = Retry same method with 1-click link. Message tone = Reassuring.")
        st.code("Hi Aman, your payment of ₹1499 timed out. No worries! Retry securely here: rzp.io/r/pay_RZP001 - DhanWapas AI")
    else:
        st.success("AI Reasoning: Failure = insufficient_funds. Strategy = Suggest UPI + EMI option.")
        st.code("Hi Priya, your ₹2999 payment failed due to low balance. Try UPI or convert to 3-month EMI: rzp.io/r/pay_RZP002")

st.info("Note: Synthetic/demo data only. No real Razorpay data used.")
