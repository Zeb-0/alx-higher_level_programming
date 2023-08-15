-- dispaly max temp for each state
-- Ordered bt State name

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
