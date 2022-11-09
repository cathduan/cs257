# Hannah Moran
# CS 257
# access the source data file 'athlete_events.csv' through Kaggle

import csv

def main():

    with open('MetObjects.csv') as csvfile:
        met_objects_text = csv.reader(csvfile)
        next(met_objects_text)

        # instantiate all dictionaries
        linking_table_dict = {}
        collections_dict = {}
        materials_dict = {}
        geographic_locations_dict = {}
        artists_dict = {}

        # for each row in athlete_events csv
        for row in met_objects_text:   

            # check name and sex data; format data as a string to be compared
            c_data = row[1] + '|' + row[2]
            # if data is not already present in dictionary
            if c_data not in collections_dict:
                # add into dictionary under new unique key, len(dict)
                collections_dict[c_data] = str(len(collections_dict))
            
            # check age, height, weight, team, and year; format data as a string to be compared
            m_data = row[3] + '|' + row[4] + '|' + row[5] + '|' + row[6] + '|' + row[9]
            if m_data not in materials_dict:
                # add into dictionary under new unique key, len(dict)
                materials_dict[m_data] = str(len(materials_dict))
            
            # check season, year, city, and games; format data as a string to be compared
            g_data = row[10] + '|' + row[9] + '|' + row[11] + '|' + row[8]
            if g_data not in geographic_locations_dict:
                # add into dictionary under new unique key, len(dict)
                geographic_locations_dict[g_data] = str(len(geographic_locations_dict))

            # check sports and event; format data as a string to be compared
            a_data = row[12] + '|' + row[13]
            if a_data not in artists_dict:
                # add into dictionary under new unique key, len(dict)
                artists_dict[a_data] = str(len(artists_dict))

            # data is all data in row
            data = str(collections_dict[c_data]) + '|' + str(materials_dict[m_data]) + '|' + str(geographic_locations_dict[g_data]) + '|' + str(artists_dict[a_data])
            if data not in linking_table_dict:
                linking_table_dict[data] = str(len(linking_table_dict))
                    
        # open new athletes csv
        with open('collections.csv', 'a') as csvfile:
            athletes = csv.writer(csvfile)
            # each unique key in athletes will be read
            for key in collections_dict.keys():
                # split string keys back into list elements for csv layout
                data_list = key.split('|')
                # use insert built-in to format list into writeable elements
                data_list.insert(0, collections_dict[key])
                # finally transcribe formatted key information into csv row
                athletes.writerow(data_list)
        
        # repeat steps in "athletes.csv"
        with open('materials.csv', 'a') as csvfile:
            player_attributes = csv.writer(csvfile)
            for key in materials_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, materials_dict[key])
                player_attributes.writerow(data_list)

        # repeat steps in "athletes.csv" 
        with open('geographic_locations.csv', 'a') as csvfile:
            olympic_games = csv.writer(csvfile)
            for key in geographic_locations_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, geographic_locations_dict[key])
                olympic_games.writerow(data_list)
        
        # repeat steps in "athletes.csv"
        with open('artists.csv', 'a') as csvfile:
            olympic_events = csv.writer(csvfile)
            for key in artists_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, artists_dict[key])
                olympic_events.writerow(data_list)
        
        with open('linking_table.csv', 'a') as csvfile:
            linking_table = csv.writer(csvfile)
            for key in linking_table_dict.keys():
                data_list = key.split('|')
                data_list.insert(0, linking_table_dict[key])
                linking_table.writerow(data_list)

if __name__ == '__main__':
    main()