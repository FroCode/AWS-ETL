-- Common Types of Industries Within Fintech with Most Investments
SELECT Industry, COUNT(*) AS Number_of_Companies
FROM dev.public.fintech
GROUP BY Industry
ORDER BY Number_of_Companies DESC;
