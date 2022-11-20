'''
    app.py
    Cathy Duan and Hannah Moran, 8 November 2022

    A small Flask application that provides a barelywebsite with an accompanying
    API (which is also tiny) to support that website.
'''
import flask 
from flask import Flask, request
import argparse
import api

######### Initializing Flask #########
app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

######### The website routes #########
@app.route('/') 
def get_index_page():
    return flask.render_template('index.html')

@app.route('/browse-all')
def browse_all():
    # attempt to read collections params
    if request.args.get('collections'):
        # '<h1>Testing: {}</h1>'.format(collection)
        return flask.render_template('mockup2.html')
    
    # non functional but placeholder for future
    if request.args.get('geographic_locations'):
        return flask.render_template('mockup2.html')

    # non functional but placeholder for future
    if request.args.get('materials'):
        return flask.render_template('mockup2.html')
        
    return flask.render_template('mockup2.html')

@app.route('/collections')
def collections():
    return flask.render_template('mockup3.html')
    
@app.route('/artists')
def artists():
    return flask.render_template('mockup5.html')

@app.route('/artwork')
def artwork():
    return flask.render_template('mockup6.html')

@app.route('/randomizer')
def randomizer():
    return flask.render_template('mockup6.html')

@app.route('/artist') 
def artist():
    return flask.render_template('mockup7.html')

@app.route('/map')
def map():
    return flask.render_template('mockup8.html')

######## Running the website server #########
if __name__ == '__main__':
    parser = argparse.ArgumentParser('Parser')
    parser.add_argument('host', help = 'this is host')
    parser.add_argument('port', type = int, help = 'this is a port')
    arguments = parser.parse_args()

    app.run(host = arguments.host, port = int(arguments.port), debug = True)