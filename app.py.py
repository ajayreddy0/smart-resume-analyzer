import streamlit as st
from PyPDF2 import PdfReader
import spacy
from utils.text_cleaning import clean_text
from keyword_matcher import match_keywords

nlp = spacy.load("en_core_web_sm")

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")
st.title("\U0001F4C4 Smart Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    raw_text = ""
    for page in reader.pages:
        raw_text += page.extract_text()

    cleaned_text = clean_text(raw_text)
    doc = nlp(cleaned_text)

    st.subheader("Extracted Resume Text")
    st.write(cleaned_text)

    sample_jd = st.text_area("Paste a Job Description to match against:")
    if sample_jd:
        score, matched, missing = match_keywords(cleaned_text, sample_jd)

        st.subheader("✅ Match Score")
        st.write(f"{score}%")

        st.subheader("✔️ Keywords Found")
        st.write(matched)

        st.subheader("❌ Keywords Missing")
        st.write(missing)
