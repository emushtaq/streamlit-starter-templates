import streamlit as st
import spacy_streamlit

models = ["en_core_web_sm", "de_core_news_sm"]
default_text = "Sundar Pichai is the CEO of Google."

st.header("Demo - Spacy token visualization")
st.text("This is a prototype to try out Spacy and Streamlit")

spacy_streamlit.visualize(models, default_text)