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

api = flask.Blueprint('api', __name__)

def get_connection():
    try:
        test = psycopg2.connect(database=config.database, user=config.user, password='')
        return test
    except Exception as e:
        print(e)
        exit()

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
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name
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
                        'material_type':row[11]}
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
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name
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
                        'material_type':row[11]}
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
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name
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
                        'material_type':row[11]}
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
    print(material_name)
    material_name_search = "%" + material_name + "%"
    query = '''SELECT artworks.id, artworks.artwork, artworks.art_date, artworks.material_id, artworks.artist_id, artworks.geographic_location_id, artworks.department_id, artists.id, artists.artist_firstname, artists.artist_surname, materials.id, materials.material_type,
                collections.id, collections.department_name, geographic_locations.id, geographic_locations.country_name
                FROM artworks, artists, materials, collections, geographic_locations
                WHERE artists.id = artworks.artist_id
                AND materials.id = artworks.material_id
                AND geographic_locations.id = artworks.geographic_location_id
                AND collections.id = artworks.department_id
                AND LOWER(materials.material_type) LIKE LOWER(%s)
                ORDER BY artworks.artwork, artworks.id'''

    current_browsing = []
    print("test")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (material_name_search,))
        for row in cursor:
            current = {'artwork':row[1],
                        'art_date':row[2],
                        'artist_firstname': row[8],
                        'artist_surname':row[9],
                        'material_type':row[11]}
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


@api.route('/mockup7') 
def get_artists():
    query = '''SELECT artist_surname, artist_firstname, artist_bio, artist_birthyear, artist_deathyear
               FROM artists 
               ORDER BY artist_surname'''

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
       
        connection.close()

    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(artist_list)


@api.route('/help')
def get_help():
    return