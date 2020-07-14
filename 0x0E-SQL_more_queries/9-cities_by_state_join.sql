-- enumerate all citys contained in the database
-- enumerate all citys contained in the database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
