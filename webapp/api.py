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
import re
import urllib.request
# from met_image_url_scraper import *

api = flask.Blueprint('api', __name__)

def get_connection():
    try:
        test = psycopg2.connect(database=config.database, user=config.user, password='')
        return test
    except Exception as e:
        print(e)
        exit()

def image_url(page_url):
    ''' Given the URL for one of the Met's single-artwork pages, retrieve
        that page, extract the artwork's image url, and return that url.
        If this fails, return an empty string. '''
    data_from_server = urllib.request.urlopen(page_url).read()
    string_from_server = data_from_server.decode('utf-8')
    match = re.search(r'<img id="artwork__image".*src="([^"]*)"', string_from_server)
    print(string_from_server)
    if match:
        print(match.group(1) + "hi")
        return match.group(1)
    return ''

@api.route('/browse-all')
def browse_all():
    # collections menu query
    collections_query = '''SELECT department_name
                            FROM collections
                            ORDER BY department_name;'''
    collections_menu = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(collections_query, tuple())
        for row in cursor:
            cur_collections = {'collection':row[0]}
            collections_menu.append(cur_collections)
        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    # geographic locations menu
    geographic_locations_query = '''SELECT country_name
                                    FROM geographic_locations
                                    ORDER BY country_name;'''

    geographic_locations_menu = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(geographic_locations_query, tuple())
        for row in cursor:
            cur_geo = {'country_name':row[0]}
            geographic_locations_menu.append(cur_geo)
        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    # materials menu
    materials_query = '''SELECT DISTINCT material_type, COUNT(material_type)
                        FROM materials
                        GROUP BY material_type
                        ORDER BY COUNT(material_type)
                        OFFSET 750;'''

    materials_menu = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(materials_query, tuple())
        for row in cursor:
            cur_material = {'material_type':row[0]}
            materials_menu.append(cur_material)
        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)
    
    query = '''SELECT artworks.id, artworks.artwork, artworks.art_date, artworks.material_id, artworks.artist_id, artworks.geographic_location_id, artworks.department_id, artists.id, artists.artist_firstname, artists.artist_surname, materials.id, materials.material_type,
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name, artworks.link_resource
                FROM artworks, artists, materials, collections, geographic_locations
                WHERE artists.id = artworks.artist_id
                AND materials.id = artworks.material_id
                AND geographic_locations.id = artworks.geographic_location_id
                AND collections.id = artworks.department_id
                ORDER BY artworks.artwork, artworks.id LIMIT 10'''

    current_browsing = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            current = {'artwork':row[1],
                        'art_date':row[2],
                        'artist_firstname': row[8],
                        'artist_surname':row[9],
                        'material_type':row[11],
                        'link_resource': row[16],
                        'artwork_id': row[0]}
            # print(image_url(row[16]) + "test!")
            current_browsing.append(current)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    browse_all_page = {'collections' : collections_menu, 'geographic_locations' : geographic_locations_menu, 'materials' : materials_menu, 'current_browsing' : current_browsing}
    return json.dumps(browse_all_page)  
    
@api.route('/browse-all/collections/<collection_name>')
def browse_all_collections(collection_name):
    collection_name_list = collection_name.split("-")
    collection_name = " ".join(collection_name_list)
    collection_name_search = "%" + collection_name + "%"
    query = '''SELECT artworks.id, artworks.artwork, artworks.art_date, artworks.material_id, artworks.artist_id, artworks.geographic_location_id, artworks.department_id, artists.id, artists.artist_firstname, artists.artist_surname, materials.id, materials.material_type,
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name, artworks.link_resource
                FROM artworks, artists, materials, collections, geographic_locations
                WHERE artists.id = artworks.artist_id
                AND materials.id = artworks.material_id
                AND geographic_locations.id = artworks.geographic_location_id
                AND collections.id = artworks.department_id
                AND LOWER(collections.department_name) LIKE LOWER(%s)
                ORDER BY artworks.artwork, artworks.id'''

    current_browsing = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (collection_name_search,))
        for row in cursor:
            current = {'artwork':row[1],
                        'art_date':row[2],
                        'artist_firstname': row[8],
                        'artist_surname':row[9],
                        'material_type':row[11],
                        'artwork_id': row[0]}
            current_browsing.append(current)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    browse_all_page = {'current_browsing' : current_browsing}
    return json.dumps(browse_all_page)    
   
