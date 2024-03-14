import streamlit as st
from main import data

st.write('# Rob')
st.write('##')

ro_movie_list = data['Rob'].to_list()

s = ''
for i in ro_movie_list:
    if type(i) is float:
        continue
    else:
        s += "- " + str(i) + "\n"
st.markdown(s)