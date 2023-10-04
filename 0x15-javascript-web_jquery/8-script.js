/**$(document).ready(function () {
	$.getJSON(
		"https://swapi-api.alx-tools.com/api/films/?format=json",
		function (data) {
			data.results.forEach(function (film) {
				$("li").text(film.title).appendTo("UL#list_movies")
				))}
		}
	}
*/
$(document).ready(function () {
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
		function (data) {
			data.results.forEach(function (film) {
				$("<li>").text(film.title).appendTo("UL#list_movies")
			})
		})
})

