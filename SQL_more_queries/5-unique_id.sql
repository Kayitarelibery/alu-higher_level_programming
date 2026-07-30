-- Creates the table unique_id with a default and unique id value of 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
