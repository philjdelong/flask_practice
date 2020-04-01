from flask import Blueprint

home_view = Blueprint("home_view", __name__)
@home_view.route("/", methods=['GET'])

def display_home_page():
    return "<h1>SAMPLE</h1><p>Home page</p>"
