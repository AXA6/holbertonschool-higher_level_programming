fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
	.then(Response => {
		return Response.json();

	})
	.then(data => {
		const character = document.getElementById("character");
		character.textContent = data.name;
	});
