'''
    app.py
    Cathy Duan and Hannah Moran, 8 November 2022

    A small Flask application that provides a barelywebsite with an accompanying
    API (which is also tiny) to support that website.
'''
import flask
import argparse
import api

######### Initializing Flask #########
app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

######### The website routes #########
@app.route('/') 
def get_main_page():
    return flask.render_template('index.html')

@app.route('/mockup7') 
def mockup7():
    return flask.render_template('mockup7.html')

######## Running the website server #########
if __name__ == '__main__':
    parser = argparse.ArgumentParser('Parser')
    parser.add_argument('host', help = 'this is host')
    parser.add_argument('port', type = int, help = 'this is a port')
    arguments = parser.parse_args()

    app.run(host = arguments.host, port = int(arguments.port), debug = True)