@api.route('/browse-all/geographic_locations/<geographic_location_name>')
def browse_all_geographic_locations(geographic_location_name):
    print(geographic_location_name)
    geographic_location_name_list = re.split(', |_|-|! |\|', geographic_location_name)
    geographic_location_name = " ".join(geographic_location_name_list)
    geographic_location_name_search = "%" + geographic_location_name + "%"
    print(geographic_location_name)
    query = '''SELECT artworks.id, artworks.artwork, artworks.art_date, artworks.material_id, artworks.artist_id, artworks.geographic_location_id, artworks.department_id, artists.id, artists.artist_firstname, artists.artist_surname, materials.id, materials.material_type,
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name, artworks.link_resource
                FROM artworks, artists, materials, collections, geographic_locations
                WHERE artists.id = artworks.artist_id
                AND materials.id = artworks.material_id
                AND geographic_locations.id = artworks.geographic_location_id
                AND collections.id = artworks.department_id
                AND LOWER(geographic_locations.country_name) LIKE LOWER(%s)
                ORDER BY artworks.artwork, artworks.id'''

    current_browsing = []
    print("test")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (geographic_location_name_search,))
        for row in cursor:
            current = {'artwork':row[1],
                        'art_date':row[2],
                        'artist_firstname': row[8],
                        'artist_surname':row[9],
                        'material_type':row[11],
                        'artwork_id': row[0]}
            current_browsing.append(current)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    browse_all_page = {'current_browsing' : current_browsing}
    return json.dumps(browse_all_page)    
   
@api.route('/browse-all/materials/<material_name>')
def browse_all_materials(material_name):
    material_name_list = re.split(', |_|-|! |\|', material_name)
    material_name = " ".join(material_name_list)
    material_name_search = "%" + material_name + "%"
    query = '''SELECT artworks.id, artworks.artwork, artworks.art_date, artworks.material_id, artworks.artist_id, artworks.geographic_location_id, artworks.department_id, artists.id, artists.artist_firstname, artists.artist_surname, materials.id, materials.material_type,
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name, artworks.link_resource
                FROM artworks, artists, materials, collections, geographic_locations
                WHERE artists.id = artworks.artist_id
                AND materials.id = artworks.material_id
                AND geographic_locations.id = artworks.geographic_location_id
                AND collections.id = artworks.department_id
                AND LOWER(materials.material_type) LIKE LOWER(%s)
                ORDER BY artworks.artwork, artworks.id'''

    current_browsing = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (material_name_search,))
        for row in cursor:
            current = {'artwork':row[1],
                        'art_date':row[2],
                        'artist_firstname': row[8],
                        'artist_surname':row[9],
                        'material_type':row[11],
                        'artwork_id': row[0]}
            # url = row[16]
            # url = url[11:-1]
            # print(url)
            # print(image_url(url))
            current_browsing.append(current)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    browse_all_page = {'current_browsing' : current_browsing}
    return json.dumps(browse_all_page)    

@api.route('/browse-all/q/<query_name>')
def browse_all_query(query_name):
    query_name_list = re.split(', |_|-|! |\|', query_name)
    query_name = " ".join(query_name_list)
    query_name_search = "%" + query_name + "%"
    query = '''SELECT artworks.id, artworks.artwork, artworks.art_date, artworks.material_id, artworks.artist_id, artworks.geographic_location_id, artworks.department_id, artists.id, artists.artist_firstname, artists.artist_surname, materials.id, materials.material_type,
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name, artworks.link_resource
                FROM artworks, artists, materials, collections, geographic_locations
                WHERE artists.id = artworks.artist_id
                AND materials.id = artworks.material_id
                AND geographic_locations.id = artworks.geographic_location_id
                AND collections.id = artworks.department_id
                AND LOWER(artworks.artwork) LIKE LOWER(%s)
                ORDER BY artworks.artwork, artworks.id'''

    current_browsing = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (query_name_search,))
        for row in cursor:
            current = {'artwork':row[1],
                        'art_date':row[2],
                        'artist_firstname': row[8],
                        'artist_surname':row[9],
                        'material_type':row[11],
                        'artwork_id': row[0]}
            current_browsing.append(current)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    browse_all_page = {'current_browsing' : current_browsing}
    return json.dumps(browse_all_page)    

