-- a script that prepares a MySQL server for the project
-- setup database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creates new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant basic usage
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- grant select privelges on performance shema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- grant all privileges on hbnbh_dev
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
