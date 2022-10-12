'''
convert.py for the olympics database CS257 assignment
authors: Cathy Duan

to get the source data: 
https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results?resource=download
'''

import csv

# Create a dictionary that maps athlete_id -> athlete_name
# and then save the results in athletes.csv
athletes = {}
with open('athlete_events.csv') as original_data_file,\
        open('athletes.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name])


# Create a dictionary that maps event_id -> sport_event
# and then save the results in events.csv
events = {}
with open('athlete_events.csv') as original_data_file,\
        open('events.csv', 'w') as events_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(events_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        sport = row[12]
        sport_event = row[13]
        if sport_event not in events:
            event_id = len(events) + 1
            events[sport_event] = event_id
            writer.writerow([event_id, sport, sport_event])

# Create a dictionary that maps team_NOC_id -> team
# and then save the results in team_NOC.csv
team_NOCs = {}
with open('athlete_events.csv') as original_data_file,\
        open('team_NOC.csv', 'w') as team_NOC_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(team_NOC_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        team = row[6]
        NOC = row[7]
        if team not in team_NOCs:
            team_NOC_id = len(team_NOCs) + 1
            team_NOCs[team] = team_NOC_id
            writer.writerow([team_NOC_id, team, NOC])

# Create a dictionary that maps game_id -> year_value
# and then save the results in games.csv
games = {}
with open('athlete_events.csv') as original_data_file,\
        open('games.csv', 'w') as games_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(games_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        year_value = row[9]
        season = row[10]
        city = row[11]
        if year_value not in games:
            game_id = len(games) + 1
            games[year_value] = game_id
            writer.writerow([game_id, year_value, season, city])

#For each row in the original athlete_events.csv file, build a row
#for our new event_results.csv table
with open('athlete_events.csv') as original_data_file,\
        open('event_results.csv', 'w') as event_results_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(event_results_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        sport_event = row[13]
        event_id = events[sport_event] # this is guaranteed to work by section (2)
        team = row[6]
        team_NOC_id =team_NOCs[team] 
        year_value = row[9]
        game_id = games[year_value]
        medal = row[14]
        writer.writerow([athlete_id, event_id, team_NOC_id, game_id, medal])




