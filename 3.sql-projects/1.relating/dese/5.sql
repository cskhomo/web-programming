SELECT "city", COUNT("name") AS "Schools"
FROM "schools"
WHERE "type" LIKE 'Public%'
GROUP BY "city"
HAVING "Schools" <= 3
ORDER BY "Schools" DESC, "city";
