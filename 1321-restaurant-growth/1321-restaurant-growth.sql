# Write your MySQL query statement below
WITH daily_amount AS (
    SELECT
        visited_on,
        SUM(amount) AS daily_total
    FROM Customer
    GROUP BY visited_on
)
SELECT
    visited_on,
    SUM(daily_total) OVER (
        ORDER BY visited_on
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    ROUND(
        AVG(daily_total) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS average_amount
FROM daily_amount
LIMIT 18446744073709551615 OFFSET 6;