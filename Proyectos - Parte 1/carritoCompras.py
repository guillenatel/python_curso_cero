
listaProductos = [];

def agregarProducto():
    productosDisponibles = """
PRODUCTOS DISPONIBLES
1) Leche
2) Galletas
3) Gaseosa
4) Huevos
5) Aceite
6) Pan
    """
    print(productosDisponibles);

    while True:
        producto = input("Ingrese el producto que desea agregar: ");
        productos = producto.lower();

        if productos in ["leche", "galletas", "gaseosa", "huevos", "aceite", "pan"]:
            listaProductos.append(productos);
            break
        else:
            print("El producto ingresado no se encuentra disponible. Por favor, inténtelo de nuevo");
            
def eliminarProducto():
    while True:  
        producto = input("Ingrese el producto que desea eliminar: ");
        productos = producto.lower();

        if productos in listaProductos:
            listaProductos.remove(productos);
            break
        else:
            print("El producto ingresado no se encuentra en la lista. Por favor, inténtelo de nuevo");
            
def verListaCompras(): 
    print()
    print("Lista de compra")
    for productos in listaProductos: 
        print("-" + productos); 
    
def finalizarCompra(): 
    precioLeche = 50
    precioGalletas = 35
    precioGaseosa = 87
    precioHuevos = 66
    precioAceite = 110
    precioPan = 20

    total = 0
    print(); 
    print("LISTA DE LA COMPRA"); 
    print();
    for producto in listaProductos:
        if producto == "leche":
            total += precioLeche
        elif producto == "galletas":
            total += precioGalletas
        elif producto == "gaseosa":
            total += precioGaseosa
        elif producto == "huevos":
            total += precioHuevos
        elif producto == "aceite":
            total += precioAceite
        elif producto == "pan":
            total += precioPan
            
        print(f"- {producto}"); 
    print(); 
    print(f"Total ${total}"); 



menu = """
MENU
1) Agregar producto
2) Eliminar producto
3) Ver lista de compras
4) Finalizar compra
5) Salir
"""

while True:
    print(menu)
    opcion = int(input("Ingrese el número de la opción que desea realizar:"));

    if opcion < 1 or opcion > 5:
        print("No es una opción válida");
    elif opcion == 1:
        agregarProducto();
    elif opcion == 2:
        eliminarProducto(); 
    elif opcion == 3:
        verListaCompras(); 
    elif opcion == 4:
        finalizarCompra();
    elif opcion == 5:
        break;

