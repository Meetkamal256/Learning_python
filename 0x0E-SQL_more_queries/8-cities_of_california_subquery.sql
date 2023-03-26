--lists all the cities of California that can be found in the database hbtn_0d_usa.
--he states table contains only one record where name = California
--Results must be sorted in ascending order by cities.id

SELECT id, name, state_id FROM cities WHERE state_id=5 ORDER BY id DESC;       