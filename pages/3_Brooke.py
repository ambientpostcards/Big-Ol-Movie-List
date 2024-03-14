import streamlit as st
from main import data

st.write('# Brooke')
st.write('##')

br_movie_list = data['Brooke'].to_list()

s = ''
for i in br_movie_list:
    if type(i) is float:
        continue
    else:
        s += "- " + str(i) + "\n"
st.markdown(s)