
from flask import jsonify, request
from functools import wraps
import os

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == os.getenv("BASIC_AUTH_USER") and password == os.getenv("BASIC_AUTH_PASS")

def authenticate():
    """Sends a 401 response that enables basic auth"""
    response = {
        'status': False,
        'message': 'Unauthorized'
    }
    return jsonify(response), 401

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated