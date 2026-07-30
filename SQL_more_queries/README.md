# SQL_more_queries

This project goes further into SQL and MySQL: managing users and privileges, enforcing column constraints, and writing multi-table queries with JOINs and subqueries.

## Description

This project covers:

- Creating MySQL users and managing privileges
- Enforcing constraints: `NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`
- Writing subqueries
- Joining tables with `JOIN` and `LEFT JOIN`
- Grouping and counting results with `GROUP BY` and aggregate functions

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of users `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates user `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates database `hbtn_0d_2` and user `user_0d_2` with SELECT only |
| `3-force_name.sql` | Creates table `force_name` with a required `name` column |
| `4-never_empty.sql` | Creates table `id_not_null` with a default `id` value |
| `5-unique_id.sql` | Creates table `unique_id` with a unique, defaulted `id` |
| `6-states.sql` | Creates database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Creates table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists California cities using a subquery |
| `9-cities_by_state_join.sql` | Lists cities with their state name using a JOIN |
| `10-genre_id_by_show.sql` | Lists shows with at least one linked genre |
| `11-genre_id_all_shows.sql` | Lists all shows, with NULL if no genre |
| `12-no_genre.sql` | Lists shows without a linked genre |
| `13-count_shows_by_genre.sql` | Counts shows per genre |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their linked genres |

## Usage

Each script can be run against a MySQL server like this:

\`\`\`
cat script_name.sql | mysql -hlocalhost -uroot -p database_name
\`\`\`

## Author

Libery - ALU Software Engineering Program
