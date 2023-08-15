-- list all records in `second_table`
-- don't list rows without `name` value
-- list records be descending order
-- Result should display score and the name

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
