import streamlit as st
import faiss
import pickle

from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="RBI Financial AI Assistant")

st.title("RBI Financial AI Assistant")

question = st.text_input("Ask a question")

if question:

    model = SentenceTransformer("all-MiniLM-L6-v2")

    index = faiss.read_index("rbi_vector.index")

    with open("rbi_chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    query_embedding = model.encode([question])

    distances, indices = index.search(query_embedding, 3)

    st.subheader("Relevant Information")

    for idx in indices[0]:
        st.write(chunks[idx][:1000])