'''
    api.py
    Cathy Duan and Hannah Moran, 8 November 2022

    Tiny Flask API to support the met web application.
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    try:
        test = psycopg2.connect(database=config.database, user=config.user, password='')
        return test
    except Exception as e:
        print(e)
        exit()

@api.route('/mockup7') 
def get_artists():
    query = '''SELECT artist_surname, artist_firstname, artist_bio, artist_birthyear, artist_deathyear
               FROM artists 
               ORDER BY artist_surname '''

    artist_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            artist = {'artist_surname':row[0],
                        'artist_firstname':row[1],
                        'artist_bio': row[2],
                        'artist_birthyear':row[3],
                        'artist_deathyear':row[4]}
            artist_list.append(artist)
        cursor.close()
        print("app slay moment")
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)
        
    return json.dumps(artist_list)
