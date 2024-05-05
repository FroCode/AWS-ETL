WITH RECURSIVE split_investors (no, company, investor, rest) AS (
  SELECT
    no,
    company,
    SPLIT_PART(investor, ',', 1) AS investor,
    CASE
      WHEN POSITION(',' IN investor) > 0 THEN SUBSTRING(investor, POSITION(',' IN investor) + 1)
      ELSE NULL
    END AS rest
  FROM dev.public.unicorn
  UNION ALL
  SELECT
    no,
    company,
    SPLIT_PART(rest, ',', 1),
    CASE
      WHEN POSITION(',' IN rest) > 0 THEN SUBSTRING(rest, POSITION(',' IN rest) + 1)
      ELSE NULL
    END
  FROM split_investors
  WHERE rest IS NOT NULL
)

SELECT LTRIM(investor), COUNT(DISTINCT company) AS investment_count
FROM split_investors
GROUP BY investor
ORDER BY investment_count DESC;

