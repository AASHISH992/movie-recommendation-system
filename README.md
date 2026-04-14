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
<img width="1849" height="1079" alt="Screenshot 2026-04-14 132446" src="https://github.com/user-attachments/assets/be4d2450-efa6-4e53-b753-7db4c0a37d4a" />


### 🔹 Recommendation Output

<img width="1847" height="1079" alt="Screenshot 2026-04-14 132502" src="https://github.com/user-attachments/assets/1538fb1c-2e3b-4ff0-a40d-3192c3f9f9bc" />

<img width="1856" height="1079" alt="home" src="https://github.com/user-attachments/assets/7897071d-ac43-4745-a0c9-3e3366b61d3e" />

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
