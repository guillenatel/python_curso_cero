class Libro: 
    def __init__(self,titulo,autor,ano_publicacion,unidades,disponible=True): 
        self.titulo = titulo;
        self.autor = autor; 
        self.ano_publicacion = ano_publicacion; 
        self.disponible = True; 
        self.unidades = unidades; 

    def mostrar_libro(self):
        return f"- {self.titulo} / {self.autor} / {self.ano_publicacion} / {self.unidades} / {'(Disponible)' if self.disponible else '(No disponible)'}"

        