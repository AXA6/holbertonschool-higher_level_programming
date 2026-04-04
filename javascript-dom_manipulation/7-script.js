fetch("https://swapi-api.hbtn.io/api/films/?format=json")
	.then(Response => {
		return Response.json();

	})
	.then(data => {
		const list_movies = document.getElementById("list_movies");
		data.results.forEach(item => {
			const li = document.createElement('li');
			li.textContent = item.title;
			list_movies.appendChild(li);
		});
	});
