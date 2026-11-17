
WITH FirstExam AS (
    SELECT
        student_id,
        subject,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date ASC
        ) AS rn
    FROM Scores
),

LatestExam AS (
    SELECT
        student_id,
        subject,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date DESC
        ) AS rn
    FROM Scores
)

SELECT
    f.student_id,
    f.subject,
    f.score AS first_score,
    l.score AS latest_score
FROM FirstExam f
JOIN LatestExam l
    ON f.student_id = l.student_id
    AND f.subject = l.subject
WHERE
    f.rn = 1
    AND l.rn = 1
    AND l.score > f.score
ORDER BY
    f.student_id,
    f.subject;
