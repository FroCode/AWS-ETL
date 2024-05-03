SELECT * FROM dev.public.fintech;
/* Change Column Names */

ALTER TABLE dev.public.fintech RENAME COLUMN "valuation ($b)" TO valuation_inB;
ALTER TABLE dev.public.fintech RENAME COLUMN "date joined" TO date_joined;
/* Check Data Types */

SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'fintech'
AND table_schema = 'public';

--Update Datatype value for "date_joined" column
ALTER TABLE dev.public.fintech ADD COLUMN new_date_column DATE;
UPDATE dev.public.fintech
SET new_date_column = TO_DATE(date_joined, 'YYYY-MM-DD');  -- Adjust the format string as necessary
-- Drop old column "date_joined" and update "new_date_column" to "date_joined"
ALTER TABLE dev.public.fintech DROP COLUMN date_joined;
ALTER TABLE dev.public.fintech RENAME COLUMN new_date_column TO date_joined;

--Update Datatype value for "year" column
ALTER TABLE dev.public.fintech ADD COLUMN new_year INTEGER;
UPDATE dev.public.fintech
SET new_year = EXTRACT(YEAR FROM TO_DATE(year, 'YYYY-MM-DD'));
ALTER TABLE dev.public.fintech DROP COLUMN year;
ALTER TABLE dev.public.fintech RENAME COLUMN new_year TO year;

-- Check Missing values City column
SELECT
    COUNT(*) AS total_records,
    COUNT(city) AS non_empty_city,
    COUNT(*) - COUNT(NULLIF(TRIM(city), '')) AS empty_or_whitespace_city
FROM dev.public.fintech;
-- Filling empty values with "Unknown"
UPDATE dev.public.fintech
SET city = 'Unknown'
WHERE city = '';
-- Delete Duplicates Rows
DELETE FROM dev.public.fintech
WHERE (city, company, date_joined) IN (
    SELECT city, company, date_joined
    FROM (
        SELECT city, company, date_joined,
               ROW_NUMBER() OVER (PARTITION BY city, company, date_joined ORDER BY date_joined) as row_num
        FROM dev.public.fintech
    ) t
    WHERE t.row_num > 1
);

