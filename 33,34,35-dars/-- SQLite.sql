SELECT c.country_name, region_name
FROM countries c INNER JOIN Regions r
ON c.region_id = r.region_id;