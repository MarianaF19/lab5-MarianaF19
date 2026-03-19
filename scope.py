int_global = None
str_global = None

def set_globals(some_int, some_str):
    """
    Asigna valores a las variables globales.
    """
    global int_global
    global str_global
    
    int_global = some_int
    str_global = some_str

def get_globals():
    """
    Recupera los valores actuales de las variables globales.
    """
    return (int_global, str_global)