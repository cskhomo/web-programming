SELECT "name", "per_pupil_expenditure", "graduated"
FROM "schools" 
JOIN "graduation_rates" on "schools"."id" = "school_id"
JOIN "expenditures" ON "schools"."district_id" = "expenditures"."district_id"
ORDER BY "per_pupil_expenditure" DESC, "name";