#@author: Jereny Chica Tapasco
#@Fecha: 6-10-2026
#@Descripción: Ejercicio practico de manejo de diccionarios 

acetaminofen = {
    'id_product': 1,
    'nom_product': 'Acetaminofen',
    'precio': 5000,
    'descripcion': 'Acetaminofen 500mg, 20 tabletas',
    'cant_stock': 100
}
jarabevix = {
    'id_product': 2,
    'nom_product': 'Jarabe Vix',
    'precio': 8000,
    'descripcion': 'Jarabe Vix 100ml',
    'cant_stock': 50
}
atorvastatina = {
    'id_product': 3,
    'nom_product': 'Atorvastatina',
    'precio': 10000,
    'descripcion': 'Atorvastatina 10mg, 30 tabletas',
    'cant_stock': 75
}
enterogermina = {
    'id_product': 4,
    'nom_product': 'Enterogermina',
    'precio': 12000,
    'descripcion': 'Enterogermina 5ml, 10 viales',
    'cant_stock': 30
}
mareol = {
    'id_product': 5,
    'nom_product': 'Mareol',
    'precio': 15000,
    'descripcion': 'Mareol 10mg, 20 tabletas',
    'cant_stock': 40
}
aspirina = {
    'id_product': 6,
    'nom_product': 'Aspirina',
    'precio': 7000,
    'descripcion': 'Aspirina 500mg, 20 tabletas',
    'cant_stock': 60
}
electrolit = {
    'id_product': 7,
    'nom_product': 'Electrolit',
    'precio': 6000,
    'descripcion': 'Electrolit 500ml, sabor limón',
    'cant_stock': 80
}
gastrofast = {
    'id_product': 8,
    'nom_product': 'Gastrofast',
    'precio': 9000,
    'descripcion': 'Gastrofast 10mg, 20 tabletas',
    'cant_stock': 25
}
algodon = {
    'id_product': 9,
    'nom_product': 'Algodón',
    'precio': 3000,
    'descripcion': 'Algodón 100g',
    'cant_stock': 150
}
gasa = {
    'id_product': 10,
    'nom_product': 'Gasa',
    'precio': 4000,
    'descripcion': 'Gasa estéril 10x10cm, 10 unidades',
    'cant_stock': 200
}
productos = [
    acetaminofen,
    jarabevix,
    atorvastatina,
    enterogermina,
    mareol,
    aspirina,
    electrolit,
    gastrofast,
    algodon,
    gasa,
]

print("Listado de productos")
for producto in productos:
    print(f"""
    id_product: {producto['id_product']}
    nombre del producto: {producto['nom_product']}
    precio del producto: {producto['precio']}
    descripcion: {producto['descripcion']}
    cantidad en stock: {producto['cant_stock']}
""")

total_inventario = 0
stock_total = 0
sumatoria_precios = 0
producto_mas_caro = productos[0]

for producto in productos:
    total_inventario += producto['precio'] * producto['cant_stock']
    stock_total += producto['cant_stock']
    sumatoria_precios += producto['precio']

    if producto['precio'] > producto_mas_caro['precio']:
        producto_mas_caro = producto

promedio_precio = sumatoria_precios / len(productos)

print(f"El total invertido en el inventario es: {total_inventario}")
print(f"La cantidad total de stock es: {stock_total}")
print(
    f"El producto más costoso es: {producto_mas_caro['nom_product']} "
    f"con un precio de {producto_mas_caro['precio']}"
)
print(f"El promedio de precio de los productos es: {promedio_precio}")