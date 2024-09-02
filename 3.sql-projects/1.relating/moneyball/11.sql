SELECT "first_name", "last_name", "salary"/"H" AS "dollars per hit"
FROM "players"
JOIN "salaries" ON "players"."id" = "salaries"."player_id"
AND "salaries"."year" = '2001'
JOIN "performances" USING("player_id", "year")
WHERE "H" > 0
ORDER BY "dollars per hit", "first_name", "last_name" 
LIMIT 10;