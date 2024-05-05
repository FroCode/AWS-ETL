SELECT Industry, AVG(CAST(valuation_inbAS NUMERIC)) AS Average_Valuation
FROM dev.public.fintech
GROUP BY Industry
ORDER BY Average_Valuation DESC;
