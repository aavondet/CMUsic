import flask

# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_start.html')
    
@APP.route('/input')
def index2():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_input.html')

@APP.route('/result')
def index3():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index_result.html')

if __name__ == '__main__':
    APP.debug = True
    APP.run()
