-- queries.sql for the olympic database assignment for cs257
-- authors: Cathy Duan

--
--List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation
--
SELECT DISTINCT team_NOC.NOC
FROM team_NOC
ORDER BY team_NOC.NOC;

--
--List the names of all the athletes from Jamaica
--

SELECT DISTINCT athletes.athlete_name
FROM athletes, team_NOC, event_results
WHERE team_NOC.team = 'Jamaica'
AND athletes.id = event_results.athlete_id
AND team_NOC.id = event_results.team_NOC_id;

--
--List all the medals won by Gregory Efthimios "Greg" Louganis, sorted by year. Include whatever fields in this output that you think appropriate.
--
SELECT athletes.athlete_name, events.sport_event, games.year_value, event_results.medal
FROM athletes, games, events, event_results
WHERE athletes.athlete_name = 'Gregory Efthimios "Greg" Louganis'
AND athletes.id = event_results.athlete_id
AND events.id = event_results.event_id
AND games.id = event_results.game_id
AND event_results.medal != 'NA'
ORDER BY games.year_value;


--
--List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
--

SELECT COUNT(event_results.medal), team_NOC.NOC
FROM team_NOC, event_results
WHERE event_results.medal = 'Gold'
AND team_NOC.id = event_results.team_NOC_id
GROUP BY team_NOC.NOC
ORDER BY COUNT(event_results.medal) DESC;
