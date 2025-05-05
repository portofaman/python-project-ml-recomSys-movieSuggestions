
![Static Badge](https://img.shields.io/badge/code-python_3.12-red) ![Static Badge](https://img.shields.io/badge/web_ui-streamlit_1.42.2-blue)

# Movie Recommender System

## Overview
This is a **Movie Recommender System** built using **Streamlit** for the frontend and **Google Colab** for data preprocessing. The system suggests movies based on a selected title and displays movie posters using The Movie Database (**TMDb**) API.

## Features
- Recommends **5 similar movies** based on the selected movie.
- Fetches and displays **movie posters** using TMDb API.
- Uses **precomputed similarity scores** for recommendations.
- Simple and interactive **Streamlit UI**.

## Tech Stack
- **Python** (Main programming language)
- **Pandas** (Data handling)
- **Scikit-learn** (Similarity computations)
- **Pickle** (Storing precomputed data)
- **Streamlit** (Web UI)
- **Google Colab** (Data preprocessing)
- **Requests** (Fetching data from TMDb API)

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### **2. Install Dependencies**
```bash
pip install streamlit pandas requests scikit-learn
```

### **3. Download Required Files**
- Ensure `movie_dict.pkl` and `similarity.pkl` are present in the project directory. These files contain movie data and precomputed similarity scores.

### **4. Run the Streamlit App**
```bash
streamlit run app.py
```

## How It Works
### **1. Data Preprocessing (Google Colab)**
- **Movie data** is processed and stored in `movie_dict.pkl`.
- **Similarity scores** between movies are computed and saved in `similarity.pkl`.
- Preprocessed files are downloaded and used in the Streamlit app.

### **2. Movie Recommendation Logic**
- Uses **cosine similarity** on movie metadata to find similar movies.
- The top 5 most similar movies are recommended.

### **3. Fetching Movie Posters**
- The `fetch_poster(movie_id)` function retrieves movie posters using the **TMDb API**.
- Posters are displayed along with movie names in the Streamlit UI.

### **4. Feel of the WebApp**
![image](https://github.com/user-attachments/assets/9125aa3e-d3fb-42fa-987d-d6b4600bbd76)


## Usage
1. Select a movie from the dropdown.
2. Click **'Give recommendations'**.
3. View the **recommended movies and posters**.

## Future Improvements
- Add **hybrid filtering** (content + collaborative recommendations).
- Implement **user-based recommendations**.
- Improve **UI design** and make it more interactive.

## License
This project is open-source and available under the **MIT License**.


