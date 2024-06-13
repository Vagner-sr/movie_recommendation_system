import streamlit as st
import pickle


df_movies = pickle.load(open('\new_df.pkl', 'rb'))
similarity = pickle.load(open('\similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = df_movies[df_movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]

    recomended_movies = []
    for i in movies_list:
        recomended_movies.append(df_movies.iloc[i[0]]['title'])
    return recomended_movies

st.title('Movie Recommendation System')

selected_movie = st.selectbox('choose a movie', df_movies['title'])

if st.button('select'):
    recommendations = recommend(selected_movie)
    st.subheader('We believe you will also enjoy these movies:')
    for i in recommendations:
        st.write(i)
