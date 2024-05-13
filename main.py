import streamlit as st
import pickle as p
import requests
movie = p.load(open('movie_list.pkl', 'rb'))
similarity=p.load(open('similarity.pkl', 'rb'))
movie_list = movie['title'].values
st.header('Movies recommender system')

select_value=st.selectbox('Select movies from dropbox',movie_list)

def recommand(name):
    index=movie[movie['title']==name].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])[:5]
    recommand_movie=[]
    movie_poster=[]
    
    for index,_ in distance:
        movie_id=movie['id'][index]
        recommand_movie.append(movie['title'][index])
        movie_poster.append(get_poster(movie_id))
    return recommand_movie,movie_poster

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=cd252c3dc235d8d9600713f92f3153bb&language=en-US".format(movie_id)
    response = requests.get(url)
    data=response.json()
    poster_path = data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path
if st.button('Show Recommand'):
    movie_name,movie_poster = recommand(select_value)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
