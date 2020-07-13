-- list the number of records with the same score in a table
-- list the number of records with the same score in a table
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY number DESC;
