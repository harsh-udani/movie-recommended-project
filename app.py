import streamlit as st
import pickle as pk
import pandas as pd 
import numpy as np
import requests

movies_list = pk.load(open('movies.pkl','rb'))
movies_list1 = movies_list['title'].values
similarity  = pk.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response = requests.get( f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US&api_key=f8d236dc15cd72a8790fcf097b09e198")
    data = response.json()
    return " https://image.tmdb.org/t/p/w500/"+ data['poster_path']



def recomm(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    recom_movies_list = sorted(list(enumerate(distances)) , reverse=True ,key = lambda x : x[1])[1:7]
    recommended_movies = []
    recommended_movie_poster = []
    #recommended_movies.append(movie)
    for i in recom_movies_list:
        # fetching movie id
        movie_id = movies_list.iloc[i[0]]['movie_id']
        recommended_movies.append(movies_list.iloc[i[0]]['title'])
         # fetching poster API
        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_poster


st.title('Movie Recommender System')
# st.text_input("Enter The Movie Name", key="Movie_name") 

select_movie_name = st.selectbox(
    'Which movie whould you like to watch ?',
     movies_list1)

if st.button('recommend'):
    names,posters = recomm(select_movie_name)  
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


