import flask
from flask import request
# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_start.html')

users = []
@APP.route('/submit', methods=['POST'])
def index2():
    if request.method == 'POST':
        new_user={}
        json = request.get_json()
        new_user["andrewId"] = json["id"]
        new_user["artists"] = json["artist_list"]
        new_user["genres"] = json["genre_list"]
        new_user["songs"] = json["song_list"]
        print(new_user)
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_input.html')

@APP.route('/input')
def index4():
    return flask.render_template('index_input.html')

@APP.route('/result')
def index3():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_result.html')

if __name__ == '__main__':
    APP.debug = True
    APP.run()
