-- a script that prepares a MySQL server for the project
-- setup database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creates new user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- grant basic usage
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';

-- grant select privelges on performance shema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- grant all privileges on hbnbh_test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
