SELECT EXTRACT(YEAR FROM "date_joined"::date) AS Year, COUNT(*) AS Company_Count
FROM dev.public.unicorn
GROUP BY date_joined
ORDER BY date_joined;
