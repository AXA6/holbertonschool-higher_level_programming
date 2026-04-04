fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
	.then(Response => {
		return Response.json();

	})
	.then(data => {
		const hello = document.getElementById("hello");
		hello.textContent = data.hello;
	});
