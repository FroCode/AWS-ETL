SELECT Country, Industry, COUNT(*) AS Number_of_Companies
FROM dev.public.fintech
GROUP BY Country, Industry
ORDER BY Country, Number_of_Companies DESC;
