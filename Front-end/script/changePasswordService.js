document.getElementById("form1").addEventListener("submit", async (e) => {
	e.preventDefault();
	const response = await await fetch(
		"http://localhost:8000/api/v1/Auth/validateUser",
		{
			method: "POST",
			body: JSON.stringify({ email: document.getElementById("correo").value }),
		}
	);
	if (response.status == 200) {
		document.getElementById("form2").hidden = false;
	} else {
		$("#alertaNoOk")
			.fadeTo(2000, 500)
			.slideUp(500, () => {
				$("#alertaNoOk").slideUp(500);
			});
	}
});

document.getElementById("form2").addEventListener("submit", async (e) => {
	e.preventDefault();
	if (
		document.getElementById("contrasena").value ==
		document.getElementById("contrasena2").value
	) {
		const response = await await fetch(
			"http://localhost:8000/api/v1/Auth/changePassword",
			{
				method: "PUT",
				body: JSON.stringify({
					password: document.getElementById("contrasena").value,
					username: document.getElementById("correo").value,
				}),
			}
		);
		$("#alertaOk").fadeTo(2000, 500);
	} else {
		$("#alertaNoOkCon")
			.fadeTo(2000, 500)
			.slideUp(500, () => {
				$("#alertaNoOk").slideUp(500);
			});
	}
});
