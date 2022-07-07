-- SELECT first_name, last_name FROM users WHERE id = 2 OR id < 4;
-- to select more than 1 table head or attribute, separate by commas
-- SELECT * FROM users WHERE first_name LIKE "%e";
-- SELECT last_name FROM users WHERE first_name in ('Kobe'); -- this is how you make a list, separate by commas
-- LIKE "k%" means starts with k, "%e" means ends with e, first_name <> "K%" means first names that start with anything but K
-- SELECT * FROM users ORDER BY birthday DESC; -- DESC is descending order, ASC is accending order
-- SELECT * FROM users WHERE first_name LIKE "%e"ORDER BY birthday DESC; -- does both of the above
-- SELECT * FROM users ORDER BY first_name; -- this orders them aphabetically, default is ASC
-- SELECT * FROM users LIMIT 3; -- this gets the first 3 
-- SELECT * FROM users LIMIT 3 OFFSET 2; -- this returns the 3-5th index
-- or do offset like this 
-- SELECT * FROM users LIMIT 2,3; -- first num is OFFSET, second is LIMIT
-- SELECT first_name FROM users WHERE num BETWEEN 1960 AND 1990; -- this doesnt work because the values dont work, but between is useful
-- SELECT birthday FROM users;

-- Template for insterting a value into the database
-- INSERT INTO table_name (column_name1, column_name2) 
-- VALUES('column1_value', 'column2_value');
-- INSERT INTO users(first_name, last_name, handle, birthday, created_at, updated_at) VALUES('Sam', 'Kniffin', 'sammyk', '2002-02-12', now(), now()); -- this runs
-- you do not have to put the values in the right order ^, can do (last_name, birthday, first_name, updated_at, created_at) and will be correct
-- you dont have to include id because id is set to Auto Increment, and created_at and updated_at arent necesary unless you want to add them (that goes for all )
-- if you insert it more than once, it will be inserted every time
-- select * from users

-- Template for updatung values in the database
-- UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)
-- or could do UPDATE 'schema_name'.'table_name' SET...
-- update users set first_name = 'Samuel', handle = 'sammyk123', updated_at = now() where id = 6; -- this runs

-- Template for deleting values in the database
-- DELETE FROM table_name WHERE condition(s)
-- could do DELETE FROM 'schema_name'.'table_name' WHERE...
-- delete from users where id > 7; -- this runs
-- be careful, if a condition isnt added the ENTIRE TABLE will be deleted. 
-- if you get an error about permission when deleting, use: SET SQL_SAFE_UPDATES = 0;

