--
-- PostgresSQL olympic database dump
--

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: athletes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE athletes(		
	id integer,
	athlete_name text
);

--
-- Name: events; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE events(
	id integer,
	sport text,
	sport_event text
);

--
-- Name: team_NOC; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE team_NOC(
	id integer,
	team text,
	NOC text
);

--
-- Name: games; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE games(
	id integer,
	year_value integer,
	season text,
	city text
);


--
-- Name: event_results; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE event_results(
	athlete_id integer,
	event_id integer,
	team_NOC_id integer,
	game_id integer,
	medal text
);


--
-- PostgreSQL olympic database dump complete
--
