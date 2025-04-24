print('Bienvenido al programa de gestión de inventarios'.center(60, '-'))
cantidad = []
productos = []
precio = []

while True:
    print("""
           (1) Añadir Productos 
           (2) Buscar Productos 
           (3) Modificar Productos 
           (4) Ver Productos 
           (5) Salir
                      """)
    
    respuesta = int(input('Ingrese su opción: '))
    if respuesta == 1:
        ac = int(input('Ingrese la cantidad del producto: '))
        ap = input('Ingrese el nombre del producto: ')  
        apre = float(input('Ingrese el precio del producto: '))

        cantidad.append(ac)
        productos.append(ap)
        precio.append(apre)

    elif respuesta == 2:
        buscador = input('Ingrese el nombre del producto que quiere buscar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            print('La cantidad del producto es:', cantidad[posicion])
            print('El nombre del producto es:', productos[posicion])
            print('El precio del producto es:', precio[posicion])
        else:
            print("Producto no encontrado.")

    elif respuesta == 3: 
        buscador = input('Ingrese el nombre del producto que quiere modificar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            ac = int(input('Ingrese la nueva cantidad del producto: ')) 
            ap = input('Ingrese el nuevo nombre del producto: ')  
            apre = float(input('Ingrese el nuevo precio del producto: '))  

            cantidad[posicion] = ac
            productos[posicion] = ap
            precio[posicion] = apre
        else:
            print("Producto no encontrado.")

    elif respuesta == 4: 
        print('Cantidad de productos:', cantidad)
        print('Nombres de productos:', productos)
        print('Precios de productos:', precio)

    elif respuesta == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")
