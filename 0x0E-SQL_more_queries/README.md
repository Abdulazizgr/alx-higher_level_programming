
# SQL - More queries

This repository contains a collection of SQL scripts for various database management tasks. Each script is designed to perform specific actions on a MySQL server. Below is a summary of each script and its purpose:

## List of SQL Scripts:
- 0-privileges.sql: Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server (localhost).

- 1-create_user.sql: Creates the MySQL server user user_0d_1 with all privileges. The password for user_0d_1 is set to user_0d_1_pwd.

- 2-create_read_user.sql: Creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege only on hbtn_0d_2.

- 3-force_name.sql: Creates a table force_name with columns id (INT) and name (VARCHAR(256)), where name cannot be null.

- 4-never_empty.sql: Creates a table id_not_null with columns id (INT, default value 1) and name (VARCHAR(256)), ensuring id cannot be null.

- 5-unique_id.sql: Creates a table unique_id with columns id (INT, default value 1, unique) and name (VARCHAR(256)).

-  6-states.sql: Creates the database hbtn_0d_usa and the table states with columns id (INT, unique, auto-generated, primary key) and name (VARCHAR(256)).

- 7-cities.sql: Creates the table cities in the hbtn_0d_usa database with columns id (INT, unique, auto-generated, primary key), state_id (INT, foreign key referencing id in states table), and name (VARCHAR(256)).

-  8-cities_of_california_subquery.sql: Lists all cities of California found in the hbtn_0d_usa database using a subquery method.

-  9-cities_by_state_join.sql: Lists all cities contained in the hbtn_0d_usa database, displaying city details along with their respective states using a JOIN method.

-  10-genre_id_by_show.sql: Lists all shows contained in hbtn_0d_tvshows with at least one genre linked, displaying their titles along with their respective genre IDs.

-  11-genre_id_all_shows.sql: Lists all shows contained in hbtn_0d_tvshows along with their respective genre IDs. If a show doesn't have a genre, NULL is displayed.

- 12-no_genre.sql: Lists all shows contained in hbtn_0d_tvshows without a genre linked, displaying their titles along with their respective genre IDs.

- 13-count_shows_by_genre.sql: Lists all genres from hbtn_0d_tvshows along with the number of shows linked to each genre, sorted in descending order by the number of shows.

- 14-my_genres.sql: Lists all genres of the show "Dexter" from hbtn_0d_tvshows.

- 15-comedy_only.sql: Lists all Comedy shows in hbtn_0d_tvshows.

- 16-shows_by_genre.sql: Lists all shows and their linked genres from hbtn_0d_tvshows.

- 100-not_my_genres.sql: Lists all genres not linked to the show "Dexter" from hbtn_0d_tvshows.

- 101-not_a_comedy.sql: Lists all shows without the genre "Comedy" from hbtn_0d_tvshows.

- 102-rating_shows.sql: Lists all shows from hbtn_0d_tvshows_rate by their ratings.

- 103-rating_genres.sql: Lists all genres from hbtn_0d_tvshows_rate along with their ratings.

