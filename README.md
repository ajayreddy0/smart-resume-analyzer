# 📄 Smart Resume Analyzer

An intelligent resume analysis tool that uses **NLP and keyword matching** to evaluate resumes against job descriptions. Built with Python and Streamlit.

---

## 🔍 Features
- ✔️ Upload and parse PDF resumes
- ✔️ Clean and process text using spaCy NLP
- ✔️ Match resume content with job descriptions
- ✔️ Display keyword match score, matched & missing terms
- ✔️ Simple, clean, interactive UI with Streamlit

---

## 🚀 Demo
To run the app locally:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

Then open the browser at `http://localhost:8501`

---

## 🚜 Use Case
> Helps job seekers improve their resumes by analyzing keyword alignment with job descriptions. Especially useful for ATS (Applicant Tracking System) optimization.

---

## ⚖️ Tech Stack
- Python
- Streamlit
- spaCy (NLP)
- PyPDF2
- Regex

---

## 📁 Project Structure
```
smart-resume-analyzer/
├── app.py                  # Main Streamlit app
├── keyword_matcher.py     # Keyword matching logic
├── requirements.txt
├── utils/
│   └── text_cleaning.py   # Resume cleaning module
```

---

## 🌟 Future Improvements
- [ ] Section-based resume parsing (Skills, Education, Experience)
- [ ] PDF report export of feedback
- [ ] More intelligent keyword matching (TF-IDF or cosine similarity)
- [ ] Save and track scores for improvement over time

---

## 🌝 Author
**Ajay Reddy**  
[GitHub](https://github.com/ajayreddy0) 

---

## ✨ Show some love
If you find this useful, give it a ⭐ on GitHub and share with your network!
