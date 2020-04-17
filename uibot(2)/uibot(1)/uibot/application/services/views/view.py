from flask import current_app

def main_page():

    return current_app.send_static_file("index.html")