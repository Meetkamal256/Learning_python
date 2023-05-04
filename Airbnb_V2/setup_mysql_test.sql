-- a script that prepares a mysql server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a user hbnb_test with all privileges on database hbnb_test_db
-- with password: hbnb_test_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting select privileges for the user hbnb_test on db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- granting all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
