SELECT "name", "per_pupil_expenditure"
FROM "districts"
JOIN "expenditures" ON "districts"."id" = "district_id"
WHERE "type" LIKE 'public%'
ORDER BY "per_pupil_expenditure" DESC
LIMIT 10;