document.addEventListener("DOMContentLoaded", async (event) => {
	const bodyProductos = document.getElementById("body-productos");
	const bodyTotal = document.getElementById("body-total");
	var lista = localStorage.getItem("carrito");
	if (lista != "") {
		lista = JSON.parse(lista);
		const unic = lista.reduce(function (obj, name) {
			obj[name] = obj[name] ? ++obj[name] : 1;
			return obj;
		}, {});

		const keys = Object.keys(unic);
		const listOfProducts = Promise.all(
			keys.map(async (element, index) => {
				const result = await (
					await fetch(
						`http://localhost:8000/api/v1/Productos/productos/${element}`
					)
				).json();
				result["total"] = result["valor"] * unic[result.idProducto];
				return result;
			})
		);
		let total = 0;
		(await listOfProducts).forEach((result, index) => {
			total += result["valor"] * unic[keys[index]];
			bodyProductos.innerHTML =
				bodyProductos.innerHTML +
				`<tr><td>${result.idProducto}</td><td>${result.nombre}</td><td>$${
					result.valor
				}</td><td>${unic[keys[index]]}</td><td><a href="./verProducto.html?id=${
					result.idProducto
				}" class="font-weight-bold text-dark">Ver</a></td></tr>`;
		});

		bodyTotal.innerHTML = await `<tr><td>${total}</td><td>${Math.ceil(
			total * 0.19
		)}</td><td>${Math.ceil(
			total * 1.19
		)}</td><td><button type="button" id="pago" class="btn btn-success"style="font-family: cursive" >Pagar</button></td></tr>`;

		document.getElementById("pago").addEventListener("click", async (e) => {
			const usuario = Number(localStorage.getItem("usuario"));
			const venta = { usuario: usuario, estadoVenta: 1, totalVenta: total };
			const response = await (
				await fetch("http://localhost:8000/api/v1/Ventas/ventas/", {
					method: "POST",
					body: JSON.stringify(venta),
				})
			).json();

			keys.forEach(async (element) => {
				const detalleVenta = { venta: response.idVenta, producto: element };
				console.log(detalleVenta);
				const responseDetalle = await (
					await fetch("http://localhost:8000/api/v1/Ventas/detalleVentas/", {
						method: "POST",
						body: JSON.stringify(detalleVenta),
					})
				).json();
			});
			localStorage.setItem("carrito", "");
			window.location.reload();
		});
	}
});
