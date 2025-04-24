print('Bienvenido al sistema de gestión de inventarios de MegaVentas'.center(80, '-'))

# almacenamiento de los productos con su ID como clave.
inventario = {}

while True:
    print("""
           (1) Añadir Producto 
           (2) Eliminar Producto 
           (3) Buscar Producto por ID
           (4) Listar Todos los Productos 
           (5) Salir
                      """)
    
    respuesta = input('Ingrese su opción: ')
    
    if respuesta == '1':
        id_producto = input('Ingrese el identificador único del producto: ')
        if id_producto in inventario:
            print("Error: El identificador ya existe. Intente con otro.")
        else:
            nombre = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad del producto: '))
            precio = float(input('Ingrese el precio del producto: '))
            inventario[id_producto] = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio}
            print("Producto agregado exitosamente.")
    
    elif respuesta == '2':
        id_producto = input('Ingrese el identificador del producto a eliminar: ')
        if id_producto in inventario:
            del inventario[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")
    
    elif respuesta == '3':
        id_producto = input('Ingrese el identificador del producto a buscar: ')
        if id_producto in inventario:
            producto = inventario[id_producto]
            print(f"ID: {id_producto}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']}")
        else:
            print("Error: Producto no encontrado.")
    
    elif respuesta == '4':
        if inventario:
            print("Listado de productos en inventario:")
            for id_producto, producto in inventario.items():
                print(f"ID: {id_producto}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']}")
        else:
            print("No hay productos en el inventario.")
    
    elif respuesta == '5':
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Inténtelo de nuevo.")