-- enumerate all citys from california in the database
-- enumerate all citys from california in the database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
