CREATE DATABASE IF NOT EXISTS codification_test_db;
USE codification_test_db;

CREATE TABLE codification_test_table (
    some_text varchar(255) not null
);

insert into codification_test_table (some_text) values ('Hello, world!');
insert into codification_test_table (some_text) values ('Visca el Barça!');
insert into codification_test_table (some_text) values ('àèìòù & áéíóú & ñ');
