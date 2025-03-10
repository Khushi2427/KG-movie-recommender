import streamlit as st
import pickle
import bz2
import pandas as pd
import requests
st.title('Movie Recommendation System')
movie_dict= pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movie_dict)

similarity= pickle.load(bz2.open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    response=  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c67784e96ad4e926aa1caae95bd71dcc&language=en_US'.format(movie_id))
    data= response.json()
    return 'https://image.tmdb.org/t/p/original/'+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies= []
    recomended_movies_poster=[]
    for i in movies_list:
        movie_id= movies.iloc[i[0]].id
        recomended_movies.append(movies.iloc[i[0]].title)
        #fetch movie poster from API
        recomended_movies_poster.append(fetch_poster(movie_id))
    return recomended_movies,recomended_movies_poster

selected_movie_name = st.selectbox(
    'Select the movie',
    movies['title'].values
)

if st.button('Recommend'):
   names,posters=  recommend(selected_movie_name)
   col1, col2, col3 ,col4,col5= st.columns(5)

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
