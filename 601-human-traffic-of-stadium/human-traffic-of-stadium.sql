
WITH HighTraffic AS (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
QualifiedGroups AS (
    SELECT grp
    FROM HighTraffic
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT h.id, h.visit_date, h.people
FROM HighTraffic h
JOIN QualifiedGroups q
ON h.grp = q.grp
ORDER BY h.visit_date;
