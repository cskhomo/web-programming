SELECT DISTINCT("name")
FROM "teams"
JOIN "performances" ON "teams"."id" = "team_id"
JOIN "players" ON "players"."id" = "player_id"
WHERE "first_name" = 'Satchel'
AND "last_name" = 'Paige';