SELECT * FROM (  
    SELECT "first_name", "last_name"
    FROM "players"
    JOIN "salaries" ON "players"."id" = "salaries"."player_id"
    AND "salaries"."year" = '2001'
    JOIN "performances" USING("player_id", "year")
    WHERE "H" > 0
    ORDER BY "salary"/"H"
    LIMIT 10
)

INTERSECT

SELECT * FROM (
    SELECT "first_name", "last_name"
    FROM "players"
    JOIN "salaries" ON "players"."id" = "salaries"."player_id"
    AND "salaries"."year" = '2001'
    JOIN "performances" USING("player_id", "year")
    WHERE "RBI" > 0
    ORDER BY "salary"/"RBI" 
    LIMIT 10
)

ORDER BY "last_name";
