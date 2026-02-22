## AI-Based Resume Screening System

### Overview

This project is an AI-based Resume Screening System developed as part of my Data Science & Machine Learning internship.The system automates the process of screening resumes by analyzing resume text and matching it with job descriptions using Natural Language Processing (NLP) and Machine Learning techniques.The goal is to help recruiters shortlist suitable candidates efficiently while reducing manual effort and bias.

### Objectives
* Automate resume shortlisting
* Extract and preprocess resume text
* Match resumes with job descriptions
* Rank candidates based on relevance score
* Improve hiring efficiency using AI
  
### Technologies & Tools Used
* **Python**
* **Jupyter Notebook**
* **Pandas & NumPy** – Data handling
* **NLTK / spaCy** – Text preprocessing
* **Scikit-learn** – Machine Learning models
* **TF-IDF Vectorizer** – Feature extraction
* **Cosine Similarity** – Resume–JD matching

### System Workflow

1. Load resumes and job description data
2. Clean and preprocess text (lowercasing, stopword removal, lemmatization)
3. Convert text into numerical features using TF-IDF
4. Calculate similarity between resumes and job description
5. Rank resumes based on matching score
6. Display shortlisted candidates

### Machine Learning Approach

* **Text Vectorization**: TF-IDF
* **Similarity Metric**: Cosine Similarity
* **Evaluation**: Relevance score-based ranking

### Project Structure
AI-Based-Resume-Screening-System/
│
├── AI Based Resume Screening System.ipynb
├── data/
│   ├── resumes.csv
│   └── job_description.txt
├── README.md

### Key Features
- Automated resume shortlisting
- Job description–based matching
- Resume ranking using similarity scores
- Scalable and reusable pipeline

### Learning Outcomes
- Practical understanding of NLP pipelines
- Experience with TF-IDF and cosine similarity
- Hands-on ML project implementation
- Improved data preprocessing and analysis skills
  
## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install required libraries

```bash
pip install pandas numpy scikit-learn nltk spacy
```

3. Open Jupyter Notebook

```bash
jupyter notebook
```

4. Run `AI Based Resume Screening System.ipynb`

---

## ✅ Results

* Successfully ranked resumes based on job relevance
* Reduced manual resume screening effort
* Improved shortlisting accuracy

---

## 🚀 Future Enhancements

* Use **BERT / FastText** for better semantic understanding
* Build a **Streamlit web application**
* Add resume parsing (skills, experience, education extraction)
* Multi-job role support

---

## 👩‍💻 Author

**Apurwa Khare**
MCA (AI & ML)
Data Science & Machine Learning Intern

---

## 📜 License

This project is for **academic and learning purposes only**.
