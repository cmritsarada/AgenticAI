import streamlit as st
import pandas as pd

from agents.parser_agent import parse_statement
from agents.categorizer_agent import categorize_transactions
from agents.analysis_agent import analyze_transactions
from agents.advisor_agent import generate_advice

st.title("💰 Statement-to-Insights Finance Agent")

uploaded_file = st.file_uploader(
    "Upload Bank Statement",
    type=["csv"]
)

if uploaded_file:

    df = parse_statement(uploaded_file)

    df = categorize_transactions(df)

    summary = analyze_transactions(df)

    advice = generate_advice(summary)

    st.subheader("Transactions")
    st.dataframe(df)

    st.subheader("Summary")
    st.write(summary)

    st.subheader("AI Insights")
    st.success(advice)