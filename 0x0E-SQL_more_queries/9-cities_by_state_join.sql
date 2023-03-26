-- lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name, cities.state_id, states.name 
FROM cities 
INNER JOIN state cities.state_id=state_id ORDER BY cities.id DESC;
