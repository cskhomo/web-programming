SELECT "first_name", "last_name", 
        "salary", "HR", "salaries"."year"
FROM "players"
JOIN "salaries" ON "players"."id" = "salaries"."player_id"
JOIN "performances" USING("player_id", "year")
ORDER BY "players"."id" ASC, "salaries"."year" DESC,
        "performances"."HR" DESC, "salaries"."salary" DESC;