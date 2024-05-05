SELECT Country, SUM(CAST(valuation_inb AS NUMERIC)) AS Total_Valuation
FROM dev.public.unicorn
GROUP BY Country
ORDER BY Total_Valuation DESC;
