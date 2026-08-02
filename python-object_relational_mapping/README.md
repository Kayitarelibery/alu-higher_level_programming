# python-object_relational_mapping

## Description

This project is part of the ALU Higher-Level Programming curriculum. It covers connecting Python to a MySQL database, first with the low-level MySQLdb module (raw SQL queries), then with the SQLAlchemy ORM (mapping Python classes to database tables).

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to SELECT rows from a MySQL table
- How to INSERT, UPDATE, and DELETE rows in a MySQL table
- What ORM means
- How to map a Python class to a MySQL table
- How to use SQLAlchemy to interact with a MySQL database
- How to prevent SQL injection with parameterized queries

## Requirements

- Ubuntu 20.04 LTS
- Python 3 (python3 interpreter)
- MySQLdb (mysqlclient) module
- SQLAlchemy module
- MySQL server running on localhost, port 3306
- Scripts must pass pycodestyle (version 2.x)
- All files must end with a new line
- The first line of all files must be exactly #!/usr/bin/python3
- All files must be executable
- README.md at the root of the project folder is mandatory

## Files

| File | Description |
| --- | --- |
| 0-select_states.py | Lists all states from hbtn_0e_0_usa using MySQLdb |
| 1-filter_states.py | Lists all states starting with N from hbtn_0e_0_usa using MySQLdb |
| 2-my_filter_states.py | Lists states matching a name argument (vulnerable to SQL injection) |
| 3-my_safe_filter_states.py | Lists states matching a name argument, safe from SQL injection |
| 4-cities_by_state.py | Lists all cities with their state name from hbtn_0e_4_usa |
| 5-filter_cities.py | Lists all cities of a given state, safe from SQL injection |
| model_state.py | Defines the State class and Base (SQLAlchemy declarative_base) |
| 6-model_state.py | Creates the states table in the database via SQLAlchemy |
| 7-model_state_fetch_all.py | Lists all State objects via SQLAlchemy |
| 8-model_state_fetch_first.py | Prints the first State object via SQLAlchemy |
| 9-model_state_filter_a.py | Lists all State objects containing the letter a |
| 10-model_state_my_get.py | Prints the id of a State matching a given name, safe from SQL injection |
| 11-model_state_insert.py | Adds a new State (Louisiana) to the database |
| 12-model_state_update_id_2.py | Updates the name of the State with id 2 |
| 13-model_state_delete_a.py | Deletes all State objects containing the letter a |
| model_city.py | Defines the City class, linked to states via a foreign key |
| 14-model_city_fetch_by_state.py | Lists all City objects joined with their State name |

## Usage

MySQLdb scripts:
```bash
./0-select_states.py <mysql_user> <mysql_pwd> <db_name>
./3-my_safe_filter_states.py <mysql_user> <mysql_pwd> <db_name> <state_name>
```

SQLAlchemy scripts:
```bash
./7-model_state_fetch_all.py <mysql_user> <mysql_pwd> <db_name>
./10-model_state_my_get.py <mysql_user> <mysql_pwd> <db_name> <state_name>
```

## Author

Libery
