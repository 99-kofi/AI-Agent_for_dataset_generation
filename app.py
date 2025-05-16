import streamlit as st
from agent import handle_query

st.set_page_config(page_title="AI Web Data Agent", layout="wide")
st.title("🤖 AI Web Data Agent")

topic = st.text_input("🔍 Enter a topic/domain to crawl and summarize:")

limit = st.slider("Number of articles to fetch", min_value=1, max_value=10, value=3)

if st.button("Generate Dataset"):
    with st.spinner("Crawling the web, extracting and summarizing..."):
        df = handle_query(topic, limit)
        st.success("Dataset ready! Preview below 👇")
        st.dataframe(df[["title", "summary"]])

        st.download_button("Download CSV", df.to_csv(index=False), file_name=f"{topic}.csv")
        st.download_button("Download JSON", df.to_json(indent=4), file_name=f"{topic}.json")
