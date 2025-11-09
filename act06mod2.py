#Eres estudiante de último año de Ingeniería en Computación y te solicitan desarrollar un sistema sencillo para gestionar libros 
# en una biblioteca. Cada libro debe contar con información básica y debe ser posible acceder a sus detalles
# Requisito 1
# Crea la clase Libro con los atributos privados _titulo, _autor y _isbn (1 punto). 
class Libro: 
# Requisito 2
# Define un constructor para Libro que inicialice estos atributos al momento de crear un objeto (1 punto). 
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
# Requisito 3
#Implementa métodos get_titulo(), get_autor() y get_isbn() para obtener el valor de cada atributo 
# desde fuera de la clase (2 puntos). 
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_isbn(self):
        return self.__isbn
# Requisito 4
# Crea un método descripcion() en la clase Libro que retorne una cadena con los detalles del libro 
# en el formato “Título: [titulo], Autor: [autor], ISBN: [isbn]” (2 puntos). 
    def descripcion(self):
        print(f"Titulo: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}")

# Requisito 5
# Crea una clase Biblioteca que permita gestionar una lista de libros. Define un método 
# agregar_libro() para añadir un libro a la biblioteca (1 punto). 

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro'{libro}' añadido a la biblioteca.")
# Requisito 6
# Define un método mostrar_libro() en Biblioteca que recorra la lista de libros e imprima 
# la descripción de cada libro (2 puntos).     
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Los libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro}")
                print(Libro.descripcion(self)) 



informacion_libro = Libro("Dune", "Frank Herbert", 109867553)
informacion_libro2 = Libro("Harry Potter", "J.K. Rowling", 100009876)
informacion_libro3 = Libro("Lord of the Ring", "Tolkien", 109867553)


print(f"El nombre del titulo consultado es:",informacion_libro.get_titulo())
print(f"El nombre del autor consultado es:",informacion_libro.get_autor())
print(f"El ISBN del titulo consultado es:",informacion_libro.get_isbn())
informacion_libro.descripcion()
# Requisito 7
# Instancia la clase Biblioteca, crea al menos dos libros y añádelos a la biblioteca. 
# Luego, muestra los detalles de los libros almacenados (1 punto). 
biblioteca = Biblioteca()
biblioteca.agregar_libro({informacion_libro[1]})
biblioteca.agregar_libro({informacion_libro2[1]})
biblioteca.mostrar_libros()