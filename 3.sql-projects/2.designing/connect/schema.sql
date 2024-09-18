CREATE TABLE IF NOT EXISTS "users"(
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "passhash" TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "school"(
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INTEGER NOT NULL, 
    PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "companies"(
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "industry" TEXT NOT NULL,    
    "location" TEXT NOT NULL,
    PRIMARY KEY("id")
);


CREATE TABLE IF NOT EXISTS "connections"(
    "user_x_id" INTEGER,
    "user_y_id" INTEGER,
    FOREIGN KEY("user_x_id")
    	REFERENCES "users"("id"),
    FOREIGN KEY("user_y_id")
    	REFERENCES "users"("id")
);


CREATE TABLE IF NOT EXISTS "students"(
    "user_id" INTEGER,
    "school_id" INTEGER,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC,
    "degree" TEXT,
    FOREIGN KEY("user_id")
    	REFERENCES "users"("id"),
    FOREIGN KEY("school_id")
    	REFERENCES "schools"("id")
);


CREATE TABLE IF NOT EXISTS "employees"(
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start_date" NUMERIC NOT NULL,
    "end_date" NUMERIC,
    "title" TEXT NOT NULL,
    FOREIGN KEY("user_id")
    	REFERENCES "users"("id"),
    FOREIGN KEY("company_id")
    	REFERENCES "companies"("id")
);