CREATE DATABASE recipes;

USE recipes;

CREATE TABLE users(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(45) NOT NULL,
last_name VARCHAR(45) NOT NULL,
email VARCHAR(45) NOT NULL,
user_password varchar(250) NOT NULL,
created_at DATETIME NOT NULL,
updated_at DATETIME NOT NULL 
);

INSERT INTO users(id,first_name,last_name,email,user_password,created_at,updated_at)
VALUES 
(1,'John', 'Ramirez','johnr@gmail.com','john123',SYSDATE(),SYSDATE() );


CREATE TABLE recipes(
recipe_id INT NOT NULL PRIMARY KEY auto_increment,
recipe_name VARCHAR(45) NOT NULL,
recipe_description VARCHAR(500) NOT NULL,
recipe_instructions VARCHAR(900) NOT NULL,
time_recipe VARCHAR(45) NOT NULL,
created_at DATETIME NOT NULL,
updated_at DATETIME NOT NULL 
);

INSERT INTO recipes(recipe_id,recipe_name,recipe_description,recipe_instructions,time_recipe,created_at,updated_at)
VALUES 
(1,'Tortica de pollo', 'La mejor torta de la abuela','Solo la abuela sabe prepararla preguntale a ella','Yes', SYSDATE(),SYSDATE() );

CREATE TABLE users_and_recipes(
thogether_id INT NOT NULL AUTO_INCREMENT
recipe_id INT NOT NULL, 
FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ON DELETE CASCADE,
id INT NOT NULL,
FOREIGN KEY (id) REFERENCES users(id) ON DELETE CASCADE);
