import streamlit as st

from main import data

st.write('# Rhonda')
st.write('##')

rh_movie_list = data['Rhonda'].to_list()
print(rh_movie_list)
s = ''
for i in rh_movie_list:
    if type(i) is float:
        continue
    else:
        s += "- " + str(i) + "\n"
st.markdown(s)
