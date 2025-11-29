import streamlit as st
import summarization_lib as glib

st.set_page_config(
    page_title="Document Summarization",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Document Summarization")

input_text = st.text_area("How would you like the document summarized?")

summarize_button = st.button("Summarize", type="primary")

if summarize_button:
    st.subheader("Summary")

    with st.spinner("Working..."):
        response_content = glib.get_summary(input_text)
        st.write(response_content)

