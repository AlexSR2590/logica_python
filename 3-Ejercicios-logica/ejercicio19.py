"""
Dado una lista de objetos película (titulo, director, vista), pasar la lista de objetos películas
a una función, la función debe mostrar todas las películas indicando cuales has visto y cuáles no
Ejemplo:
mostrarPelicuas(peliculas)//Devuelve:
Constantine --- Has visto esta película
Pinocchio --- No has visto esta película
John Wick --- Has visto esta película

pelicula 1: Constantine, Director: Francis Lawrence, vista: Has visto esta película.
pelicula 2: Pinocchio, Director: Guillermo del toro, vista: No has visto esta película.
pelicula 3: John Wick, Director: Chad Stahelski, vista: Has visto esta película.
"""
class Pelicula():
    def __init__(self, titulo, director, vista):
        self.titulo = titulo
        self.director = director
        self.vista = vista

def mostrarPeliculas(lista_peliculas):
    listado_peliculas = ""
    for pelicula in lista_peliculas:
        if pelicula.vista == True:
            listado_peliculas += f"{pelicula.titulo} --- Has visto esta película.\n"
        else:
            listado_peliculas += f"{pelicula.titulo} --- No has visto esta película.\n"
    return listado_peliculas

pelicula1 = Pelicula("Constantine", "Francis Lawrence", True)
pelicula2 = Pelicula("Pinocchio", "Guillermo del toro", False)
pelicula3 = Pelicula("John Wick", "Chad Stahelski", True)

peliculas = [pelicula1, pelicula2, pelicula3]
print(mostrarPeliculas(peliculas))
