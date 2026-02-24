import streamlit as st
import os
from utils.fetch_news import get_mobile_news
from utils.fetch_macro import get_macro_indicators_nigeria, get_macro_indicators_kenya
from utils.scrapers import get_competitor_news
from utils.summarizer import summarize_text

st.set_page_config(page_title="Agent007 - Mobile AI Researcher", layout="wide")

st.title("📱 Agent007 - Mobile Industry Intelligence Dashboard")
st.markdown("---")

section = st.sidebar.radio("Navigation", [
    "Nigeria",
    "Kenya",
    "Competitor Moves",
    "Economic Indicators"
])

# ------------------------
# NIGERIA
# ------------------------
if section == "Nigeria":
    st.header("🇳🇬 Nigeria Market Overview")

    news_ng = get_mobile_news(country="ng")

    if news_ng:
        combined = " ".join([article['title'] for article in news_ng[:5]])
        summary = summarize_text(combined)

        st.subheader("AI Weekly Summary")
        st.success(summary)

        with st.expander("View Raw Articles"):
            for article in news_ng[:5]:
                st.markdown(f"- [{article['title']}]({article['url']})")

# ------------------------
# KENYA
# ------------------------
elif section == "Kenya":
    st.header("🇰🇪 Kenya Market Overview")

    news_ke = get_mobile_news(country="ke")

    if news_ke:
        combined = " ".join([article['title'] for article in news_ke[:5]])
        summary = summarize_text(combined)

        st.subheader("AI Weekly Summary")
        st.success(summary)

        with st.expander("View Raw Articles"):
            for article in news_ke[:5]:
                st.markdown(f"- [{article['title']}]({article['url']})")

# ------------------------
# COMPETITORS
# ------------------------
elif section == "Competitor Moves":
    st.header("🔥 Competitor Activity")

    xiaomi = get_competitor_news("Xiaomi", "Nigeria")
    tecno = get_competitor_news("Tecno", "Kenya")

    st.subheader("Xiaomi - Nigeria")
    for item in xiaomi[:5]:
        st.markdown(f"- {item['title']}")

    st.subheader("Tecno - Kenya")
    for item in tecno[:5]:
        st.markdown(f"- {item['title']}")

# ------------------------
# ECONOMIC
# ------------------------
elif section == "Economic Indicators":
    st.header("🌍 Economic Indicators")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Nigeria")
        data = get_macro_indicators_nigeria()
        for k, v in data.items():
            st.metric(k, v)

    with col2:
        st.subheader("Kenya")
        data = get_macro_indicators_kenya()
        for k, v in data.items():
            st.metric(k, v)

st.markdown("---")
st.caption("Powered by Agent007 AI")
