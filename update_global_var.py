import streamlit as st
import global_vars

@st.cache_resource
def update_global():
  if global_vars.global_var is not None:
    global_vars.global_var = global_vars.global_var - 1;
  else:
    global_vars.global_var = 1000
  update_global.clear()
