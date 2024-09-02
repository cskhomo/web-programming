SELECT "name"
FROM "schools"
JOIN "graduation_rates" ON "schools"."id" = "school_id"
WHERE "graduated" = '100';