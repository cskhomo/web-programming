SELECT "districts"."name"
FROM "districts"
JOIN "expenditures" ON "districts"."id" = "district_id"
ORDER BY "pupils"
LIMIT 1; 