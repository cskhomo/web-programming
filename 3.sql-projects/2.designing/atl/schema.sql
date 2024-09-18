CREATE TABLE IF NOT EXISTS "passengers" (
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INTEGER NOT NULL
    	CHECK("age" > 0),
    PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "checkins" (
    "id" INTEGER,
    "passenger_id" INTEGER,
    "datetime" NUMERIC NOT NULL
    	DEFAULT CURRENT_TIMESTAMP,
    "flight_id" INTEGER,
    "destination" TEXT NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("flight_id")
    	REFERENCES "flights"("id")
    FOREIGN KEY("passenger_id")
    	REFERENCES "passengers"("id")
);


CREATE TABLE IF NOT EXISTS "airlines"(
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "A" INTEGER DEFAULT '0'
    	CHECK("A" IN ('0', '1')),
    "B" INTEGER DEFAULT '0'
    	CHECK("B" IN ('0', '1')),
    "C" INTEGER DEFAULT '0'
    	CHECK("C" IN ('0', '1')),
    "D" INTEGER DEFAULT '0'
    	CHECK("D" IN ('0', '1')),
    "E" INTEGER DEFAULT '0'
    	CHECK("E" IN ('0', '1')),
    "F" INTEGER DEFAULT '0'
    	CHECK("F" IN ('0', '1')),
    "T" INTEGER DEFAULT '0'
    	CHECK("T" IN ('0', '1')),
    PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "flights"(
    "id" INTEGER,
    "flight_number" INTEGER NOT NULL, 
    "airline_id" INTEGER,
    "departure" TEXT NOT NULL,
    "takeoff_time" NUMERIC NOT NULL
    	DEFAULT CURRENT_TIMESTAMP,
    "landing_time" NUMERIC NOT NULL
    	DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id")
    FOREIGN KEY("airline_id")
    	REFERENCES "airlines"("id")
);