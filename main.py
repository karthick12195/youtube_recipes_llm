import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO

st.title('Ranveer Brar Recipes from YouTube')
df = pd.read_csv('data/recipe_with_instructions.csv')

recipe_selection = st.selectbox("Choose a recipe from below to see ingredients and instructions", df['title'].drop_duplicates(), placeholder="Search recipes...", index=None)

if recipe_selection:
    df_filtered = df[df['title']==recipe_selection]
    st.subheader(df_filtered['title'].values[0])
    st.markdown("[YouTube Link](https://www.youtube.com/watch?v={})".format(df_filtered['video_id'].values[0]))
    st.image(Image.open(BytesIO(requests.get(df_filtered['thumbnail'].values[0]).content)))
    st.markdown('### Ingredients')
    st.markdown(df_filtered['ingredients'].values[0])
    st.markdown('### Recipe')
    st.markdown(df_filtered['recipe'].values[0])
else:
    df_filtered = df

