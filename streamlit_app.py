import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import global_vars
import update_global_var as ugv

if 'key' not in st.session_state:
    st.session_state['key'] = {}

# st.write(f'key = {st.session_state['key']} and count = {global_vars.global_var}')

global_vars.global_var = global_vars.global_var
# First time default call for initialization 2
# st.write('Count = ', global_vars.global_var)
st.write(f"key = {st.session_state['key']['count']} and count = {global_vars.global_var}")

if st.button('Update Count'):
  ugv.update_global()

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
