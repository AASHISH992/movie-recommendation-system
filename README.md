# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Project-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Overview
This project is a **Machine Learning-based Movie Recommendation System** that suggests movies based on similarity.

It uses the **TMDB movie dataset** and applies **content-based filtering** techniques to recommend movies similar to the one selected by the user.

---

## 🚀 Features
- 🎯 Personalized movie recommendations  
- 🧠 Content-based filtering using cosine similarity  
- 📊 Data preprocessing and feature extraction  
- 🌐 Interactive UI built with Streamlit  
- ⚡ Real-time recommendation system  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Framework:** Streamlit  
- **Dataset:** TMDB Movie Dataset  

---

## ⚙️ How It Works
1. Load TMDB dataset  
2. Preprocess data (genres, keywords, etc.)  
3. Convert text into vectors  
4. Compute similarity using cosine similarity  
5. Recommend top similar movies  

---

## 📸 Demo

### 🔹 Home Page
![Home]("C:/Users/Sud//Pictures/Screenshots/Screenshot 2026-04-14 132446.png")

### 🔹 Recommendation Output
![Output](add-your-screenshot-link-here)

---

## ▶️ Run Locally

```bash
# Clone the repository
git clone https://github.com/AASHISH992/movie-recommendation-system.git

# Navigate into the folder
cd movie-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
