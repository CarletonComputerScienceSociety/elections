from flask import Blueprint, request

# This file is part of the Carleton Computer Science Society election 
# server. It is licensed under the MIT permissive free software license.
# See LICENSE.txt.

bp = Blueprint('vote', __name__, template_folder='templates/vote')

