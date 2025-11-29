import streamlit as st #all streamlit commands will be available through the "st" alias
import embeddings_search_lib as glib #reference to local lib script

st.set_page_config(page_title="Embeddings Search", layout="wide", page_icon="🧪") #HTML title
st.title("Embeddings Search") #page title


st.markdown("""
    <style>
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: #FAFAFA !important;
        }
    </style>

""", unsafe_allow_html=True)

input_text = st.text_input("What do you want to know about about Amazon Bedrock:")
go_button = st.button("Go Girl!", type="primary") #display a primary button

if go_button: #code in this if block will be run when the button is clicked
    
    with st.spinner("Working..."): #show a spinner while the code in this with block runs
        response_content = glib.get_similarity_search_results(question=input_text)
        
        st.table(response_content) #using table so text will wrap
        
