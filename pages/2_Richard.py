import streamlit as st
from main import data

st.write('# Richard')
st.write('##')

ri_movie_list = data['Richard'].to_list()

s = ''
for i in ri_movie_list:
    if type(i) is float:
        continue
    else:
        s += "- " + str(i) + "\n"
st.markdown(s)