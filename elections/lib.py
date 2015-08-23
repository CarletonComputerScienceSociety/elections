# This file is part of the Carleton Computer Science Society election 
# server. It is licensed under the MIT permissive free software license.
# See LICENSE.txt.

from flask import request, abort
from functools import wraps

def _has_logged_in():
    """
    This function returns True iff:

    1. Authentication has been completed
    2. Authentication is valid.

    Currently this is unimplemented pending knowledge of 
    how the SCS authentication system works.
    """
    return True

def require_login(func):
    """
    This decorator checks if the user has been 
    authenticated with the associated login page
    before calling the given function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if _has_logged_in():
            return func(*args, **kwargs)
        else:
            # Forbidden, login invalid or non existant.
            # TODO: Redirect to login page.
            abort(403)
    return wrapper
