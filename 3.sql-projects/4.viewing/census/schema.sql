CREATE TABLE IF NOT EXISTS "census" (
    "id" INTEGER,
    "district" TEXT NOT NULL,
    "locality" TEXT NOT NULL,
    "families" INTEGER NOT NULL,
    "households" INTEGER NOT NULL,
    "population" INTEGER NOT NULL,
    "male" INTEGER NOT NULL,
    "female" INTEGER NOT NULL,
    PRIMARY KEY("id")
);
