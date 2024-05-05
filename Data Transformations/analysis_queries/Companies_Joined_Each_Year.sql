SELECT EXTRACT(YEAR FROM "date_joined"::date) AS Year, COUNT(*) AS Company_Count
FROM dev.public.fintech
GROUP BY Year
ORDER BY Year;
