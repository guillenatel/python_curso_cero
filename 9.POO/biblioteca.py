from libro import libro; 
import json;


class biblioteca: 
    def __init__(self):
        self.lista_libros = []; 
        
    def agregar_libro(self,libro): 
        if(libro not in self.lista_libros): 
            self.lista_libros.append(libro);
            print(f"Libro agregado: {libro.titulo}");
        else: 
            print(f"El libro '{libro.titulo}' ya está en la biblioteca.");
    
    def eliminar_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.titulo == titulo:
                self.lista_libros.remove(libro)
                print(f"Libro eliminado: {libro.titulo}"); 
            else: 
                print(f"No se encontró el libro con título '{titulo}' en la biblioteca."); 
    
    def libros_disponibles(self): 
        print(f"Los libros que se encuentran disponibles son:\n"); 
        for libro in self.lista_libros: 
            if(libro.disponible == True):
                print(f"-{libro.titulo} / {libro.autor} / Año de publicación: {libro.ano_publicacion} / Unidades disponibles: {libro.unidades} "); 
            
    def prestar_libro(self,titulo): 
        for libro in self.lista_libros: 
            if(libro.titulo == titulo and libro.unidades > 0): 
                libro.unidades -= 1; 
                print(f"Libro prestado: {libro.titulo}"); 
            elif(libro.titulo == titulo and libro.unidades <= 0):
                libro.disponible = False; 
                print(f"No se puede prestar el libro '{titulo}'. No está disponible."); 
        
    
    def devolver_libro(self,titulo): 
        for libro in self.lista_libros:
            if(libro.titulo == titulo): 
                libro.unidades += 1; 
                libro.disponible = True; 
                print(f"Libro devuelto: {libro.titulo}"); 
            else: 
                (f"No se puede devolver el libro '{titulo}'. No está en la lista de libros prestados."); 
                
                
    def guardar_en_json(self, archivo):
        with open(archivo, 'w') as file:
            #dict --> devovlera un diccionario con sus atributos y valores asociciados
            data = [libro.__dict__ for libro in self.lista_libros]
            json.dump(data, file)

    
    def cargar_desde_json(self, archivo):
        #cargar biblioteca desde json
        pass

                
