-- create user table 
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255) ,
    country ENUM ('US', 'CO','TN') DEFAULT 'US' NOT NULL);
