import streamlit as st
import pickle
import docx
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

nltk.download('stopwords')

# Load model and TF-IDF vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text.lower())
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def read_docx(file):
    doc = docx.Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

st.title("📄 AI Resume Screener")
st.write("Upload your resume to get a predicted job category.")

uploaded_file = st.file_uploader("Upload a .docx resume file", type="docx")

if uploaded_file is not None:
    resume_text = read_docx(uploaded_file)
    cleaned_text = preprocess(resume_text)
    vector = tfidf.transform([cleaned_text])
    prediction = model.predict(vector)[0]
    st.success(f"✅ Predicted Job Role: **{prediction}**")
