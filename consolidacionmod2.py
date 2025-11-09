# Requerimiento 1
# Definir variables básicas y tipos de datos (1 punto): 
# o Crea una lista que contenga al menos cinco libros, donde cada libro sea un diccionario con los 
# atributos título (cadena de caracteres), autor (cadena de caracteres), 
# precio (decimal) y cantidad en stock (entero)  
libro1 ={"titulo":"Dune","autor":"Herbert","precio":20000.00,"stock":4}
libro2 ={"titulo":"Harry Potter","autor":"J.K Rowling","precio":10000.00,"stock":10}
libro3 ={"titulo":"Lord of the Rings","autor":"J. Tolkien","precio":35000.00,"stock":0}
libro4 ={"titulo":"Bosque Oscuro","autor":"Cixin Liu","precio":25000.00,"stock":5}
libro5 ={"titulo":"1984","autor":"Orwell","precio":45000.00,"stock":0}

libros = [libro1, libro2, libro3, libro4, libro5]

# Requerimiento 2
# Implementa una función llamada mostrar_libros_disponibles() que recorra la lista de libros y muestre 
# en pantalla los libros que tienen más de una unidad en stock usando una sentencia for y una condición 
# if. 
def mostrar_libros_disponibles(lista): 
    print("Libros con más de 1 unidad en stock")
    for item in lista:
        if item["stock"] > 1:
            print(f"Titulo:{item['titulo']}")

mostrar_libros_disponibles(libros)
 
# Requerimiento 3
# Condiciones y operadores (1 punto): 
# Solicita al usuario que ingrese un rango de precios (mínimo y máximo) y utiliza una 
# sentencia if elif else para filtrar los libros en el rango ingresado y mostrarlos en pantalla.  
min = int(input("precio minimo: "))
max = int(input("precio maximo: "))
print(f"libros con precios entre {min} y {max:}: ")
for item in libros:
    if item ["precio"] >=min and item ["precio"] <= max:
        print(f"Titulo:{item['titulo']}")
                             
# Requerimiento 4
# Función personalizada para simular una compra (2 puntos): o Crea una función comprar_libros(título, cantidad) que reciba 
# como parámetros el título del libro y la cantidad a comprar. La función debe: 
# ▪ Verificar si el libro está en el inventario y si la cantidad deseada está disponible. 
# ▪ Si la compra es válida, restar la cantidad comprada al stock y mostrar el monto total de la compra. 
# ▪ Si la cantidad solicitada es mayor al stock disponible, mostrar un mensaje de error. 
def comprar_libros(titulo, cantidad):
    contador = 0
    for item in libros:
        if item ["titulo"] == titulo and item["stock"] >= cantidad:
            item["stock"] = item["stock"]-cantidad
            print(f"monto total de la compra: {item["precio"]*cantidad}")
        elif item["stock"] == titulo and item["stock"]<cantidad:
            print("no se encuentra el stock requerido")
        else:
            contador = contador +1
    if contador == len(libros):
        print("no se encontro el libro")
tit = input("Introduzca titulo deseado: ")
cant = int(input("Introduzca la cantidad deseada: "))
comprar_libros(tit, cant)            
        