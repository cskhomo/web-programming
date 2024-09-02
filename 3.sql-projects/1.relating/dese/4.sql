SELECT "city", COUNT("name") AS "Schools"
FROM "schools"
WHERE "type" LIKE 'public%'
GROUP BY "city"
ORDER BY "Schools" DESC, "city"
LIMIT 10;