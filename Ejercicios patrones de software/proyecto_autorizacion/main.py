def registrar_usuario():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    
    # Guardar el registro en un archivo
    with open("\Users\USER\Documents\Python y Pseint\Ejercicios patrones de software\proyecto_autorizacion\user.txt", "a") as file: 
        file.write(f"user:{username},password:{password}\n")
    print("Registro exitoso!")

def iniciar_sesion():
    while True:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")     
        # Verificar las credenciales
        with open("/user.txt", "r") as file:
            for line in file:
                # Extraer información del formato guardado
                stored_user = line.strip().split(',')[0].split(':')[1]
                stored_pass = line.strip().split(',')[1].split(':')[1]
                if stored_user == username and stored_pass == password:
                    print("Iniciaste sesicion correctamente")
                    return
        print("Usuario o contraseña incorrectos. Intente de nuevo.")
        opcion = input("¿Desea intentar nuevamente (1) o registrarse (2)? ")

        if opcion == '2':
            registrar_usuario()
            return  

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()