-- lists all records of the table second_table
INSERT INTO second_table (score, name)
VALUES
(18, 'Aria'),
(12, 'Aria');

SELECT score, name FROM second_table
ORDER BY score DESC;
