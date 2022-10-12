-- queries.sql for the olympic database assignment for cs257
-- authors: Cathy Duan

--
--List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation
--
SELECT team_NOCs.NOC
FROM team_NOCs
ORDER BY team_NOCS.NOC;

--
--List the names of all the athletes from Jamaica
--

SELECT athletes.athlete_name
FROM athletes, team_NOCs, event_results
WHERE team_NOCs.team = "Jamaica"
AND athletes.athlete_id = event_results.athlete_id
AND team_NOCs.team_NOC_id = event_results.team_NOC_id

--
--List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.
--
SELECT athletes.athlete_name, events.sport_event, games.year_value, event_results.medal
FROM athletes, games, event_results
WHERE athletes.athlete_name = "Greg Louganis"
AND athletes.id = event_results.athlete_id
AND events.id = event_results.events_id
AND games.id = event_results.games_id
AND event_results.medal != "NA" 
ORDER BY games.year_value


--
--List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
--

SELECT team_NOCs.NOC, COUNT(event_results.medal)
FROM team_NOCs, event_results
WHERE event_results.medal = "Gold"
AND team_NOCS.team_NOC_id = event_results.team_NOC_id
ORDER BY COUNT(event_results.medal) DESC