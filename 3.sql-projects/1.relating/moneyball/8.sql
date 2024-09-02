SELECT "salary"
FROM "salaries"
JOIN "performances" USING("player_id")
WHERE "salaries"."year" = '2001' 
AND "HR" = (
    SELECT MAX("HR")
    FROM "performances"
);