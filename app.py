import streamlit as st
from search_threads import search_threads

st.set_page_config(page_title="ThreadSeeker", layout="wide")
st.title("🧵 ThreadSeeker — AI-Curated Social Thread Explorer")

st.markdown("Search smart: Describe the kind of threads you want in plain English. Get relevant results + LLaMA-powered insights.")

query = st.text_input("🔍 What's on your mind?", placeholder="e.g. Deep convos about AI ethics with humor")

top_k = st.slider("Number of results", min_value=1, max_value=10, value=5)

if st.button("Search") and query:
    with st.spinner("Searching and talking to LLaMA..."):
        results = search_threads(query, top_k=top_k)

    for result in results:
        st.markdown("---")
        st.subheader(f"🧵 {result['title']}")
        st.markdown(f"**Content:** {result['content']}")
        st.markdown(f"**Semantic Match Score:** `{result['score']:.4f}`")
        st.info(f"💡 **Why this?** {result['why_this']}")
