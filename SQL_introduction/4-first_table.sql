-- This script creates the table first_table in the current database
-- If the table already exists, the script will not fail
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
