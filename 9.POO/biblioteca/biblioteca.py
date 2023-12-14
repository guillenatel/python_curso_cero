from libro import Libro; 
import json;
import os; 


class Biblioteca: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []; 
    
    def mostrar_libros(self):
        print(f"Libros disponibles en la biblioteca {self.nombre}:");
        print(f"  Título   /    Autor  /  Año de publicación / Unidades / Disponibilidad");
        for libro in self.libros:
            print(libro.mostrar_libro()); 
    
    def prestar_libro(self,titulo): 
        for libro in self.libros: 
            if(libro.titulo == titulo and libro.unidades > 0): 
                libro.unidades -= 1; 
                print(f"Libro prestado: {libro.titulo}"); 
            elif(libro.titulo == titulo and libro.unidades <= 0):
                libro.disponible = False; 
                print(f"No se puede prestar el libro '{titulo}'. No está disponible."); 
        
    def devolver_libro(self,titulo): 
        for libro in self.libros:
            if(libro.titulo == titulo): 
                libro.unidades += 1; 
                libro.disponible = True; 
                print(f"Libro devuelto: {libro.titulo}"); 
            else: 
                (f"No se puede devolver el libro '{titulo}'. No encontrado o no prestado en esta biblioteca..");
    
    def agregar_libro(self,libro): 
        if(libro not in self.libros): 
            self.libros.append(libro);
            print(f"Libro '{libro.titulo}' agregado a la biblioteca {self.nombre}.");
        else: 
            print(f"El libro '{libro.titulo}' ya está en la biblioteca.");
    
    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro);
                print(f"Libro '{titulo}' eliminado de la biblioteca {self.nombre}.");
            else: 
                print(f"No se encontró el libro con título '{titulo}' en la biblioteca."); 
    

    def guardar_en_json(self, nombre_archivo):
        datos_biblioteca = {
            "nombre": self.nombre,
            "libros": [{"titulo": libro.titulo, "autor": libro.autor, "ano_publicacion": libro.ano_publicacion,"unidades": libro.unidades,"disponible": libro.disponible, } for libro in self.libros]
        }
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_biblioteca, archivo, indent=2);
        print(f"Datos de la biblioteca {self.nombre} guardados en '{nombre_archivo}'.");

    
    @classmethod  #metodo de clase recibe la clase como su primer parámetro, por convención llamado cls en lugar de self como en los métodos de instancia.
    def cargar_desde_json(cls, nombre_archivo):# cls es similar al self, cls representa a la clase misma 
        with open(nombre_archivo, 'r') as archivo:
            datos_biblioteca = json.load(archivo); 
        biblioteca = cls(datos_biblioteca["nombre"]);
        for libro_data in datos_biblioteca["libros"]:
            libro = Libro(libro_data["titulo"], libro_data["autor"], libro_data["ano_publicacion"], libro_data["unidades"], libro_data["disponible"]);
            biblioteca.libros.append(libro);
        print(f"Biblioteca {biblioteca.nombre} cargada desde '{nombre_archivo}'.");
        return biblioteca;
        
            
            
