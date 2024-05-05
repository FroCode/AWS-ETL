-- City with the Highest Number of Fintech Companies
SELECT City, COUNT(*) AS Company_Count
FROM dev.public.unicorn
WHERE City IS NOT NULL AND City != ''
GROUP BY City
ORDER BY Company_Count DESC
LIMIT 1;
