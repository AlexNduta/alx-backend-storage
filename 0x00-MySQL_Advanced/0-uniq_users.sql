-- create a table `users` if it does not exit

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE, 
    name VARCHAR(255)
);
