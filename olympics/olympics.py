'''
olympics.py 
10/22/2022
Author: Cathy Duan

DB-driven command-line application assignment 
CS 257: Software Design 
Carleton College

Note: Adapted from Jeff Ondich's psycopg2-sample.py code.
'''

import sys
import psycopg2
import config


def get_connection():
    try:
        return psycopg2.connect(database=config.database, user=config.user)
    
    except Exception as e:
        print(e, file=sys.stderr)
        exit()


def get_athletes(NOC):
    ''' Returns a list of the full names of all the athletes
        in the database who have competed for a user-inputted NOC'''
    athletes = []
    try:
        # Create a "cursor"
        connection = get_connection()
        cursor = connection.cursor()

        # Execute the query
        query = ''' SELECT DISTINCT athletes.athlete_name
                    FROM athletes, team_NOC, event_results
                    WHERE team_NOC.NOC = ''' + "'" + NOC + "'" '''
                    AND athletes.id = event_results.athlete_id
                    AND team_NOC.id = event_results.team_NOC_id; '''
        cursor.execute(query, (NOC,))

        # Iterate over the query results to produce the list of athlete names.
        for row in cursor:
            full_name = row[0]
            athletes.append(f'{full_name}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_NOCs_medal_count(medal_type):
    ''' Returns a list of all NOCs and the count of how many gold medals each NOC has won.'''
    NOCS = []
    medal_count = []
    try:
        query = ''' SELECT COUNT(event_results.medal), team_NOC.NOC
                    FROM team_NOC, event_results
                    WHERE event_results.medal = ''' + "'" + medal_type + "'"  '''
                    AND team_NOC.id = event_results.team_NOC_id
                    GROUP BY team_NOC.NOC
                    ORDER BY COUNT(event_results.medal) DESC; '''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, ())
        for row in cursor:
            count = row[0]
            NOC = row[1]
            medal_count.append(count)
            NOCS.append(f'{NOC}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return NOCS, medal_count

def get_events_for_sport(sport, NOC):
    ''' Returns a list of all the sport events that the given <sport> encompasses for a given <NOC> '''
    sport_events = []
    try:
        query = ''' SELECT DISTINCT events.sport_event, team_NOC.NOC
                    FROM events, team_NOC, event_results
                    WHERE events.sport = ''' + "'" + sport + "'" '''
                    AND team_NOC.NOC = ''' + "'" + NOC + "'" '''
                    AND team_NOC.id = event_results.team_NOC_id; '''
        
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (sport, NOC,))

        for row in cursor:
            sport_event = row[0]
            sport_events.append(f'{sport_event}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return sport_events


# Prints out a NOC's list of athletes
def athlete_print(athletes):
    for athlete in athletes: 
        print (athlete)

# Prints out each NOC's medal count, the medal type depends on input
def NOC_medal_print(NOCs, medal_count):
    for i in range(len(NOCs)):
        print(NOCs[i] + ", " + str(medal_count[i]) + " " + sys.argv[2] + " medals")

# Prints out a NOC's list of sport events for a specific sport
def event_print(sport_events):
    for event in sport_events:
        print(event)

# Opens, reads, and prints the usage statement
def usage_statement_print():
    file = open("usage.txt")
    print(file.read())


def main():
    user_input = sys.argv[1:] # Ignores olympics.py in the command line
    length = len(user_input)

    
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        usage_statement_print()

    elif length == 2: 
        if sys.argv[1] == "athletes" or sys.argv[1] == "-a":
            athletes = get_athletes(sys.argv[2])
            athlete_print(athletes)
        elif sys.argv[1] == "NOCs" or sys.argv[1] == "-n":
            NOCs, medal_count = get_NOCs_medal_count(sys.argv[2])
            NOC_medal_print(NOCs, medal_count)
        else: 
            print("Please refer to the usage statement below")
            usage_statement_print()
    elif sys.argv[1] == "events" or sys.argv[1] == "-e": 
        if length == 3: 
            sport_events = get_events_for_sport(sys.argv[2], sys.argv[3])
            event_print(sport_events)
        elif length > 3: # if the sport is multiple words
            sport = "" #sys.argv[2:-1] is a list and needs to be a joined as a string
            for i in (2, length-1):
                if i == 2:
                    sport = sys.argv[i]
                else: 
                    sport = sport +  " " + sys.argv[i]
            sport_events = get_events_for_sport(sport, sys.argv[-1])
            event_print(sport_events)
        else: 
            print("Please refer to the usage statement below")
            usage_statement_print()
    else: 
        print("Please refer to the usage statement below")
        usage_statement_print()

if __name__ == '__main__':
    main()
