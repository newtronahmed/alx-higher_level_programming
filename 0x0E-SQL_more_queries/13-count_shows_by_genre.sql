-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Don’t display a genre that doesn’t have any shows linked
SELECT tv_genres.name, count(*) as number_of_shows FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id ORDER BY number_of_shows DESCshow_id ;
