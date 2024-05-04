SELECT * FROM dev.public.unicorn;
SELECT * FROM dev.public.fintech;
ALTER TABLE dev.public.unicorn
-----------------------------------------------------------------------------
DROP COLUMN "company.1";

------------------------------------------------------------------------------
ALTER TABLE dev.public.unicorn RENAME COLUMN "valuation ($b)" TO valuation_inB;
ALTER TABLE dev.public.unicorn RENAME COLUMN "date joined" TO date_joined;
-------------------------------------------------------------------------------
-- Update DT Year
ALTER TABLE dev.public.unicorn ADD COLUMN year INTEGER;
UPDATE dev.public.unicorn
SET year = EXTRACT(YEAR FROM TO_DATE(date_joined, 'YYYY-MM-DD'));
ALTER TABLE dev.public.unicorn DROP COLUMN new_year;
ALTER TABLE dev.public.unicorn RENAME COLUMN new_year TO year;
-----------------------------------------------------------------------------------
