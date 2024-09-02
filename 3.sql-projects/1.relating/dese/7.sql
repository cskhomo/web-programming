SELECT "schools"."name"
FROM "schools"
JOIN "districts" ON "district_id" = "districts"."id"
WHERE "districts"."name" = 'Cambridge';