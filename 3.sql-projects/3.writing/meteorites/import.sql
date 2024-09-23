.import --csv meteorites.csv  temp


UPDATE "temp"
SET "mass" = NULL
WHERE "mass" = '';

UPDATE "temp"
SET "year" = NULL
WHERE "year" = '';

UPDATE "temp"
SET "long" = NULL
WHERE "long" = '';

UPDATE "temp"
SET "lat" = NULL
WHERE "lat" = '';


DELETE FROM "temp"
WHERE "nametype" = 'Relict';


ALTER TABLE "temp"
DROP COLUMN "nametype";

ALTER TABLE "temp"
DROP COLUMN "id";


CREATE TABLE IF NOT EXISTS "meteorites"(
    "id" INTEGER,
    "name" TEXT NOT NULL UNIQUE,
    "class" TEXT NOT NULL,
    "mass" FLOAT,
    "discovery" TEXT NOT NULL
        CHECK("discovery" in ('Fell', 'Found')),
    "year" NUMERIC,
    "lat" FLOAT,
    "long" FLOAT,
    PRIMARY KEY("id")
);


INSERT INTO "meteorites" 
    ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", ROUND("mass", 2), "discovery", "year", ROUND("lat", 2), ROUND("long", 2)
FROM "temp"
ORDER BY "year", "name";


DROP TABLE "temp";