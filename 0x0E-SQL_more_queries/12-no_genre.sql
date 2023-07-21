-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_shows_genres ON tv_shows_genres.show_id = tv_shows.id WHERE tv_shows_genres.genre_id IS NULL ORDER BY
tv_shows.title ASC, tv_shows_genres.genre_id ASC;
