DROP TABLE IF EXISTS summary;

CREATE TABLE summary AS
SELECT
    year AS publication_year,
    COUNT(*) AS book_count,
    ROUND(AVG(
        CASE
            WHEN price LIKE '€%' THEN CAST(SUBSTR(price, 2) AS REAL) * 1.2
            ELSE CAST(SUBSTR(price, 2) AS REAL)
        END
    ), 2) AS average_price
FROM books
GROUP BY year
ORDER BY year;