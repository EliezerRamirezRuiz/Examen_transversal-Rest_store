document.addEventListener("DOMContentLoaded", async (e) => {
	const response = await (
		await fetch("http://localhost:8000/api/v1/Productos/productos")
	).json();
	const container = document.getElementById("container");
	for (let i = 0; i < response.length; i += 3) {
		const row = document.createElement("div");
		row.className = "row gx-5 mb-5";
		for (let j = 0; j < 3; j++) {
			const divProducto = document.createElement("div");
			const item = response[i + j];
			if (item != null) {
				divProducto.className = "col-4";
				divProducto.innerHTML = `<div class="card mx-auto" style="width: 18rem; min-height: 
                650px; justify-content: space-between"><img src="../${
									item.imagen
								}" class="card-img-top" alt="..." /><div class="card-body" style="flex:0"><h5 class="card-title">${
					item.nombre
				}</h5><p class="card-text">${
					item.descripcion.length > 50
						? item.descripcion.substr(0, 50).trim() + "..."
						: item.descripcion
				}</p><div class="row text-center"><div class="col-6"><p>$${
					item.valor
				}</p></div><div class="col-6"><p>${
					item.stock
				} uni.</p></div></div><a href="verProducto.html?id=${
					item.idProducto
				}" class="btn btn-primary d-block mt-5">Ver Producto</a></div></div>`;
				row.appendChild(divProducto);
			}
		}
		container.appendChild(row);
	}
});
