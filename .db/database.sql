DROP DATABASE IF EXISTS flask_login;
CREATE DATABASE flask_login;
USE flask_login;

CREATE TABLE login(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20),
    email VARCHAR(250),
    password VARCHAR(50)
);


INSERT INTO login (username, email, password)
VALUES  ("jcjohan", "jcjohan2707@gmail.com", "PASSWORD"),
        ("jlpaisano", "jlpaisano@gmail.com", "12345678");

SELECT * FROM login;
