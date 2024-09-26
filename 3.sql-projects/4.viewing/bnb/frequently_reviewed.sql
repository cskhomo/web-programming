CREATE VIEW "frequently_reviewed" AS
    SELECT "listings"."id", "property_type", "host_name", COUNT("reviews"."id") AS "reviews"
    FROM "listings"
    JOIN "reviews"
    ON "listings"."id" = "listing_id"
    GROUP BY "listing_id"
    ORDER BY "reviews" DESC, "property_type" ASC, "host_name" ASC
    LIMIT 100;
