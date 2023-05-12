-- TEST script that prepares a MySQL server for the project
-- creates test database and test user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'Kamal256$';
 GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
 GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';