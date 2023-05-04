-- a script that prepares a mysql server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating new user named: hbnb_dev with all privileges on the db hbnb_dev_db
-- with password : hbnb_dev_pwd if it doesnt exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost;
FLUSH PRIVILEGES;
-- granting select privileges for user on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
