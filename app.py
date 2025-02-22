import streamlit as st
import pickle
import pandas as pd
import requests

import requests


def fetch_poster(movie_id):
    bearer_token = (
        'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MDI3NTkwNmY2OTNlY2M0OWNjMjYyZjhiNGVmYmY5MSIsIm5iZiI6MTc0MDI1MjA1Mi4zODgsInN1YiI6IjY3YmEyMzk0NzQxMTUyYjA0MjBhODhmZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HTnpNjBU9Nap06LPLB1YOKcAWBchSzYMIm6XPJCgQfk')

    url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return f"http://image.tmdb.org/t/p/w500/{data['poster_path']}" if 'poster_path' in data else None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

  recommended_movies = []
  recommended_movies_posters = []
  for i in movies_list:
      movie_id = movies.iloc[i[0]].movie_id
      # fetch poster from an api
      recommended_movies.append(movies.iloc[i[0]].title)
      recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    'Can you please select a Movie?',
    movies['title'].values)

if st.button('Give recommendations'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
