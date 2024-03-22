-- create a table `users` if it does not exit
-- atributes: id, email, name

CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255));
