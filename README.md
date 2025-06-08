# 🎬 Movie Recommender System

Welcome to the **Movie Recommender System**, a content-based movie recommendation web app that helps users find similar movies based on the one they like!

🖼️ Demo
https://movie-recommender-kg.onrender.com

## 🧠 How It Works

This system uses **content-based filtering** to recommend movies. It processes metadata like:
- Title
- Genre
- Overview
- Cast
- Crew
- Keywords

It then:
1. **Combines** this information into a single 'tags' field.
2. **Cleans and stems** text data using **NLTK**.
3. **Vectorizes** the tags using **TF-IDF** or **CountVectorizer** from **Scikit-learn**.
4. **Calculates cosine similarity** to find and suggest the most similar movies.

## 🛠️ Tech Stack

- **Frontend**: HTML / CSS / Streamlit (or Flask + Bootstrap)
- **Backend**: Python
- **Libraries**: Pandas, Scikit-learn, NLTK
- **Deployment**: Render / Vercel / Localhost

## 🚀 Features

- Simple UI to input a movie name
- Recommends top 5 similar movies
- Displays posters of recommended movies using the TMDB API
- Lightweight and fast response

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/Khushi2427/KG-movie-recommender.git
cd movie-recommender

2 . Install required packages:

```bash
pip install -r requirements.txt

3. streamlit run app.py