@api.route('/collections') 
def get_collections():
    query = '''SELECT department_name
                FROM collections
                ORDER BY department_name;'''

    collections_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            collection = {'department_name':row[0]}
            collections_list.append(collection)
        cursor.close()
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(collections_list)


@api.route('/artists') 
def get_artists():
    query = '''SELECT id, artist_surname, artist_firstname, artist_bio, artist_birthyear, artist_deathyear
               FROM artists 
               ORDER BY artist_surname'''

    artist_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            artist = {  'artist_id' : row[0],
                        'artist_surname':row[1],
                        'artist_firstname':row[2],
                        'artist_bio': row[3],
                        'artist_birthyear':row[4],
                        'artist_deathyear':row[5]}
            artist_list.append(artist)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    browse_artist_page = {'artist_list' : artist_list}
    return json.dumps(browse_artist_page)

@api.route('/artist/id/<artist_id>') 
def get_artist_by_id(artist_id):
    query = '''SELECT id, artist_surname, artist_firstname, artist_bio, artist_birthyear, artist_deathyear
               FROM artists 
               WHERE id = (%s)
               ORDER BY artist_surname'''

    artist_data = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (artist_id,))
        for row in cursor:
            info = {    'artist_id' : row[0],
                        'artist_surname':row[1],
                        'artist_firstname':row[2],
                        'artist_bio': row[3],
                        'artist_birthyear':row[4],
                        'artist_deathyear':row[5]}
            artist_data.append(info)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    #browse_artist_page = {'artist_list' : artist_list}
    return json.dumps(artist_data)

@api.route('/artists/q/<query_name>')
def browse_artist_query(query_name):
    query_name_search = "%" + query_name + "%"
    query = '''SELECT id, artist_firstname, artist_surname, artist_bio, artist_birthyear, artist_deathyear
                FROM artists
                WHERE LOWER(artist_surname) LIKE LOWER(%s)
                ORDER BY artist_surname LIMIT 100'''

    artist_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (query_name_search,))
        for row in cursor:
            current = { 'artist_id' : row[0],
                        'artist_surname':row[1],
                        'artist_firstname':row[2],
                        'artist_bio': row[3],
                        'artist_birthyear':row[4],
                        'artist_deathyear':row[5]}
            artist_list.append(current)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    browse_artist_page = {'artist_list' : artist_list}
    return json.dumps(browse_artist_page)

@api.route('/artwork/id/<artwork_id>')
def get_artwork_by_id(artwork_id):
    query = '''SELECT artworks.artwork, artworks.id, artworks.art_date, artworks.artist_id, artists.id, artists.artist_surname, artists.artist_firstname, artworks.material_id, materials.id, materials.medium, artworks.department_id, collections.id, collections.department_name, artworks.geographic_location_id, geographic_locations.id, geographic_locations.country_name, artworks.link_resource
        FROM artworks, artists, materials, collections, geographic_locations
        WHERE artworks.artist_id = artists.id
        AND artworks.geographic_location_id = geographic_locations.id
        AND artworks.material_id = materials.id
        AND artworks.department_id = collections.id
        AND artworks.id = (%s)
        ORDER BY artworks.artwork, artworks.id'''

    artwork_data = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (artwork_id,))
        for row in cursor:
            info = {'artwork':row[0],
                        'art_date':row[2],
                        'artist_surname': row[5],
                        'artist_firstname': row[6],
                        'medium':row[9],
                        'collection':row[12],
                        'country':row[15],
                        'link_resource':row[16]}
            artwork_data.append(info)
        cursor.close()
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    #artwork_data_page = {'artwork_data' : artwork_data}
    return json.dumps(artwork_data)

@api.route('/help')
def get_help():
    file = open('api-design.txt')
    lines = file.readlines()
    help_text = ''
    for line in lines:
        help_text += (line)
    return help_text