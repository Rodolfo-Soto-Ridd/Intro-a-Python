# Requerimiento 1
productos = ["Harry Potter", "Dune", "Lord of the Rings", "Bosque Oscuro", "House of Dragon"]
print(productos)
# Requerimiento 2
productos.append("Cryptonomicon")
print(productos)

productos.append("Un Mundo Feliz")
print(productos)

productos_destacados = productos[0:3]
print(productos_destacados)
# Requerimiento 3
inventario={"titulo1":{"nombre":"Harry Potter","stock":10},"titulo2":{"nombre":"Dune","stock":50},"titulo3":{"nombre":"Lord of the Rings","stock":120},"titulo4":{"nombre":"Bosque Oscuro","stock":500},"titulo5":{"nombre":"House of Dragon","stock":1000}}
print(inventario)
# Requerimiento 4
inventario["titulo6"] = {"nombre":"1984","stock":70}
print(inventario)

print(inventario.get("titulo5"))
# Requerimiento 5
categorias1 = ("Electronica","Ropa","Alimentos")
segundo_elemento = categorias1[1]
print(segundo_elemento)
# Requerimiento 6
categorias2 = "Perfumes", "Tecnologia", "Wellness"
a, b, c = categorias2
print(a)
print(b)
print(c)
# Requerimiento 7
productos_unicos = set(productos)
union = productos_unicos|productos_unicos
print(union)
# Requerimiento 8
productos_mayuscula = [x.upper() for x in productos]
print(productos_mayuscula)