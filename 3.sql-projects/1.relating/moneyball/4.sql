SELECT "first_name", "last_name", "salary"
FROM "players"
JOIN "salaries" ON "players"."id" = "player_id"
AND "year" = '2001'
ORDER BY "salary", "first_name", "last_name", "player_id"
LIMIT 50;