-- list all shows in hbtn_0d_tvshows with atleast one inked genre
--	 Each record should display: tv_shows.title - tv_show_genres.genre_id
--	sort the Result in ASC order by: tv_shows.title & tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
