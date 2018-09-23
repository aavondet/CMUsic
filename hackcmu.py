import flask
from flask import request
# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_start.html')
lst = []   
@APP.route('/login',methods=['POST'])
def index2():
    """ Displays the index page accessible at '/'
    """
    newUser={}
    newUser[id] = request.form['id']


    artistList=request.form['artist_list']
    lst[] += 
    return flask.render_template('index_input.html')

@APP.route('/result')
def index3():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_result.html')

if __name__ == '__main__':
    APP.debug = True
    APP.run()
