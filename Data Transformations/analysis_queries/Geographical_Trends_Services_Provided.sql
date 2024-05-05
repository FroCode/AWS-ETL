SELECT Country, Industry, COUNT(*) AS Number_of_Companies
FROM dev.public.unicorn
GROUP BY Country, Industry
ORDER BY Number_of_Companies DESC;
