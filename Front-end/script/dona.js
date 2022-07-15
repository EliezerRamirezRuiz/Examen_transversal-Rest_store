document.getElementById("form").addEventListener("submit", async (e) => {
	await fetch("http://localhost:8000/api/v1/Usuarios/usuarios/suscrito", {
		method: "PUT",
		body: { email: document.getElementById("email").value, isSuscrito: 1 },
	});
});
