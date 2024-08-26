SELECT "english_title" AS "title", "artist", "entropy", "contrast"
FROM "views"
WHERE "print_number" BETWEEN '1' AND '5'
ORDER BY "entropy"; 