import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=663946077f71ad69d0ad466f9ff0b8ae&language=en-US".format(movie_id))
    data = response.json()  
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

def recommend(movie): 
    movie_index = movies[movies['title']==movie].index[0]
    similarity_of_movies = similarity[movie_index]
    sorted_movies = sorted(list(enumerate(similarity_of_movies)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in sorted_movies:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))   
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.markdown("""
<style>
.css-czk5ss.e16jpq800{
    visibility: hidden;        
}
.css-cio0dv.ea3mdgi1{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("Movie Recommender System")
selected_movie_name = st.selectbox("Select a movie", movies['title'].values)  
button = st.button("Recommend")
if button:
    recommended_movies, recommended_movies_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])










