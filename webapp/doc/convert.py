'''
convert.py for the olympics database CS257 assignment
authors: Cathy Duan

to get the source data: 
https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results?resource=download
'''

import csv

# Create a dictionary that maps athlete_id -> athlete_name
# and then save the results in athletes.csv
# collections = {}
# with open('MetObjects.csv') as original_data_file,\
#         open('collections.csv', 'w') as collections_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(collections_file)
#     heading_row = next(reader) # eat up and ignore the heading row of the data file
#     for row in reader:
#         department = row[4]
#         if department not in collections:
#             collection_id = len(collections) + 1
#             collections[department] = collection_id
#             writer.writerow([collection_id, department])


# # Create a dictionary that maps event_id -> sport_event
# # and then save the results in events.csv
# materials = {}
# with open('MetObjects.csv') as original_data_file,\
#         open('materials.csv', 'w') as materials_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(materials_file)
#     heading_row = next(reader) # eat up and ignore the heading row of the data file
#     for row in reader:
#         material_type = row[38]
#         medium = row[24]
#         if medium not in materials:
#             material_id = len(materials) + 1
#             materials[medium] = material_id
#             writer.writerow([material_id, material_type, medium])

# # Create a dictionary that maps team_NOC_id -> team
# # and then save the results in team_NOC.csv
# geographical_locations = {}
# with open('MetObjects.csv') as original_data_file,\
#         open('geographical_locations.csv', 'w') as geographical_location_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(geographical_location_file)
#     heading_row = next(reader) # eat up and ignore the heading row of the data file
#     for row in reader:
#         geographical_location = row[31]
#         if geographical_location not in geographical_locations:
#             geographical_location_id = len(geographical_locations) + 1
#             geographical_locations[geographical_location] = geographical_location_id
#             writer.writerow([geographical_location_id, geographical_location])

# # Create a dictionary that maps game_id -> year_value
# # and then save the results in games.csv
# geography_types = {}
# with open('MetObjects.csv') as original_data_file,\
#         open('geography_types.csv', 'w') as geography_type_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(geography_type_file)
#     heading_row = next(reader) # eat up and ignore the heading row of the data file
#     for row in reader:
#         geography_type = row[27]
#         if geography_type not in geography_types:
#             geography_type_id = len(geography_types) + 1
#             geography_types[geography_type] = geography_type_id
#             writer.writerow([geography_type_id, geography_type])

# Create a dictionary that maps game_id -> year_value
# and then save the results in games.csv
artists = {}
with open('MetObjects.csv') as original_data_file,\
        open('artist.csv', 'w') as artist_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(artist_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        if row[17] == "":
            surname = None
            first_name = None
        else:
            artist_name_list = row[17].split(",")
            if len(artist_name_list) == 1:
                first_name = None
            else:
                first_name= artist_name_list[1]
            surname = artist_name_list[0]

        artist_bio = row[15]
        birth_year = row[19]
        death_year = row[20]
        # if row[19] == "":
        #     birth_year == None
        # elif "|" in row[19]:
        #     birth_year_list = row[19].split("|")
        #     birth_year = birth_year_list[0]
        # elif "-" in row[19]:
        #     birth_year_list = row[19].split("-")
        #     if birth_year_list[0] == "":
        #         birth_year = birth_year_list[1]
        #     else: 
        #         birth_year= birth_year_list[0]
        # else:
        #     birth_year = row[19]
        # if row[20]== "":
        #     death_year == None
        # elif "|" in row[20]:
        #     death_year_list = row[20].split("|")
        #     death_year = death_year_list[0]
        # elif "-" in row[20]:
        #     death_year_list = row[20].split("-")
        #     if death_year_list[0] == "":
        #         death_year = death_year_list[1]
        #     else: 
        #         death_year= death_year_list[0]
        # else:
        #     death_year = row[20]

        if artist_bio not in artists:
            artist_id = len(artists) + 1
            artists[artist_bio] = artist_id
            writer.writerow([artist_id, surname, first_name, artist_bio, birth_year, death_year])

#For each row in the original athlete_events.csv file, build a row
#for our new event_results.csv table
# with open('MetObjects.csv') as original_data_file,\
#         open('linking_table.csv', 'w') as linking_table_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(linking_table_file)
#     heading_row = next(reader) # eat up and ignore the heading row of the data file
#     linking_table_id = 0
#     for row in reader:

#         artwork_name = row[6]
#         collection= row[4]
#         collection_id = collections[collection] # this is guaranteed to work by section (2)
#         material = row[24]
#         material_id = materials[material] 
#         geographical_location = row[31]
#         geographical_location_id = geographical_locations[geographical_location]
#         geography_type = row[27]
#         geography_types_id = geography_types[geography_type]
#         artist = row[15]
#         artist_id = artists[artist]
#         link_resource = row[40]
#         linking_table_id = linking_table_id + 1
#         writer.writerow([linking_table_id, artwork_name, collection_id, material_id, geographical_location_id, geography_type_id, artist_id, link_resource])


