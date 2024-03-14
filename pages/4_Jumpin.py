import streamlit as st
from main import data

st.write('# Jumpin')
st.write('##')

ju_movie_list = data['Jumpin'].to_list()

s = ''
for i in ju_movie_list:
    if type(i) is float:
        continue
    else:
        s += "- " + str(i) + "\n"
st.markdown(s)