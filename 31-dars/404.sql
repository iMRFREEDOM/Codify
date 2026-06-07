-- SELECT AVG(price) FROM books;
-- SELECT AVG(price) FROM books WHERE autor = 'A.Qodiriy';
-- SELECT AVG(price) FROM books WHERE janri = 'roman';
-- SELECT AVG(price) FROM books
-- WHERE autor = 'A.Qodiriy' AND janri = 'roman';
-- SELECT AVG(post_code) FROM city;
-- SELECT AVG(post_code) FROM city
-- WHERE country LIKE 'O`zbekiston';
-- SELECT SUM(price) FROM books;
-- SELECT SUM(price) FROM books WHERE autor = 'A.Qodiriy' AND janri = 'roman';
-- SELECT SUM(price) FROM books WHERE janri = 'roman';
-- SELECT * FROM city WHERE country  LIKE 'O`zbekiston' LIMIT 2;
-- SELECT * FROM city WHERE id > 4 LIMIT 2 OFFSET 1;
-- SELECT * FROM city WHERE postcode < 12345 LIMIT 5;
-- SELECT * FROM city WHERE country  = 'rossiya' LIMIT 1 OFFSET 1;
-- SELECT * FROM books WHERE janri = 'roman' LIMIT 3 OFFSET 1;
-- SELECT * FROM books WHERE autor = 'A.Qodiriy' LIMIT 6;
-- SELECT * FROM books ORDER BY price ASC LIMIT 5;
-- SELECT * FROM books ORDER BY price DESC LIMIT 5;
-- SELECT * FROM books ORDER BY price DESC LIMIT 7 OFFSET 3;
-- SELECT MIN(min_salary) FROM jobs;
-- SELECT MAX(max_salary) FROM jobs;
-- SELECT MIN(max_salary) FROM jobs;
-- SELECT MAX(min_salary) FROM jobs;
-- SELECT * FROM jobs ORDER BY max_salary DESC LIMIT 5;
-- SELECT * FROM countries WHERE region_id = 4 ORDER BY  country_name ASC;
-- SELECT *  FROM countries ORDER BY region_id ASC, country_name ASC;



