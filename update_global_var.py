# import streamlit as st
# @st.cache_resource
# import global_vars
# update_global.clear()

def update_global():
  # if global_vars.global_var is None:
  #   global_vars.global_var = 1000
  #   global_vars.refresh = False 
  # else:
  #   delta = global_vars.global_var
  #   global_vars.global_var = delta - 1
  #   global_vars.refresh = True

  # if global_vars.refresh:
  #     st.write(global_vars.global_var)
  #     global_vars.refresh = False
  if global_vars.global_var is not None:
    global_vars.global_var = global_vars.global_var - 1;
  else:
    global_vars.global_var = 1000

