document.addEventListener("DOMContentLoaded", async (e) => {
	const urlParams = new URLSearchParams(window.location.search);
	const idProducto = urlParams.get("id");
	const response = await (
		await fetch(
			`http://localhost:8000/api/v1/Productos/productos/${idProducto}`
		)
	).json();
	const container = document.getElementById("detalleProduto");
	container.innerHTML = `<div class="row"><div class="d-flex justify-content-center col-lg-6"><img src="../${response.imagen}"alt=" "class="img-fluid"/></div><div class="col-lg-6 d-flex"style="flex-direction: column; justify-content: space-evenly"><h1 class="page-header">${response.nombre}</h1><ul class="list-inline" style="list-style: none"><li><p>$${response.valor}</p></li><li><p>Stock: ${response.stock} Und.</p></li><li><p>${response.descripcion}</p></li></ul><a href="./producto.html" class="btn btn-block"style="background-color: rgb(133, 185, 11); color: #fff"type="button" id="button">Agregar carrito</a></div></div>`;

	document.getElementById("button").addEventListener("click", (e) => {
		if (
			localStorage.getItem("carrito") == null ||
			localStorage.getItem("carrito") == ""
		) {
			localStorage.setItem(
				"carrito",
				JSON.stringify([new URLSearchParams(window.location.search).get("id")])
			);
		} else {
			const localDB = JSON.parse(localStorage.getItem("carrito"));
			localDB.push(new URLSearchParams(window.location.search).get("id"));
			localStorage.setItem("carrito", JSON.stringify(localDB));
		}
	});
});
