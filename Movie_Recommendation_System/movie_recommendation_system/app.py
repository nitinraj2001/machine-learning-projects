from cmath import pi
import streamlit as st;
import pickle;

movies_list=pickle.load(open('movies.pkl','rb'))
movies_list=movies_list['title'].values
st.title("movie recommendation system");
selected_movie_name=st.selectbox('How would u like to be contacted?',movies_list)

def recommend(selected_movie_name):
    return 1

if st.button('Recommend movies'):
    recommend(selected_movie_name)
    #st.write("welcome to the world of recommendation by nitinraj2001@gmail.com")