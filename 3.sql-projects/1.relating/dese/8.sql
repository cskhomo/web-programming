SELECT "districts"."name", "expenditures"."pupils"
FROM  "districts"
JOIN "expenditures" ON "districts"."id" = "district_id";