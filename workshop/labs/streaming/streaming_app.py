import streaming_lib as glib  # reference to local lib script
import streamlit as st

st.set_page_config(
    page_title="Response Streaming",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"

    )  # HTML title
st.image("Brain.png", width=150)
st.title("Response Streaming using Converse Streaming API")  # page title

input_text = st.text_area("Ask your question", label_visibility="collapsed")
go_button = st.button("Go", type="primary")  # display a primary button

if go_button:  # code in this if block will be run when the button is clicked

    with st.empty():
        combined_response = ""
        
        def streaming_callback(chunk):
            global combined_response
            
            combined_response += chunk
            st.write(combined_response)
        
        glib.get_streaming_response(prompt=input_text, streaming_callback=streaming_callback)

