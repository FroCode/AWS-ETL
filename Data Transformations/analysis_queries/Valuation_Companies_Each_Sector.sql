SELECT Industry, AVG(CAST(valuation_inb AS NUMERIC)) AS Average_Valuation
FROM dev.public.unicorn
GROUP BY Industry
ORDER BY Average_Valuation DESC;
