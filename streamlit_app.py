import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import global_vars
import update_global_var as ugv


import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)



st.title('Counter Example using Callbacks with args')
if 'count' not in st.session_state:
    st.session_state.count = 100

def decrement_counter(decrement_value):
    st.session_state.count -= decrement_value

increment = st.button('Decrement', on_click=decrement_counter,
    args=(1, ))

st.write('Count = ', st.session_state.count)



# # st.write(f'''
# #     <a target="_self" href="https://eox.at">
# #         <button>
# #             Please login via Google
# #         </button>
# #     </a>
# #     ''',
# #     unsafe_allow_html=True
# # )

# # if 'credits' not in st.session_state:
# #     st.session_state.credits = 1000


# from streamlit.web.server import Server

# server = Server.get_current()

# origins = ["https://neuron.affineanalytics.ai"] 

# server.enableCORS(origins=origins, methods=['POST', 'GET'], allow_credentials=True, headers=['Content-Type'])

# if st.button("Reduce Credits"):
#   st.redirect("new-page", base="https://neuron.affineanalytics.ai/#/login")
#   # st.session_state.credits -= consumed

# # st.write('Credits = ', st.session_state.credits)
# # if st.session_state.changed:
# #   st.write('Credits = ', st.session_state.credits)
# #   st.session_state.changed = False
# # else:  
# #   st.write('Credits = ', st.session_state.credits)



# st.title("Change Browser Tab URL")

# # JavaScript code to change the URL
# javascript_code = """
# <script>
#     // Change the URL without reloading the page
#     window.history.pushState({}, "", "/new-url");
# </script>
# """

# # Add a button to trigger the JavaScript code
# if st.button("Change URL"):
#     st.write("Click the button to change the URL")
#     st.write(javascript_code, unsafe_allow_html=True)

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
