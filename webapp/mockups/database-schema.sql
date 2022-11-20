---
--- PostgreSQL MET Database Dump
--- Authors: Cathy Duan and Hannah Moran
---

--
-- Name: collections; Type: TABLE; 
--

CREATE TABLE collections(
    id integer,
    department_name text
);

--
-- Name: materials; Type: TABLE; 
--

CREATE TABLE materials(
    id integer,
    material_type text
);

--
-- Name: geographic_locations; Type: TABLE; 
--

CREATE TABLE geographic_locations(
    id integer,
    country_name text
);

--
-- Name: artists; Type: TABLE; 
--

CREATE TABLE artists(
    id integer,
    artist_surname text,
    artist_firstname text,
    artist_bio text,
    artist_birthyear text,
    artist_deathyear text
);

--
-- Name: linking_table; Type: TABLE; 
--
CREATE TABLE artworks(		
	id integer,
    art_date text,
	artwork text,
    department_id integer,
    material_id integer,
    geographic_location_id integer,
    artist_id integer,
    link_resource text
);

--
-- PostgreSQL MET Database Dump Complete
--
