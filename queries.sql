SELECT
    title,
    avg_rating
FROM
    MOVIES
ORDER BY
    avg_rating DESC
LIMIT 1;

---------------------------------------------------------------------

SELECT
    genre,
    AVG(avg_rating) AS average_genre_rating
FROM
    MOVIES
WHERE
    genre IS NOT NULL
GROUP BY
    genre
ORDER BY
    average_genre_rating DESC
LIMIT 5;

---------------------------------------------------------------------

SELECT
    director,
    COUNT(movie_id) AS movie_count
FROM
    MOVIES
WHERE
    director IS NOT NULL
GROUP BY
    director
ORDER BY
    movie_count DESC
LIMIT 1;

---------------------------------------------------------------------

SELECT
    release_year,
    AVG(avg_rating) AS average_rating_for_year
FROM
    MOVIES
WHERE
    release_year > 0
GROUP BY
    release_year
ORDER BY
    release_year DESC;