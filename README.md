## AI-Based Resume Screening System
### Overview
This project is an AI-based Resume Screening System developed as part of my Data Science & Machine Learning internship.The system automates the process of screening resumes by analyzing resume text and matching it with job descriptions using Natural Language Processing (NLP) and Machine Learning techniques.The goal is to help recruiters shortlist suitable candidates efficiently while reducing manual effort and bias.

### Objectives
The objective of this project is to automate the resume shortlisting process by extracting and preprocessing resume text, matching resumes with job descriptions, ranking candidates based on relevance scores, and improving hiring efficiency using AI techniques.
  
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
- ├── AI Based Resume Screening System.ipynb
- ├── data/
- │   ├── resumes.csv
- │   └── job_description.txt
- ├── README.md

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
  
### Results
* Successfully ranked resumes based on job relevance
* Reduced manual resume screening effort
* Improved shortlisting accuracy
  
### Future Enhancements
* It uses **BERT / FastText** for better semantic understanding
* Build a **Streamlit web application**
* Add resume parsing (skills, experience, education extraction)
* It supports
  
### Author
**Apurwa Khare**
MCA (AI & ML)
Data Science & Machine Learning Intern

### License
This project is for **academic and learning purposes only**.
