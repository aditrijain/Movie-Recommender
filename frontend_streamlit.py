import streamlit as st
import pickle
import requests
new_df=pickle.load(open('movie.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
def fetch_poster(movie_index):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_index}?api_key=36fc4681313d75105c5edefa8e827849&language=en-US')
    data=response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/original'+data['poster_path']
def recommend(movie):
    movie_index=new_df[new_df['title_y']==movie.lower()].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=new_df.iloc[i[0]]['id']
        recommended_movies.append(new_df.iloc[i[0]].title_y)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_list=new_df['title_y'].values
#print(movies_list)
st.title("Movie recommendations")
movie_selected=st.selectbox('Select Movie',movies_list)
if st.button('Recommend'):
    recommendations,posters=recommend(movie_selected)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])

