import streamlit as st
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers.pipelines import pipeline

st.cache(show_spinner=False)

def create_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(
        "twmkn9/distilbert-base-uncased-squad2")
    model = AutoModelForQuestionAnswering.from_pretrained(
    "twmkn9/distilbert-base-uncased-squad2")
    nlp_pipe = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return nlp_pipe

npl_pipe = create_pipeline()

st.header("Huggingface + Streamlit Question Answering model")
st.text("This is a prototype to try out Streamlit with a pretrained BERT model from Huggingface")

add_text_sidebar = st.sidebar.title("Menu")
add_text_sidebar = st.sidebar.text("Just some random text.")

question = st.text_input(label='Insert a question.')
text = st.text_area(label="Context")

if (not len(text) == 0) and (not len(question) == 0):
    x_dict = npl_pipe(context=text, question=question)
    print(f"Question: {question}, Pipeline: {x_dict}")
    st.text(f"Answer: {x_dict['answer']}")
