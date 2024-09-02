SELECT "name", ROUND(AVG("salary"), 2) AS "Average Salary"
FROM "teams"
JOIN "salaries" ON "teams"."id" = "team_id"
AND "salaries"."year" = '2001'
GROUP BY "name"
ORDER BY "Average Salary"
LIMIT 5;