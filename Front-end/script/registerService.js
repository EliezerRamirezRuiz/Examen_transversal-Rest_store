document.addEventListener("DOMContentLoaded", (e) => {
	const region = document.getElementById("region");
	const regiones = fetch("https://apis.digital.gob.cl/dpa/regiones")
		.then((data) => data.json())
		.then((result) =>
			result.forEach((item) => {
				region.appendChild(new Option(item.nombre, item.codigo));
			})
		);
});

document.getElementById("region").addEventListener("change", (e) => {
	const region = document.getElementById("region");
	const provincia = document.getElementById("provincia");
	provincia.innerHTML = "";
	provincia.appendChild(new Option("-- Seleccione una provincia --", 0));
	const provincias = fetch(
		`https://apis.digital.gob.cl/dpa/regiones/${region.value}/provincias`
	)
		.then((data) => data.json())
		.then((result) =>
			result.forEach((item) => {
				provincia.appendChild(new Option(item.nombre, item.codigo));
			})
		);
});

document.getElementById("provincia").addEventListener("change", (e) => {
	const region = document.getElementById("region");
	const provincia = document.getElementById("provincia");
	const comuna = document.getElementById("comuna");
	comuna.innerHTML = "";
	comuna.appendChild(new Option("-- Seleccione una comuna --", 0));
	fetch(
		`https://apis.digital.gob.cl/dpa/regiones/${region.value}/provincias/${provincia.value}/comunas`
	)
		.then((data) => data.json())
		.then((result) =>
			result.forEach((item) => {
				comuna.appendChild(new Option(item.nombre, item.codigo));
			})
		);
});

const validatePassword = () => {
	const password = document.getElementById("password").value;
	const password2 = document.getElementById("password2").value;
	return password === password2;
};

const form = document.getElementById("form");
form.addEventListener("submit", (e) => {
	e.preventDefault();
	if (validatePassword()) {
		const object = {
			nombre: document.getElementById("nombre").value,
			apellidos: document.getElementById("apellido").value,
			correo: document.getElementById("email").value,
			direccion: document.getElementById("direccion").value,
			telefono: document.getElementById("telefono").value,
			comuna: document.getElementById("comuna").value,
			provincia: document.getElementById("provincia").value,
			region: document.getElementById("region").value,
			rut: document.getElementById("rut").value,
			isSuscrito: document.getElementById("isSuscrito").checked,
			password: document.getElementById("password").value,
		};
		fetch(`http://localhost:8000/api/v1/Auth/signUp`, {
			method: "POST",
			body: JSON.stringify(object),
		});
	}
});
