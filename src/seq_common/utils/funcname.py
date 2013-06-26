import inspect

def funcname():
    """
    Used to return the name of the calling function
    """
    return inspect.stack()[1][3]
