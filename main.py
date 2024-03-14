import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='Movie List', layout='wide')

with st.container():
    st.title("Big Ol' Movie List")
    st.write('---')
    st.write('##')

sheet_id = '1vLe5bmTUmp9DKm6zWqkGGh8vLxYCXT1OwPOogjUjDMI'
sheet_name = 'Movies'
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(sheet_id, sheet_name)

data = pd.read_csv(gsheet_url)
with st.container():
    st.dataframe(data, use_container_width=True)

# wrapped in a list, take first column set and pass sets of other columns as arguments
common_movie_list = list(set(data.Rhonda).intersection(set(data.Richard), set(data.Brooke),
                         set(data.Jumpin), set(data.Rob)))
# st.write(common_movie_list)




# print(common_movie_list)
# rh_movie_list = data['Rhonda'].to_list()
# print(rh_movie_list)
# s = ''
# for i in rh_movie_list:
#     s += "- " + str(i) + "\n"
# st.markdown(s)




# Table of all movies
# Click on a title to pull in information from MovieDB
# List of common movies
# Page for each user
