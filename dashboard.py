import streamlit as st
import pandas as pd
import os

st.title("📊 Quotes Dashboard")

# Check if file exists
if not os.path.exists("quotes.csv"):
    st.error("⚠️ quotes.csv not found! Please run scraper_quotes.py first.")
else:
    try:
        # Try reading with utf-8-sig
        df = pd.read_csv("quotes.csv", encoding="utf-8-sig")

        st.subheader("First 10 Quotes")
        st.dataframe(df.head(10))

        st.subheader("Search Quotes")
        keyword = st.text_input("Enter keyword (e.g., life, love, choices)")
        if keyword:
            results = df[df['quote'].str.contains(keyword, case=False, na=False)]
            if results.empty:
                st.warning(f"No quotes found for '{keyword}'")
            else:
                st.write(results)

        st.subheader("Author Breakdown")
        st.bar_chart(df['author'].value_counts())

    except Exception as e:
        st.error(f"🚨 Could not load quotes.csv: {e}")
