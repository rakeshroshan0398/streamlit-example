import global_vars

def update_global():
  if global_vars.global_var is not None:
    global_vars.global_var = global_vars.global_var - 1;
