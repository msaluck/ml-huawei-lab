# Create a database and data table.
# Create a database.
create database money;
# Create a data table.
# CREATE TABLE user(
username varchar(30) PRIMARY KEY,
pwd VARCHAR(100) NOT NULL,
start_time DATETIME NOT NULL,
end_time DATETIME NOT NULL,
balance FLOAT NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
# Insert data.
INSERT INTO user (username, pwd, start_time, end_time, balance)
VALUES ('admin','123456','2019.04.23', '2019.04.23',100.0);
INSERT INTO user (username, pwd, start_time, end_time, balance)
VALUES ('root','admin','2019.01.01', '2019.02.02',100.0); 


