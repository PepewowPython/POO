#@author:Jeremy Chica Tapasco
#@Fecha: 6-10-2026
#@Descripción: Manejo de Diccionarios

#primera forma de recorrer diccionarios

prod = dict()

prod['id_product'] = 15
prod['nom_product']='computador asus'
prod['precio']=2000000
prod['descripcion']='Asus vivabook Core 15 9na generación, ram 4gb,ssd IT'
prod['cant_stock']=10

prod2 = {
    'id_product': 6,
    'nom_product': 'Computador Dell',
    'precio': 2100000,
    'descripcion': 'Computador Optiplex Core i5 5a Generación, 32 RAM, HDD 512 GB, color gris',
    'cant_stock': 20
}
productos = [prod, prod2]

# generar reporte
print(f"""
    id_product: {prod['id_product']}
    nombre del producto: {prod['nom_product']}
    precio del producto: {prod['precio']}
    descripcion del producto: {prod['descripcion']}
    cantidad en stock: {prod['cant_stock']}
""")

print(f"""
    id_product: {prod2['id_product']}
    nombre del producto: {prod2['nom_product']}
    precio del producto: {prod2['precio']}
    descripcion del producto: {prod2['descripcion']}
    cantidad en stock: {prod2['cant_stock']}
""")

# imprimir una lista de productos
print("Listado de productos")
for p in productos:
    print(f"""
    id_product: {p['id_product']}
    nombre del producto: {p['nom_product']}
    precio del producto: {p['precio']}
    descripcion del producto: {p['descripcion']}
    cantidad en stock: {p['cant_stock']}
""")

# mostrar la cantidad de dinero invertido en el inventario
# mostrar la cantidad total de stock de los productos
# mostrar el producto más costoso
# mostrar el promedio de precio de los productos
total_inventario = 0
stock_total = 0
sumatoria_precios = 0
producto_mas_caro = productos[0]

for p in productos:
    total_inventario += p['precio'] * p['cant_stock']
    stock_total += p['cant_stock']
    sumatoria_precios += p['precio']

    if p['precio'] > producto_mas_caro['precio']:
        producto_mas_caro = p

promedio_precio = sumatoria_precios / len(productos)

print(f"El total invertido en el inventario es: {total_inventario}")
print(f"La cantidad total de stock de los productos es: {stock_total}")
print(f"El producto más costoso es: {producto_mas_caro['nom_product']} con un precio de {producto_mas_caro['precio']}")
print(f"El promedio de precio de los productos es: {promedio_precio}")

