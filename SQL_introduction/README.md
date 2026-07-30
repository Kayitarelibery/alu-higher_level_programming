# SQL_introduction


This project introduces the basics of SQL and relational databases using MySQL.

## Description


This project covers fundamental SQL operations, including:

- Creating and deleting databases
- Creating tables
- Inserting, updating, and deleting records
- Querying data with `SELECT`, `WHERE`, `ORDER BY`, and `GROUP BY`
- Aggregate functions like `COUNT` and `AVG`

## Files


| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases on the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates the table `first_table` |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a new row into `first_table` |
| `8-count_89.sql` | Counts records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Creates `second_table` and inserts multiple rows |
| `10-top_score.sql` | Lists records of `second_table` ordered by score |
| `11-best_score.sql` | Lists records with a score >= 10 |
| `12-no_cheating.sql` | Updates Bob's score to 10 (by name only) |
| `13-change_class.sql` | Removes records with a score <= 5 |
| `14-average.sql` | Computes the average score |
| `15-groups.sql` | Groups records by score with counts |
| `16-no_link.sql` | Lists records with a name, ordered by score |

## Usage


Each script can be run against a MySQL server like this:

\`\`\`
cat script_name.sql | mysql -hlocalhost -uroot -p database_name
\`\`\`

## Author


Libery - ALU Software Engineering Program
